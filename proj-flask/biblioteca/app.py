import csv
from flask import Flask, json, request
from flask_restful import Resource, Api

from models import Obras

app = Flask(__name__)
api = Api(app)

class ObrasList(Resource):
    """
    Classe responsavel por listar todas as obras e por inserir uma nova obra na base de dados...
    """
    def get(self):
        obras = Obras.query.all()
        response = [{'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')} for obra in obras]
        return response

    def post(self):
        dados = request.json
        obra = Obras(titulo=dados['titulo'], editora=dados['editora'], autor=dados['autor'])
        obra.save()
        response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': str(obra.criado_em)}
        return response


class ObraPorId(Resource):
    """
    Classe responsavel por exibir uma obra através do parametro id e também por atualizar e deletar uma obra pelo id passando como parametro. 
    """
    def get(self, id:int):
        obra = Obras.query.filter_by(id=id).first()

        try:
            response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': str(obra.criado_em)}
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
        response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': str(obra.criado_em)}
        return response

    def delete(self, id:int):
        obra = Obras.query.filter_by(id=id).first()
        try:
            obra.delete()
        except Exception:
            return {'status': 'error', 'menssage': 'Erro ao excluir a obra...'}
        return {'status': 'sucess', 'mensage': 'Obra excluída com sucesso.'}


class UploadObras(Resource):
    def post(self):
        with open('obras.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()
            
            for row in csv_reader:
                obra = Obras(titulo=row[0], editora=row[1], foto=row[2], autor=row[3])
                obra.save()

        obras = Obras.query.all()
        response = [{'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'foto': obra.foto, 'autor': obra.autor, 'criado_em': obra.criado_em.strftime('%d/%m/%Y')} for obra in obras]
        return response


api.add_resource(ObrasList, '/obras/')
api.add_resource(ObraPorId, '/obras/<int:id>/')
api.add_resource(UploadObras, '/upload-obras/')


if __name__ == '__main__':
    app.run(debug=True)
