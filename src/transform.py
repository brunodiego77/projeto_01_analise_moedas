import json
import pandas as pd
import os

CAMINHO_RAW = r"C:\Users\Robert\Desktop\projeto_01\data\raw\historico_completo.json"
PASTA_STG = r"C:\Users\Robert\Desktop\projeto_01\data\stg"

def transformar_dados():
    with open(CAMINHO_RAW, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Transformando Moedas
    lista_moedas = []
    for nome_moeda, historico in dados['moedas'].items():
        df_temp = pd.DataFrame(historico)
        df_temp['moeda'] = nome_moeda
        lista_moedas.append(df_temp)
    
    df_moedas = pd.concat(lista_moedas)
    
    # --- LIMPEZA E TRATAMENTO (Silver Layer) ---
    df_moedas['name'] = df_moedas['name'].ffill()
    df_moedas['code'] = df_moedas['code'].ffill()
    df_moedas['codein'] = df_moedas['codein'].ffill()
    
    # Criar coluna de data oficial e remover as que não prestam
    df_moedas['data'] = pd.to_datetime(df_moedas['timestamp'], unit='s')
    df_moedas = df_moedas.drop(columns=['create_date', 'timestamp'])
    
    # Exportar para a pasta STG
    caminho_final = os.path.join(PASTA_STG, "stg_moedas_silver.csv")
    df_moedas.to_csv(caminho_final, index=False)
    print(f"✅ Arquivo Silver salvo em: {caminho_final}")

if __name__ == "__main__":
    transformar_dados()