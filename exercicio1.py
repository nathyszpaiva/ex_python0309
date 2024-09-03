#produtos = {}

#codigo = input("Digite o código do produto: ")
#nome = input("Digite o nome do produto: ")
#preco = float(input("Digite o preço de venda: "))
#quantidade = int(input("Digite a quantidade em estoque: "))
#produtos[codigo] = {"nome":nome, "preco":preco, "quantidade":quantidade}
#print("Produto adicionado com sucesso!")
#print(produtos)

produtos = {}

while True:
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço de venda: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
    print("Produto adicionado com sucesso!")
    print(produtos)
    
    while True:
        continuar = input("Gostaria de fazer mais cadastros? [Sim/Não]: ").strip().lower()
        
        if continuar == 'não':
            print("Cadastros realizados!")
            print(produtos)
            exit()  # Sai do programa
        elif continuar == 'sim':
            break  # Sai do loop interno e volta ao loop principal
        else:
            print("Resposta inválida. Digite 'Sim' ou 'Não'.")