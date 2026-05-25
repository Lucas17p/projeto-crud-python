# CRUD de Produtos com Python e SQLite

Sistema CRUD desenvolvido em Python utilizando SQLite para persistência de dados.

O projeto permite:

- Cadastrar produtos
- Listar produtos
- Atualizar produtos
- Excluir produtos

Os dados ficam salvos localmente em um banco SQLite (`estoque.db`), permitindo que as informações permaneçam mesmo após fechar o programa.

---

# Tecnologias utilizadas

- Python
- SQLite3

---

# Estrutura do projeto

```text
Projeto/
│
├── main.py
├── database.py
├── estoque.db
├── .gitignore
│
└── models/
    ├── menu.py
    └── produtosSistema.py
```

---

# Funcionamento dos arquivos

## `main.py`

Arquivo principal do sistema.

Responsável por iniciar o menu da aplicação.

Também importa o `database.py` para garantir que o banco e a tabela existam antes da execução.

---

## `database.py`

Responsável pela criação do banco SQLite e da tabela `produtos`.

```python
CREATE TABLE IF NOT EXISTS produtos
```

O `IF NOT EXISTS` evita erros caso a tabela já exista.

---

## `menu.py`

Responsável pela interface no terminal.

Contém:
- Menu interativo
- Validação de entradas
- Tratamento de erros
- Navegação entre funcionalidades

Exemplo de tratamento de erro:

```python
try:
    opcao = int(input("Digite a opção: "))
except ValueError:
    print("Digite apenas números.")
```

Isso evita que o programa quebre caso o usuário digite letras.

---

## `produtosSistema.py`

Responsável pelas operações CRUD no banco de dados.

### CREATE

Adiciona produtos ao banco.

```python
INSERT INTO produtos(produto, valor)
VALUES (?, ?)
```

O uso de `?` é importante para segurança.

Ele evita ataques de SQL Injection ao separar os dados do usuário do comando SQL.

---

### READ

Lista todos os produtos cadastrados.

```python
SELECT * FROM produtos
```

---

### UPDATE

Atualiza um produto existente utilizando o ID.

```python
UPDATE produtos
SET produto = ?, valor = ?
WHERE id = ?
```

O sistema verifica se algum registro foi alterado usando:

```python
cursor.rowcount
```

Isso evita informar sucesso quando o ID não existe.

---

### DELETE

Remove um produto pelo ID.

```python
DELETE FROM produtos
WHERE id = ?
```

Também utiliza `rowcount` para validar se o produto realmente existia.

---

# Persistência de dados

O projeto utiliza SQLite.

Isso significa que os dados ficam armazenados no arquivo:

```text
estoque.db
```

Mesmo fechando o programa, os produtos permanecem salvos.

---

# Segurança

O projeto utiliza parâmetros SQL com `?`.

Exemplo:

```python
cursor.execute(
    "SELECT * FROM produtos WHERE id = ?",
    (id_produto,)
)
```

Isso ajuda a evitar SQL Injection.

---

# Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd nome-do-projeto
```

Execute:

```bash
python main.py
```

---

# Melhorias futuras

- Interface gráfica
- Front-end web
- Sistema de login
- Busca de produtos
- Paginação
- API REST
- Integração com frameworks como Flask ou Django

---

# Autor
Desenvolvido por Lucas Pinheiro
www.linkedin.com/in/lucas-pinheiro-62a373409



Projeto desenvolvido para fins de estudo e prática de Python, SQLite e operações CRUD.