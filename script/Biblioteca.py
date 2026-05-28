import os
livros = []
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
    novo_livro = input("Digite o nome do livro a ser cadastrado: ")
    livros.append(novo_livro)
    print(f"Livro '{novo_livro}' cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu...")
    chamar_menu()
  
def listar_livros():
    iniciar_app("Lista de livros cadastrados")
    input("Pressione Enter para voltar ao menu...")
    chamar_menu()
def editar_livro():
    iniciar_app("Edição de um livro cadastrado")
    input("Pressione Enter para voltar ao menu...")
    chamar_menu()
def sair():
    os.system('cls')
    iniciar_app("Saindo da aplicação...")
    
    
    
    


def main():
    chamar_menu()

if __name__ == "__main__":
    main()