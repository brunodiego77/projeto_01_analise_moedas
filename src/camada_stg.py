import json
import pandas as pd
import os

# Caminhos
CAMINHO_RAW = r"C:\Users\Robert\Desktop\projeto_01\data\raw\historico_completo.json"
PASTA_STG = r"C:\Users\Robert\Desktop\projeto_01\data\stg"

os.makedirs(PASTA_STG, exist_ok=True)

def transformar_dados():
    with open(CAMINHO_RAW, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # 1. Transformando Commodities
    print("Transformando Commodities...")
    df_commodities = pd.DataFrame(dados['commodities'])
    df_commodities.index.name = 'Data'
    df_commodities.to_csv(os.path.join(PASTA_STG, "stg_commodities.csv"))
    print("✅ Commodities salvas em: data/stg/stg_commodities.csv")

    # 2. Transformando Moedas
    print("Transformando Moedas...")
    lista_moedas = []
    
    for nome_moeda, historico in dados['moedas'].items():
        # A API retorna uma lista de dicionários para cada moeda
        df_temp = pd.DataFrame(historico)
        df_temp['moeda'] = nome_moeda
        lista_moedas.append(df_temp)
    
    df_moedas_final = pd.concat(lista_moedas)
    # Selecionando colunas relevantes para análise
    df_moedas_final = df_moedas_final[['moeda', 'bid', 'create_date']]
    df_moedas_final.to_csv(os.path.join(PASTA_STG, "stg_moedas.csv"), index=False)
    print("✅ Moedas salvas em: data/stg/stg_moedas.csv")

if __name__ == "__main__":
    transformar_dados()