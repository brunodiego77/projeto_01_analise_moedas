import pandas as pd

# 1. Carrega o dado bruto
df_comm_bronze = pd.read_csv(r"C:\Users\Robert\Desktop\projeto_01\data\stg\stg_commodities.csv")

# 2. Renomeia a coluna esquecida para 'data' e converte para datetime
df_comm_bronze = df_comm_bronze.rename(columns={"Unnamed: 0": "data"})
df_comm_bronze["data"] = pd.to_datetime(df_comm_bronze["data"])

# 3. Transforma a tabela (Melt) para o padrão vertical: data, code, bid
df_comm_silver = df_comm_bronze.melt(id_vars=["data"], var_name="code", value_name="bid")

# 4. Padroniza os nomes para os códigos internacionais
df_comm_silver["code"] = df_comm_silver["code"].replace({
    "Ouro": "XAU", 
    "Petroleo_Brent": "XBR"
})

# 5. Salva na pasta stg
caminho_silver = r"C:\Users\Robert\Desktop\projeto_01\data\stg\stg_commodities_silver.csv"
df_comm_silver.to_csv(caminho_silver, index=False)

print("✅ Arquivo Silver criado com sucesso!")
df_comm_silver.head()