# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from csv import reader
with open ('original.csv', errors='ignore') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'O lutador(a) {linha[0]} nasceu no(a)(s) {linha[1]} e sua altura é {linha[2]} centimetros ')