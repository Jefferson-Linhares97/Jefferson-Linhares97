import json

# Arquivo para armazenar os dados dos livros
ARQUIVO_LIVROS = "livros.json"

def carregar_livros():
    """Carrega os livros do arquivo JSON."""
    try:
        with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_livros(livros):
    """Salva os livros no arquivo JSON."""
    with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)

def cadastrar_livro():
    """Cadastra um novo livro na biblioteca."""
    livros = carregar_livros()

    nome = input("Nome do livro: ")
    autor = input("Autor: ")
    cod_livro = input("Código do livro: ")
    secao = input("Seção onde se encontra: ")

    livro = {
        "nome": nome,
        "autor": autor,
        "cod_livro": cod_livro,
        "secao": secao
    }

    livros.append(livro)
    salvar_livros(livros)

    print("Livro cadastrado com sucesso!\n")

def listar_livros():
    """Lista todos os livros cadastrados e mostra a quantidade disponível de cada código."""
    livros = carregar_livros()
    if not livros:
        print("Nenhum livro cadastrado.\n")
        return

    # Criar um dicionário para contar os exemplares por código
    contagem_livros = {}
    for livro in livros:
        cod_livro = livro["cod_livro"]
        if cod_livro in contagem_livros:
            contagem_livros[cod_livro]["quantidade"] += 1
        else:
            contagem_livros[cod_livro] = {
                "nome": livro["nome"],
                "autor": livro["autor"],
                "secao": livro["secao"],
                "quantidade": 1
            }

    # Exibir os livros agrupados por código
    for cod_livro, info in contagem_livros.items():
        print(f"Código: {cod_livro}, Nome: {info['nome']}, Autor: {info['autor']}, Seção: {info['secao']}, Quantidade: {info['quantidade']}")
    print("\n")

def excluir_livro():
    """Exclui um exemplar de um livro pelo Código do Livro."""
    livros = carregar_livros()
    if not livros:
        print("Nenhum livro cadastrado para excluir.\n")
        return

    cod_livro = input("Digite o código do livro a ser excluído: ")

    # Verifica se o código existe
    if not any(livro["cod_livro"] == cod_livro for livro in livros):
        print("Código do livro não encontrado.\n")
        return

    # Remove apenas um exemplar (o primeiro encontrado)
    for i, livro in enumerate(livros):
        if livro["cod_livro"] == cod_livro:
            del livros[i]
            break

    salvar_livros(livros)
    print("Um exemplar do livro foi excluído com sucesso!\n")

def menu():
    """Exibe o menu do sistema."""
    while True:
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Excluir um exemplar de um Livro")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            excluir_livro()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
