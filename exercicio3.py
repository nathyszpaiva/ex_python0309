produtos = {}
def cadastro_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome: ")
    preço = float(input("Digite o preço: "))
    estoque = float(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {'nome': nome, 'preço': preço, 'estoque': estoque}
    print("Produto cadastrado com sucesso!")
 
def altera_preço():
    novo_preço = float(input("Digite o novo preço: "))
    codigo = input("Entre com o código do produto: ")
    if(codigo in produtos):
        produtos[codigo]['preço'] = novo_preço
        print("Preço alterado com sucesso!")
       
def pesquisa_produto():
    codigop = input("Digite o código do produto: ")
    produtoencontrado = produtos.get(codigop)
    if produtoencontrado:
        print("Produto encontrado")
        print(produtoencontrado)
 
while(True):
    print("\nMenu: ")
    print("1 - Adicionar produto")
    print("2 - Alterar preço produto")
    print("3 - Pesquisar por código")
    print("4 - Sair")
    print("---------------------------")
    opcao = int(input("Escolha uma opção:"))
 
    if(opcao == 1):
        cadastro_produto()
    elif(opcao == 2):
        altera_preço()
    elif(opcao == 3):
        pesquisa_produto()
    elif(opcao == 4):
        break
    else:
        print("Escolha a opção correta")
