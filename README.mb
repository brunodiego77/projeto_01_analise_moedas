# 📊 Análise de Ativos: Risco vs. Segurança (Bitcoin, Dólar e Ouro)

## 🎯 Objetivo do Projeto
Este projeto tem como objetivo analisar o comportamento de diferentes classes de ativos financeiros entre 2025 e 2026, respondendo a uma pergunta central de negócios: **Quem é o ativo mais volátil e quem é o mais confiável no mercado atual?** A análise explora a dinâmica de *Risk-On* (apetite ao risco) e *Risk-Off* (aversão ao risco), comparando o Bitcoin (ativo digital de risco) com o Dólar (reserva fiduciária) e o Ouro (reserva física).

## 🛠️ Tecnologias Utilizadas
* **Python:** Extração e transformação de dados.
* **Pandas:** Limpeza, padronização (Camadas Bronze e Silver) e cálculos estatísticos.
* **Matplotlib:** Visualização de dados (gráficos de duplo eixo e escalas logarítmicas).
* **AwesomeAPI:** Consumo de dados financeiros reais via REST API.

## 📂 Arquitetura dos Dados
O projeto segue boas práticas de Engenharia de Dados:
* `src/`: Scripts Python de extração (`extract.py`) e limpeza (`transform.py`) automatizada.
* `data/stg/`: Camada Silver contendo os dados limpos e padronizados prontos para análise.
* `notebooks/`: Camada de visualização e inteligência de negócios.

## 📈 Principais Conclusões (Insights)

Através do cálculo de desvio padrão dos retornos diários, o projeto provou matematicamente o comportamento de cada ativo:

1. **Dólar Americano (0.67% de volatilidade):** O ativo mais confiável. Comprova sua posição como reserva fiduciária global (*Risk-Off*).
2. **Ouro (1.12% de volatilidade):** O meio-termo. Sofre com oferta/demanda de commodities, mas mantém sua solidez histórica.
3. **Bitcoin (2.06% de volatilidade):** O ativo mais volátil. Balança 3x mais que o Dólar, confirmando sua tese de ativo de alto risco (*Risk-On*).