from database import conectar

def adicionar_produto(nome, preco, estoque):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Produto (nome, preco, estoque) VALUES (%s, %s, %s)",
                   (nome, preco, estoque))
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos
