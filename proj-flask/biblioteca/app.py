import os
import csv
from flask import Flask, json, request
from flask_restful import Resource, Api

from models import Obras

app = Flask(__name__)
api = Api(app)

ARQUIVO_CSV = 'obras.csv'

class ObrasList(Resource):
    """
    Classe responsavel por listar todas as obras e também inserir uma nova obra na base de dados...
    """
    def get(self):
        obras = Obras.query.all()
        response = [{'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')} for obra in obras]
        return response

    def post(self):
        dados = request.json
        obra = Obras(titulo=dados['titulo'], editora=dados['editora'], autor=dados['autor'])
        obra.save()
        response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')}
        return response


class ObraPorId(Resource):
    """
    Classe responsavel por exibir uma obra através do parametro id e também por atualizar e deletar uma obra pelo id passando como parametro. 
    """
    def get(self, id:int):
        obra = Obras.query.filter_by(id=id).first()

        try:
            response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')}
        except AttributeError:
            response = {'status': 'error', 'menssage': 'Obra não encontrada...'}
        
        return response
    
    def put(self, id:int):
        obra = Obras.query.filter_by(id=id).first()
        dados = request.json

        if 'titulo' in dados:
            obra.titulo = dados['titulo']
        if 'editora' in dados:
            obra.editora = dados['editora']
        if 'autor' in dados:
            obra.autor = dados['autor']
        if 'foto' in dados:
            obra.foto - dados['foto']
        if 'criado_em' in dados:
            obra.criado_em = dados['criado_em']

        obra.save()
        response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')}
        return response

    def delete(self, id:int):
        obra = Obras.query.filter_by(id=id).first()
        try:
            obra.delete()
        except Exception:
            return {'status': 'error', 'menssage': 'Erro ao excluir a obra...'}
        return {'status': 'sucess', 'mensage': 'Obra excluída com sucesso.'}


class UploadObras(Resource):
    """
    Classe que recebe um arquivo *.csv e salva seus dados na base de dados...
    """
    def post(self):
        url = 'obras.csv'
        with open(url, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()
            
            for row in csv_reader:
                obra = Obras(titulo=row[0], editora=row[1], foto=row[2], autor=row[3])
                obra.save()

        obras = Obras.query.all()
        response = [{'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')} for obra in obras]
        return response


class UploadObrasComURL(Resource):
    """
    Classe que recebe um arquivo *.csv por parametro vindo de uma url e salva seus dados na base de dados...
    """
    def post(self, url:str):
        with open(url, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()
            
            for row in csv_reader:
                obra = Obras(titulo=row[0], editora=row[1], foto=row[2], autor=row[3])
                obra.save()

        obras = Obras.query.all()
        response = [{'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')} for obra in obras]
        return response


class FileObras(Resource):
    """
    Classe responsável por gerar o arquivo CSV apartir da base de dados... 
    """
    def get(self):
        obras = Obras.query.all()
        if(os.path.exists(ARQUIVO_CSV) and os.path.isfile(ARQUIVO_CSV)):
            os.remove(ARQUIVO_CSV)
        
        arquivo = csv.writer(open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8'))

        try:
            for obra in obras:
                arquivo.writerow([obra.titulo, obra.editora, obra.foto, obra.autor, obra.criado_em.strftime('%d/%m/%Y')])
        except Exception:
            return {'status': 'error', 'menssage': 'Erro ao gerar arquivo CSV...'}
        
        return {'status': 'sucess', 'mensage': 'Arquivo CSV gerado com sucesso.'}


api.add_resource(ObrasList, '/obras/')
api.add_resource(ObraPorId, '/obras/<int:id>/')
api.add_resource(UploadObras, '/upload-obras/')
api.add_resource(UploadObrasComURL, '/upload-obras/<string:url>/')
api.add_resource(FileObras, '/file-obras/')


if __name__ == '__main__':
    app.run(debug=True)
