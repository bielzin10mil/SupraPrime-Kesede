
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

produtos = [
    {
        'id': 1,
        'titulo': "Nutri Whey Protein",
        'marca': "Whey",
        'preco': 50
        
    },
    {
        'id': 2,
        'titulo': "Creatina Pura",
        'marca': "Creatina",
        'preco': 60
        
    },
    {
        'id': 3,
        'titulo': "Pré-treino Diabo Verde",
        'marca': "Diabo verde",
        'preco': 80
        
    },
]


@app.route('/produtos', methods=['GET'])
def obter_produtos():
    return jsonify(produtos)

#consulta
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produtos_por_id(id):
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)
        

#editar
@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto_por_id(id):
    produto_alterado = request.get_json()
    for indice,produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(produto_alterado)
            return jsonify(produtos[indice])



#criar
@app.route('/produtos', methods=['POST'])
def incluir_novo_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)

    return jsonify(produtos)


#excluir
@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]

    return jsonify(produtos)

app.run(port=5000,host='localhost',debug=True)

