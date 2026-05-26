import os
livros = []
input_opcao = 0

def iniciar_app():
    print("Bem vindo a sua biblioteca pessoal!")
def chamar_menu():
    print("================================")
    print("Escolha uma opção:")
    print("================================")
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
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            chamar_menu()
    else:
        print("Entrada inválida. Por favor, digite um número.")
        chamar_menu()

def cadastrar_livro():
    print("Cadastro de um novo livro:")
def listar_livros():
    print("Lista de livros cadastrados:")
def editar_livro():
    print("Editar um livro cadastrado:")
def sair():
    print("Saindo da aplicação...")
    


def main():
    iniciar_app()
    chamar_menu()

if __name__ == "__main__":
    main()