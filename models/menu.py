from models import produtosSistema

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
            continue

        #Read
        if opcao == 1:                
            produtosSistema.read()

        #Create
        elif opcao == 2:
            print("\n--- NOVO CADASTRO ---")
            while True:
                produto = str(input("Qual produtos deseja adicionar? "))

                try: 
                    valor = float(input("Qual o valor do produto? "))
                    break
                except ValueError:
                    print("Por favor digite apenas numeros. Use ponto ao inves de virgula\n")
                    continue
            produtosSistema.create(produto, valor)
            produtosSistema.read()


        #Update:
        elif opcao == 3:
            while True:
                
                while True:
                    try:
                        id_digitado = int(input("Qual o id do produto que deseja atualizar? "))
                        break
                    except ValueError:
                        print("Por favor digite apenas numeros.")
                        produtosSistema.read()

                novo_nome = input("Qual o novo nome do produto? ")
                
                while True:
                    try:
                        novo_valor = float(input("Qual o novo valor do produto? "))
                        break 
                    except ValueError:
                        print("Por favor, digite apenas números para o valor.\n")

                houve_sucesso = produtosSistema.update(id_digitado, novo_nome, novo_valor)
                    
                if houve_sucesso: # se nao volta no primeiro while
                    break 
        
        #Delete
        elif opcao == 4:
            produtosSistema.read()
            
            while True:
                try:
                    id_digitado = int(input("Qual o id que deseja excluir? "))
                    break
                except ValueError:
                    print("Digite apenas valores inteiros.")
                    produtosSistema.read()
                
            houve_sucesso = produtosSistema.delete(id_digitado)
            if houve_sucesso:
                print("Produto deletado com sucesso.")


        elif opcao == 5:
            print("Encerrando o sistema...")
            break

        else:
            print("Opcao Invalido. Tente novamente.")
    
