import json

# Arquivo para armazenar os dados dos alunos
ARQUIVO_ALUNOS = "alunos.json"

def carregar_alunos():
    """Carrega os alunos do arquivo JSON."""
    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_alunos(alunos):
    """Salva os alunos no arquivo JSON."""
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)

def cadastrar_aluno():
    """Cadastra um novo aluno, impedindo duplicação de ID de matrícula e CPF."""
    alunos = carregar_alunos()

    nome = input("Nome do aluno: ")

    # Verifica se o CPF já existe
    while True:
        cpf = input("CPF do aluno: ")
        if any(aluno["cpf"] == cpf for aluno in alunos):
            print("CPF já cadastrado. Digite um CPF diferente.")
        else:
            break

    turma = input("Turma do aluno: ")
    turno = input("Turno do aluno (Manhã/Tarde/Noite): ")

    # Verifica se o ID de matrícula já existe
    while True:
        id_matricula = input("ID da matrícula: ")
        if any(aluno["id_matricula"] == id_matricula for aluno in alunos):
            print("ID de matrícula já existe. Tente outro.")
        else:
            break

    aluno = {
        "nome": nome,
        "cpf": cpf,
        "turma": turma,
        "turno": turno,
        "id_matricula": id_matricula
    }

    alunos.append(aluno)
    salvar_alunos(alunos)

    print("Aluno cadastrado com sucesso!\n")

def listar_alunos():
    """Lista todos os alunos cadastrados."""
    alunos = carregar_alunos()
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, CPF: {aluno['cpf']}, Turma: {aluno['turma']}, Turno: {aluno['turno']}, ID Matrícula: {aluno['id_matricula']}")
    print("\n")

def excluir_aluno():
    """Exclui um aluno pelo ID de matrícula."""
    alunos = carregar_alunos()
    if not alunos:
        print("Nenhum aluno cadastrado para excluir.\n")
        return

    id_matricula = input("Digite o ID de matrícula do aluno a ser excluído: ")

    novos_alunos = [aluno for aluno in alunos if aluno["id_matricula"] != id_matricula]

    if len(novos_alunos) == len(alunos):
        print("ID de matrícula não encontrado.\n")
    else:
        salvar_alunos(novos_alunos)
        print("Aluno excluído com sucesso!\n")

def menu():
    """Exibe o menu do sistema."""
    while True:
        print("1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("3 - Excluir Aluno")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            excluir_aluno()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
