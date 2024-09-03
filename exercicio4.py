# Faça uma aplicação Python que:
#  1 - Armazene dados de alunos (nome, data_nasc, email, fone, endereco)
#  2 - Liste um aluno pesquisado
#  3 - Liste todos os alunos
#  4 - Alterar o endereço do aluno pesquisado

# Dicionário para armazenar os dados dos alunos
alunos = {}

# Função para cadastrar um aluno
def cadastro_aluno():
    matricula = input("Digite o número da matrícula: ")
    nome = input("Digite o nome: ")
    data_nasc = input("Digite a data de nascimento (dd/mm/yyyy): ")
    email = input("Digite o e-mail: ")
    fone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")
    alunos[matricula] = {
        'nome': nome, 
        'data_nasc': data_nasc, 
        'email': email, 
        'fone': fone, 
        'endereco': endereco
    }
    print("Aluno cadastrado com sucesso!")

# Função para alterar o endereço de um aluno
def altera_endereco():
    matricula = input("Digite o número da matrícula do aluno: ")
    if matricula in alunos:
        novo_endereco = input("Digite o novo endereço: ")
        alunos[matricula]['endereco'] = novo_endereco
        print("Endereço alterado com sucesso!")
    else:
        print("Aluno não encontrado.")

# Função para pesquisar um aluno por matrícula
def pesquisa_aluno():
    matricula = input("Digite o número da matrícula do aluno: ")
    aluno_encontrado = alunos.get(matricula)
    if aluno_encontrado:
        print("Aluno encontrado:")
        print(aluno_encontrado)
    else:
        print("Aluno não encontrado.")

# Função para listar todos os alunos
def listar_alunos():
    if alunos:
        print("Lista de todos os alunos:")
        for matricula, dados in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Endereço: {dados['endereco']}")
    else:
        print("Nenhum aluno cadastrado.")

# Menu principal
while True:
    print("\nMenu: ")
    print("1 - Adicionar aluno")
    print("2 - Alterar endereço de aluno")
    print("3 - Pesquisar por matrícula")
    print("4 - Listar todos os alunos")
    print("5 - Sair")
    print("---------------------------")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastro_aluno()
    elif opcao == 2:
        altera_endereco()
    elif opcao == 3:
        pesquisa_aluno()
    elif opcao == 4:
        listar_alunos()
    elif opcao == 5:
        break
    else:
        print("Escolha a opção correta.")
