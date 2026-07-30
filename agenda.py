#TUPLA
CATEGORIAS_VALIDAS =("PESSOAL","TRABALHO", "FAMILIA")
#LISTA 
agenda = []

def cadastrar_contato(nome, telefone,email,categoria):
    if categoria not in CATEGORIAS_VALIDAS:
        print(f"categoria Inválida! Use uma dessas: {CATEGORIAS_VALIDAS}")
        return False

    contato = {
        "nome" : nome,
        "telefone" : telefone,
        "email" : email,
        "categoria" : categoria
    }

    agenda.append(contato)

    print(f"Contato {nome} cadastrado com sucesso!")
    return True

def listar_contatos():
    if not agenda:
        print("Nenhum contato cadastrado.")
        return 
    print(f"\n --- {len(agenda)} contatos cadastrado(s) ---")

    for indice,contato in enumerate(agenda, start= 1):
        print(f"\nContato {indice}:")
        for chave,valor in contato.items():
            print(f" {chave} : {valor}")

def buscar_contato(termo_busca):

    resultados = []

    for contato in agenda:
        if termo_busca.lower() in contato["nome"].lower():
            resultados.append(contato)


    if not resultados:
        print(f"Nenhum contato encontrado com o termo '{termo_busca}'.")

    else:
        print(f"\n --- {len(resultados)} resultado(s) para {termo_busca} ---")
        for contato in resultados:
            print(f" {contato['nome']} - {contato['telefone']} - {contato['email']} - {contato['categoria']}")
    return resultados

def remover_contato(nome):
    
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)  # remove esse item específico da lista
            print(f"Contato '{nome}' removido com sucesso!")
            return True
 
    print(f"Contato '{nome}' não encontrado.")
    return False

def exibir_menu():

    print("\n   AGENDA DE CONTATOS ")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")

def main():
   
    while True:  # loop infinito - só sai quando escolhermos "5" (break)
        exibir_menu()
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            print(f"Categorias disponíveis: {CATEGORIAS_VALIDAS}")
            categoria = input("Categoria: ")
            cadastrar_contato(nome, telefone, email, categoria)
 
        elif opcao == "2":
            listar_contatos()
 
        elif opcao == "3":
            termo = input("Digite o nome (ou parte dele) para buscar: ")
            buscar_contato(termo)
 
        elif opcao == "4":
            nome = input("Nome do contato a remover: ")
            remover_contato(nome)
 
        elif opcao == "5":
            print("Até mais!")
            break 
 
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
