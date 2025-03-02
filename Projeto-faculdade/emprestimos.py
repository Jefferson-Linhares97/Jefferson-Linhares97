import json

# Arquivo para armazenar os empréstimos
ARQUIVO_EMPRESTIMOS = "emprestimos.json"

def carregar_emprestimos():
    """Carrega os empréstimos do arquivo JSON."""
    try:
        with open(ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_emprestimos(emprestimos):
    """Salva os empréstimos no arquivo JSON."""
    with open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
        json.dump(emprestimos, f, indent=4, ensure_ascii=False)

def registrar_emprestimo():
    """Registra um novo empréstimo de livros para um aluno."""
    emprestimos = carregar_emprestimos()

    print("\n📚 REGISTRAR EMPRÉSTIMO\n")
    
    aluno = {
        "nome": input("Nome do aluno: ").strip(),
        "turma": input("Turma: ").strip(),
        "turno": input("Turno: ").strip(),
        "id_matricula": input("ID de matrícula: ").strip()
    }

    livros = []
    
    while True:
        livro = {
            "nome_livro": input("Nome do livro: ").strip(),
            "autor": input("Autor: ").strip(),
            "cod_livro": input("Código do livro: ").strip()
        }
        livros.append(livro)

        mais_livros = input("O aluno deseja pegar outro livro? (s/n): ").strip().lower()
        if mais_livros != 's':
            break

    emprestimo = {
        "aluno": aluno,
        "livros": livros
    }

    emprestimos.append(emprestimo)
    salvar_emprestimos(emprestimos)

    print("\n✅ Empréstimo registrado com sucesso!\n")

def listar_emprestimos():
    """Lista todos os empréstimos ativos."""
    emprestimos = carregar_emprestimos()
    if not emprestimos:
        print("\n📌 Nenhum empréstimo ativo.\n")
        return

    print("\n📋 LISTA DE EMPRÉSTIMOS\n")
    for e in emprestimos:
        print(f"🎓 Aluno: {e['aluno']['nome']} (Matrícula: {e['aluno']['id_matricula']})")
        
        livros = e.get("livros", [])
        
        if not livros:
            print("⚠️ Nenhum livro registrado para este empréstimo.")
        else:
            print("📖 Livros emprestados:")
            for livro in livros:
                print(f"   - {livro['nome_livro']} (Código: {livro['cod_livro']})")
        
        print("-" * 40)
    print("\n")

def devolver_livro():
    """Registra a devolução de um livro pelo Código do Livro."""
    emprestimos = carregar_emprestimos()
    if not emprestimos:
        print("\n📌 Nenhum empréstimo ativo para devolução.\n")
        return

    cod_livro = input("Digite o código do livro a ser devolvido: ").strip()

    for emprestimo in emprestimos:
        livros = emprestimo.get("livros", [])

        for livro in livros:
            if livro["cod_livro"] == cod_livro:
                livros.remove(livro)

                if not livros:
                    emprestimos.remove(emprestimo)

                salvar_emprestimos(emprestimos)
                print("\n✅ Livro devolvido com sucesso!\n")
                return

    print("\n⚠️ Código do livro não encontrado nos empréstimos.\n")

def menu():
    """Exibe o menu do sistema."""
    while True:
        print("\n📚 Sistema de Empréstimo de Livros")
        print("1 - Registrar Empréstimo")
        print("2 - Listar Empréstimos")
        print("3 - Devolver Livro")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_emprestimo()
        elif opcao == "2":
            listar_emprestimos()
        elif opcao == "3":
            devolver_livro()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
