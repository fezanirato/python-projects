#Passo 1: Entrar no sistema da empresa 
#Passo 2: Fazer Login
#Passo 3: Importar a base de Dados
#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir para todos os produtos

# import pyautogui -> para importar a biblioteca de automações com python
# import time -> importa o tempo de espera (ex: time.sleep())

# pyautogui.press -> pressiona alguma tecla do teclado
# pyautogui.click -> clica com o botão do mouse de acordo com coordenadas
# pyautogui.write -> escreve algum texto
# pyautogui.hotkey -> combinação de teclas (ex: ctrl+c)

import pyautogui
import time

pyautogui.PAUSE = 0.5  # Define a pausa global

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(2)  # espera manualmente o Chrome abrir

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=538, y=403)
pyautogui.write("felipe.zanirato@outlook.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")

time.sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = str(tabela.loc[linha, "categoria"]) 
    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) #a função str() transforma a informação em uma string.
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])


    pyautogui.click(x=501, y=288)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    if obs != "nan":  #condição para não escrever "nan" em campos vazios.
        pyautogui.write(obs)

    pyautogui.press("tab")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(500)
    time.sleep(1)