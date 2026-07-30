import contatos
from constantes import CATEGORIAS_VALIDAS

def exibir_menu():

    print("\n   AGENDA DE CONTATOS ")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")

def rodar():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            print(f"Categorias disponíveis: {CATEGORIAS_VALIDAS}")
            categoria = input("Categoria: ")
           
            contatos.cadastrar_contato(nome, telefone, email, categoria)

        elif opcao == "2":
            contatos.listar_contatos()

        elif opcao == "3":
            termo = input("Digite o nome (ou parte dele) para buscar: ")
            contatos.buscar_contato(termo)

        elif opcao == "4":
            nome = input("Nome do contato a remover: ")
            contatos.remover_contato(nome)

        elif opcao == "5":
            print("Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")