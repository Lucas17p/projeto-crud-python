#Projeto C.R.U.D - create read update delet

import sqlite3


#Create
def create(nome_produto, valor_produto):
    #Separacao por responsabilidade (não teremos entrada aqui!)
    # IMPORTANTE: O uso dos (?) impede ataques de SQL Injection 
    # junto com a tupla de variáveis. Eles limpam o texto digitado pelo usuário.

    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    #Adicionar ao banco
    cursor.execute('''
        INSERT INTO produtos(produto,valor)
        VALUES(?,?)
    ''',(nome_produto, valor_produto))

    conexao.commit()
    conexao.close()

    print(f"Produto {nome_produto} cadastrado com sucesso!")
    read()




#Read
def read():
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT * FROM produtos      
    ''')

    #guardar resposta do banco
    #fetchal devolve lista de tuplas.
    lista_produtos = cursor.fetchall()

    print("\n--- ESTOQUE ATUAL ---")
    print("ID | PRODUTO | VALOR")
    for item in lista_produtos:
        print(f" {item[0]} | {item[1]} R${item[2]:.2f}")
        print("---------------------\n")

    conexao.close()


#Update
def update(id_produto, novo_produto, novo_valor):
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE produtos
        SET produto = ? , valor = ?
        WHERE id = ?           
    ''',(novo_produto, novo_valor, id_produto))

    linhas_alteradas = cursor.rowcount #contar quantas linhas mudaram

    conexao.commit()
    conexao.close()


    if linhas_alteradas > 0:
        print(" Produto atualizado com sucesso!")
        read()
        return True
    else:
        print(f"Erro: O ID {id_produto} não foi encontrado no banco de dados!")
        return False





#Delete
def delete(id_produto):
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM produtos
        WHERE id = ?
    ''', (id_produto,))

    linhas_alteradas = cursor.rowcount

    conexao.commit()
    conexao.close()


    if linhas_alteradas > 0:
        print("Produto excluído com sucesso!")
        read()
        return True
    else:
        print(f"Erro: O ID {id_produto} não foi encontrado no banco de dados!")
        return False

#FIM FUNCOES----


