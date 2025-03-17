from flask import Flask, request, jsonify
from produto_service import adicionar_produto , listar_produtos , apagar_produto , menu_principal

app = Flask(__name__)

# Rota para adicionar um produto
@app.route('/produtos', methods=['POST'])
def api_adicionar_produto():
    dados = request.json
    nome = dados.get('nome')
    preco = dados.get('preco')
    estoque = dados.get('estoque')

    if not nome or not preco or not estoque:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    adicionar_produto(nome, preco, estoque)
    return jsonify({"mensagem": "Produto adicionado com sucesso!"}), 201

# Rota para listar produtos
@app.route('/produtos', methods=['GET'])
def api_listar_produtos():
    produtos = listar_produtos()
    produtos_json = [{"id": p[0], "nome": p[1], "preco": float(p[2]), "estoque": p[3]} for p in produtos]
    return jsonify(produtos_json)

# Rota de teste
@app.route('/')
def index():
    return jsonify({"mensagem": "API de Vendas está rodando!"})

if __name__ == '__main__':
    app.run(debug=True)
