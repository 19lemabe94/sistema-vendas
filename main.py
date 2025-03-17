from produto_service import adicionar_produto , listar_produtos , apagar_produto , menu_principal

menu_principal()

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
    nome = input("Nome do Produto: ")
    input("VOCE QUER REALMENTE APAGAR O PRODUTO? (S/N)").lower
    apagar_produto(nome)
    print("Produto Apagado com sucesso !")
    print(nome)

menu_principal()