# Projeto de inteligência artifícial com previsões - Estudo de Caso de um banco para liberação de crédito.
# Descrição do passo a passo do projeto.
# 1º Passo - Entender o desafio da empresa.
# 2º Passo - Importar a Base de Dados.
# 3º Passo - Adequar a Base de Dados para a IA.
# 4º Passo - Criar um modelo de IA - Nesse estudo de caso, uma IA que prevê Score de Crédito. (Ruim, Médio ou Bom)
# 5º Passo - Escolher o melhor modelo - O com maior precisão.
# 6º Passo - Usar a IA para realizar as previsões.

# Usaremos as Bibliotecas Pandas e Scikit-learn - Scikit-learn é a mais abrangente ferramenta IA.
# Kaggle - Site com base de dados reais para testes.

# 2º Passo:
import pandas as pd
tabela = pd.read_csv("clientes.csv")
#print(tabela)

# 3º Passo:
# Realizar adequação nas colunas = profissão, mix_credito e comportamento_pagamento. - Necessário transformar textos para número.

from sklearn.preprocessing import LabelEncoder
codificador = LabelEncoder()
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])
print(tabela)

# 4º Passo:
# Dividir tabela em X e Y, sendo X os dados utilizados para prever e Y a coluna que você quer prever.
    # Dropar as colunas desnecessárias = score_credito porque é a que queremos prever e id_cliente por ser um valor aleatorio.
# Aprendizado de máquina. Realizar a divisão da Base de Dados em dados de treino e dados de testes.

y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"])

from sklearn.model_selection import train_test_split
xtreino, xteste, ytreino, yteste = train_test_split(x, y)

# Ainda no 4º Passo:
# Criar, Treinar, Comparar os modelos de IA.
# Árvore de Decisão - RandomForest
# KNN - Nearest Neighbors - Kneighbors

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

ArvoreDecisao = RandomForestClassifier()
KNN = KNeighborsClassifier()

# Treino
ArvoreDecisao.fit(xtreino, ytreino)
KNN.fit(xtreino, ytreino)

# Teste
PrevisaoArvoreDecisao = ArvoreDecisao.predict(xteste)
PrevisaoKNN = KNN.predict(xteste.to_numpy())

# Acurácia
from sklearn.metrics import accuracy_score 
print(accuracy_score(yteste, PrevisaoArvoreDecisao))     
print(accuracy_score(yteste, PrevisaoKNN))

# 5º Passo:
# Modelo de Árvore de decisão teve uma melhor Acurácia = Apróx. 83%

NovosClientes = pd.read_csv("novos_clientes.csv")
print(NovosClientes)

# Assim como na tabela inicial, é necessário adequar as informações nas Colunas que estão com textos.
NovosClientes["profissao"] = codificador.fit_transform(NovosClientes["profissao"])
NovosClientes["mix_credito"] = codificador.fit_transform(NovosClientes["mix_credito"])
NovosClientes["comportamento_pagamento"] = codificador.fit_transform(NovosClientes["comportamento_pagamento"])
#print(NovosClientes)

# Novas Previsões
NovasPrevisoes = ArvoreDecisao.predict(NovosClientes)
print(NovasPrevisoes)