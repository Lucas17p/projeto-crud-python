#Projeto C.R.U.D - create read update delet
class ProdutosSistema:
    item = {
        "Notebook X": 3500.00,
        "Smartphone Y": 1500.00,
        "Tablet Z": 800.00
    }


    @classmethod
    def create(cls):
        novo_produto = input("Digite o nome do novo produto: ")
        
        if novo_produto in cls.item:
            print("Produto já está na lista.")
            return # Sai da função e não faz mais nada

        try:
            preco_produto = float(input(f"Digite o preço de '{novo_produto}': R$ "))
        except ValueError:
            print("Erro: Preço inválido.")
            return

        cls.item[novo_produto] = preco_produto
        print(f"Produto {novo_produto} cadastrado com sucesso!")



#Read
    @classmethod 
    def read(cls):
        print("Produtos cadastrados: ")
        for i, produto in enumerate(cls.item, start=1):
            preco = cls.item[produto]
            print(f"{i}. {produto} - R$ {preco:.2f}")



#Update
    @classmethod
    def update(cls):
        cls.read()
        try:
            escolha = int(input("\nDigite o número do produto que deseja alterar: "))
            
            ant_produto = None
            
            # Acha o produto pelo número
            for i, produto in enumerate(cls.item, start=1):
                if i == escolha:
                    ant_produto = produto
                    break 
                    
            if ant_produto is not None:
                # 1. Pede o novo nome (se der Enter vazio, mantém o atual)
                novo_produto = input(f"Novo nome para '{ant_produto}' (ou aperte Enter para manter): ").strip()
                if novo_produto == "": #Se digitar o enter
                    novo_produto = ant_produto # Mantém o nome antigo
                
                # 2. Pede o novo preço
                preco_atual = cls.item[ant_produto]
                novo_preco_str = input(f"Novo preço (atual: R$ {preco_atual:.2f}) ou aperte Enter para manter: ").strip()
                
                # Se o usuário não digitou nada, mantém o preço antigo. Se digitou, converte para float.
                if novo_preco_str == "":
                    novo_preco = preco_atual 
                else:
                    novo_preco = float(novo_preco_str) 
                
                # 3. Atualiza no dicionário
                # Se o nome mudou, precisamos deletar a chave antiga
                if novo_produto != ant_produto:
                    del cls.item[ant_produto]
                
                # Cria/Atualiza a chave com o preço definido
                cls.item[novo_produto] = novo_preco
                
                print(f"Sucesso! O produto atualizado '{novo_produto}' custando R$ {novo_preco:.2f}.")
                
            else:
                print("Número inválido! Esse produto não existe.")

        except ValueError:
            print("Entrada inválida! Certifique-se de digitar os valores corretamente.")



#Delete
    @classmethod
    def delete(cls):
        while True:
            cls.read()

            try:
                escolha = int(input("\nDigite o número do produto que deseja deletar: "))
            except ValueError:
                print("Entrada Inválida. Por favor, digite um número.")
                continue

            ant_produto = None
            
            # 1. Percorre o dicionário para achar o produto pelo número
            for i, produto in enumerate(cls.item, start=1):
                if i == escolha:
                    ant_produto = produto
                    break 
            
            # 2. Faz a exclusão usando o 'del' se o produto foi encontrado
            if ant_produto is not None:
                del cls.item[ant_produto]
                print(f"Produto '{ant_produto}' deletado com sucesso!")
                break  # Sai do loop 'while' após deletar com sucesso
            else:
                print("Número inválido! Esse produto não existe na lista.")
#FIM ClASSEs----


