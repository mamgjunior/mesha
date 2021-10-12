"""
    Feito para gerar inserts para testes o banco de dados...
"""
from models import Obras

def inserir_obras(titulo: str, editora: str, autor: str):
    obra = Obras(titulo=titulo, editora=editora, autor=autor)
    obra.save()

def consultar_obras():
    obras = Obras.query.all()
    print(obras)

if __name__ == '__main__':
    inserir_obras('O Senhor do aneis', 'Allen & Unwin', 'J. R. R. Tolkien')
    consultar_obras()
