from models.produtosSistema import ProdutosSistema


def menu():
    opcao = 0
    while opcao != 5:
        print("\nEscolha uma opção:")
        print("1 - Ler Produtos")
        print("2 - Cadastrar Produto")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("5 - Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número."  )

        if opcao == 1:
            ProdutosSistema.read()
        elif opcao == 2:
            ProdutosSistema.create()
        elif opcao == 3:
            ProdutosSistema.update()
        elif opcao == 4:
            ProdutosSistema.delete()
        elif opcao == 5:
            print("Encerrando o sistema...")
        else:
            print("Opcao Invalido. Tente novamente.")
    
