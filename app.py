from flask import Flask, jsonify

app = Flask(__name__)

# Dados em memória - lista de dicionários com livros
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
    {"id": 3, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"id": 4, "titulo": "O Guarani", "autor": "José de Alencar"},
    {"id": 5, "titulo": "Iracema", "autor": "José de Alencar"}
]

@app.route('/livros', methods=['GET'])
def listar_livros():
    """
    Rota para listar todos os livros cadastrados
    Retorna: JSON com lista de livros (id, título, autor)
    """
    return jsonify(livros)

@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    """
    Rota para obter um livro específico pelo ID
    Parâmetros: livro_id (int) - ID do livro
    Retorna: JSON com dados do livro ou erro 404 se não encontrado
    """
    # Procura o livro pelo ID
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    
    if livro:
        return jsonify(livro)
    else:
        return jsonify({"erro": "Livro não encontrado"}), 404

@app.route('/')
def home():
    """
    Rota inicial com informações sobre o sistema
    """
    return jsonify({
        "mensagem": "Sistema de Livros - Versão Básica",
        "rotas_disponiveis": {
            "/livros": "Lista todos os livros",
            "/livros/<id>": "Busca livro por ID"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)