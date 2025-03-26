
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
# Ativar CORS para todas as rotas
CORS(app)  

# Configuração da conexão com o banco de dados

conexao_banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="191069",
    database="usuarios"
)

@app.route('/api/dados', methods=['GET'])
def obter_dados():
    cursor = conexao_banco.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    resultados = cursor.fetchall()
    cursor.close()

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
