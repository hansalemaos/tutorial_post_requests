# COMO MODIFICAR O PACOTE E SUBIR NO SERVIDOR

import glob
import os
from time import sleep

import pandas as pd
import requests
import bs4
from PrettyColorPrinter import add_printer

add_printer(1)

df = pd.read_pickle(r"C:\requestsdfs\1693834124.7608266.pkl")
arquivos = glob.glob(r'C:\arquivosparasubir\*.txt')
with open(r"C:\newfile.txt", mode='rb') as f:
    dados_subidos = f.read()
for arquivo in arquivos:
    body = df.iloc[0]._body
    header = df.iloc[0].headers.copy()
    with open(arquivo, mode='rb') as f:
        dados_para_subir = f.read()
    body_atualizado = body.replace(dados_subidos, dados_para_subir)
    nome_do_arquivo = arquivo.split(os.sep)[-1].encode()
    body_atualizado = body_atualizado.replace(b'filename="newfile.txt"',
                                              b'filename="' + nome_do_arquivo + b'"')
    header['Content-Length'] = str(len(body_atualizado))
    res = requests.post("https://testpages.eviltester.com/uploads/fileprocessor",
                        headers=header, data=body_atualizado)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())
    # @sleep(.5)
