from produto_service import adicionar_produto , listar_produtos

while True:
    print("\nMenu Principal")
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        adicionar_produto(nome, preco, estoque)
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        produtos = listar_produtos()
        for p in produtos:
            print(p)

    elif opcao == "3":
        break
