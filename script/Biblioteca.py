import os
livros = {}
input_opcao = 0

def iniciar_app(texto):
    os.system('cls')
    print("================================")
    print(texto)
    print("================================")
def chamar_menu():
    os.system('cls')

    print("================================")
    print("Bem-vindo à Biblioteca!")
    print("================================")
    print("Escolha uma opção:\n")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Editar livro")
    print("0 - Sair")

    input_opcao = input("Digite a opção desejada: ")
    if input_opcao.isdigit():
        opcoes = int(input_opcao)
        if opcoes == 1:
            cadastrar_livro()
        elif opcoes == 2:
            listar_livros()
        elif opcoes == 3:
            editar_livro()
        elif opcoes == 0:
            print("Saindo da aplicação...")
            sair()
        else:
            print("Opção inválida. Tente novamente.")
            chamar_menu()
    else:
        print("Entrada inválida. Por favor, digite um número.")
        chamar_menu()

def cadastrar_livro():

    iniciar_app("Cadastro de um novo livro")
    nome_livro = input("Digite o nome do livro a ser cadastrado: ")
    autor_livro = input("Digite o nome do autor do livro: ")
    novo_livro = {"livro": nome_livro, "autor": autor_livro, "status": False}

    livros[nome_livro] = novo_livro

    print(f"Livro '{nome_livro}' cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu...")
    chamar_menu() 
def listar_livros():
    iniciar_app("Lista de livros cadastrados")
    if livros:
        for livro in livros.values():
         print(f"\nLivro: {livro['livro'].ljust(20)} | Autor: {livro['autor'].ljust(15)} | Status: {'Lido' if livro['status'] else 'Não lido'}\n")
    else:
        print(" Nenhum livro cadastrado.")
    input("\nPressione Enter para voltar ao menu...")
    chamar_menu()
def editar_livro():
    iniciar_app("Edição de um livro cadastrado")
    nome_livro = input("Digite o nome do livro que deseja editar: ")
    if nome_livro in livros:
        livro = livros[nome_livro]
        print(f"\nLivro: {livro['livro']} | Autor: {livro['autor']} | Status: {'Lido' if livro['status'] else 'Não lido'}\n")
        print("Escolha o que deseja editar:")
        print("1 - Editar nome do livro")
        print("2 - Editar nome do autor")
        print("3 - Marcar como lido/não lido")
        print("0 - Voltar ao menu")

        input_opcao = input("Digite a opção desejada: ")
        if input_opcao.isdigit():
            opcoes = int(input_opcao)
            if opcoes == 1:
                novo_nome = input("Digite o novo nome do livro: ")
                livro['livro'] = novo_nome
                livros[novo_nome] = livros.pop(nome_livro)  
                print(f"Nome do livro atualizado para '{novo_nome}' com sucesso!")
            elif opcoes == 2:
                novo_autor = input("Digite o novo nome do autor: ")
                livro['autor'] = novo_autor
                print(f"Nome do autor atualizado para '{novo_autor}' com sucesso!")
            elif opcoes == 3:
                livro['status'] = not livro['status']
                status_atualizado = 'Lido' if livro['status'] else 'Não lido'
                print(f"Status do livro atualizado para '{status_atualizado}' com sucesso!")
            elif opcoes == 0:
                chamar_menu()
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Entrada inválida. Por favor, digite um número.")
    input("\nPressione Enter para voltar ao menu...")
    chamar_menu()
def sair():
    os.system('cls')
    iniciar_app("Saindo da aplicação...")
    

def main():
    chamar_menu()

if __name__ == "__main__":
    main()