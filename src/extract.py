import requests
import yfinance as yf
import json
import os
import time
from datetime import datetime

# Configurações do projeto
PASTA_RAW = r"C:\Users\Robert\Desktop\projeto_01\data\raw"
OS_ANOS = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
MOEDAS = ["USD-BRL", "EUR-BRL", "GBP-BRL", "JPY-BRL", "BTC-BRL", "ARS-BRL", "PYG-BRL", "CNY-BRL"]

os.makedirs(PASTA_RAW, exist_ok=True)

def extrair_historico():
  # 2. Commodities (Ajuste para converter as chaves de data para texto)
    print("Extraindo Commodities...")
    commodities = {"Petroleo_Brent": "BZ=F", "Ouro": "GC=F"}
    dados_commodities = {}
    
    for nome, ticker in commodities.items():
        ativo = yf.Ticker(ticker)
        df = ativo.history(start="2019-01-01", end=datetime.now().strftime("%Y-%m-%d"))
        
        # A MÁGICA ESTÁ AQUI: Converter as datas do índice para string formatada
        df.index = df.index.strftime('%Y-%m-%d')
        
        dados_commodities[nome] = df['Close'].to_dict()
        print(f"✅ {nome} baixado.")

    # 2. Moedas (AwesomeAPI com nossa "Política de Gentileza")
    print("\nIniciando extração de Moedas (com intervalo de 1 min)...")
    dados_moedas = {}

    for moeda in MOEDAS:
        print(f"-> Extraindo {moeda}...")
        # A AwesomeAPI permite até 365 dias por chamada histórica
        # Para simplificar, faremos uma requisição por moeda (o histórico completo)
        url = f"https://economia.awesomeapi.com.br/json/daily/{moeda}/3650"
        
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados_moedas[moeda] = resposta.json()
                print(f"   ✅ Sucesso.")
            else:
                print(f"   ❌ Falha: {resposta.status_code}")
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            
        print("   Aguardando 60 segundos por gentileza...")
        time.sleep(60)

    # 3. Salvamento Final
    dados_finais = {"moedas": dados_moedas, "commodities": dados_commodities}
    caminho = os.path.join(PASTA_RAW, "historico_completo.json")
    
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados_finais, f, indent=4)
        
    print(f"\n🚀 Carga histórica concluída com sucesso! Salvo em: {caminho}")

if __name__ == "__main__":
    extrair_historico()