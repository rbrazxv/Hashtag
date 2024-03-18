# Passo a Passo do Projeto de Automação de Tarefas - Cadastro de Materiais
# 1º Passo - Entrar no sistema da empresa
        # "Site da Empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Para controlar os processos de execução, usaremos a biblioteca Pyautogui.
import pyautogui
import time
sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 1
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "l")
pyautogui.write(sistema)
pyautogui.press("enter")
time.sleep(5)

# 2º Passo - Fazer Login
login = "raayanrocha@gmail.com"
senha = "NeymarJr10#"
pyautogui.click(586, 379)
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(senha)  
pyautogui.press("tab")
pyautogui.press("enter")

# 3º Passo - Importar  a Base de Dados
# Para trabalhar com a Análise de Dados, vamos utilizar a biblioteca Pandas.
import pandas
tabela = pandas.read_csv(r"C:\Users\Rayan\Documents\Python PowerUp\produtos.csv")
# print(tabela)

pyautogui.PAUSE = 0.5

for linha in tabela.index:

        # 4º Passo - Cadastrar um Produto 
        # 5º Passo - Repetir o processo até o fim da Base de Dados  
        pyautogui.click(461, 261)

        # Coluna Código
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(codigo)
        pyautogui.press("tab")

        # Coluna Marca
        marca = tabela.loc[linha, "marca"]
        pyautogui.write(marca)
        pyautogui.press("tab")

        # Coluna Tipo
        tipo = tabela.loc[linha, "tipo"]
        pyautogui.write(tipo)
        pyautogui.press("tab")

        # Coluna Categoria
        categoria = tabela.loc[linha, "categoria"]
        pyautogui.write(str(categoria))
        pyautogui.press("tab")

        # Coluna Preço Unitário
        precounitario = tabela.loc[linha, "preco_unitario"]
        pyautogui.write(str(precounitario))
        pyautogui.press("tab")

        # Coluna Custo
        custo = tabela.loc[linha, "custo"]
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        # Coluna Observação
        obs = tabela.loc[linha, "obs"]
        if not pandas.isna(obs):
                pyautogui.write(obs)
        pyautogui.press("tab")
        
        #Registrar o item e subir a tela para novo cadastro
        pyautogui.press("enter")
        pyautogui.scroll(2000)


