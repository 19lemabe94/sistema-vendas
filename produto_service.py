from database import conectar



def menu_principal():
    print("\nMenu Principal")
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Apagar Produtos")
    print("4 - Alguma coisa")
    print("5 - Sair")

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

def apagar_produto(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM produto WHERE nome='{nome}';")
    conexao.commit()
    conexao.close()
    return nome