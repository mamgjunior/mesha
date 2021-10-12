"""
    Feito para gerar inserts para testes o banco de dados...
"""

import csv
from models import Obras

def inserir_obras(titulo: str, editora: str, autor: str):
    obra = Obras(titulo=titulo, editora=editora, autor=autor)
    obra.save()

def consultar_obras():
    obras = Obras.query.all()
    print(obras)

def ler(arquivo):
    with open(arquivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_reader.__next__()

        for row in csv_reader:
            print(row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3])

if __name__ == '__main__':
    # inserir_obras('O Senhor do aneis', 'Allen & Unwin', 'J. R. R. Tolkien')
    # consultar_obras()
    ler('obras.csv')
