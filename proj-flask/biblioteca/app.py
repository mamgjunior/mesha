from flask import Flask, json, request
from flask_restful import Resource, Api
from werkzeug.wrappers import response

from models import Obras

app = Flask(__name__)
api = Api(app)


class Obra(Resource):
    """
    Classe responsavel por exibir uma obra através do parametro id e também por atualizar e deletar uma obra pelo id passando como parametro. 
    """
    def get(self, id:int):
        obra = Obras.query.filter_by(id=id).first()

        try:
            response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'autor': obra.autor, 'criado_em': str(obra.criado_em)}
        except AttributeError:
            response = {'status': 'error', 'menssage': 'Obra nao encontrada!'}
        
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
        if 'criado_em' in dados:
            obra.criado_em = dados['criado_em']

        obra.save()
        response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'autor': obra.autor, 'criado_em': str(obra.criado_em)}
        return response

    def delete(self, id:int):
        obra = Obras.query.filter_by(id=id).first()
        try:
            obra.delete()
        except Exception:
            return {'status': 'error', 'menssage': 'Erro ao excluir a obra!'}
        return {'status': 'sucess', 'mensage': 'Obra excluida com sucesso.'}


class ListarObras(Resource):
    """
    Classe responsavel por listar todas as obras e por inserir uma nova obra na base de dados...
    """
    def get(self):
        obras = Obras.query.all()
        response = [{'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'autor': obra.autor, 'criado_em': str(obra.criado_em)} for obra in obras]
        return response

    def post(self):
        dados = request.json
        obra = Obras(titulo=dados['titulo'], editora=dados['editora'], autor=dados['autor'])
        obra.save()
        response = {'id': obra.id, 'titulo': obra.titulo, 'editora': obra.editora, 'autor': obra.autor, 'criado_em': str(obra.criado_em)}
        return response


api.add_resource(Obra, '/obras/<int:id>/')
api.add_resource(ListarObras, '/obras/')

if __name__ == '__main__':
    app.run(debug=True)
