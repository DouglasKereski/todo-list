def adicionar_tarefa(tarefas, descricao):
    """
    Adiciona uma nova tarefa à lista com prioridade.
    """
    if descricao:
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ").capitalize()
        if prioridade not in ["Alta", "Média", "Baixa"]:
            print("⚠️ Prioridade inválida. Definida como 'Baixa' por padrão.")
            prioridade = "Baixa"
        nova_tarefa = {
            "descricao": descricao,
            "concluida": False,
            "prioridade": prioridade
        }
        tarefas.append(nova_tarefa)
        print(f"\n✅ Tarefa '{descricao}' adicionada com prioridade {prioridade}!")
    else:
        print("\n❌ A descrição da tarefa não pode ser vazia.")

def listar_tarefas(tarefas):
    """
    Lista todas as tarefas com status e prioridade.
    """
    print("\n--- Sua Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa na lista. Adicione uma!")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "✅" if tarefa["concluida"] else "◻️"
            prioridade = tarefa.get("prioridade", "Baixa")
            print(f"{i + 1}. {status} [{prioridade}] {tarefa['descricao']}")
    print("--------------------------")

def marcar_como_concluida(tarefas, indice):
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        if tarefas[indice_real]["concluida"]:
            print(f"\n⚠️ A tarefa '{tarefas[indice_real]['descricao']}' já estava concluída.")
        else:
            tarefas[indice_real]["concluida"] = True
            print(f"\n✅ Tarefa '{tarefas[indice_real]['descricao']}' marcada como concluída!")
    else:
        print("\n❌ Índice inválido.")

def remover_tarefa(tarefas, indice):
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        tarefa_removida = tarefas.pop(indice_real)
        print(f"\n🗑️ Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    else:
        print("\n❌ Índice inválido.")

def editar_descricao(tarefas, indice):
    """
    Permite editar a descrição de uma tarefa existente.
    """
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        print(f"\n✏️ Descrição atual: {tarefas[indice_real]['descricao']}")
        nova_descricao = input("Digite a nova descrição: ")
        if nova_descricao.strip():
            tarefas[indice_real]["descricao"] = nova_descricao.strip()
            print("✅ Descrição atualizada com sucesso!")
        else:
            print("❌ A nova descrição não pode ser vazia.")
    else:
        print("❌ Índice inválido.")

def exibir_menu():
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Editar Descrição de Tarefa")  # Nova opção
    print("0. Sair")

def main():
    lista_de_tarefas = []

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Número da tarefa a marcar como concluída: "))
                marcar_como_concluida(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida.")
        elif escolha == '4':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Número da tarefa para remover: "))
                remover_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida.")
        elif escolha == '5':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Número da tarefa para editar a descrição: "))
                editar_descricao(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida.")
        elif escolha == '0':
            print("\n👋 Obrigado por usar o Gerenciador de Tarefas!")
            break
        else:
            print("\n❌ Opção inválida.")

if __name__ == "__main__":
    main()

