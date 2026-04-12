def adicionar_medicamento(nome, horario, lista):
    """Regra de negócio para adicionar medicamento."""
    if not nome or not horario:
        return False, "Erro: Nome e horário são obrigatórios."
    
    lista.append({"nome": nome, "horario": horario})
    return True, "Medicamento adicionado com sucesso!"

def listar_medicamentos(lista):
    """Regra de negócio para listar medicamentos."""
    if not lista:
        return "Nenhum medicamento cadastrado."
    
    resultado = "--- Lista de Medicamentos ---\n"
    for med in lista:
        resultado += f"⏰ {med['horario']} - 💊 {med['nome']}\n"
    return resultado

def menu():
    """Interface de Linha de Comando (CLI)."""
    medicamentos = []
    while True:
        print("\n=== CONTROLE PARA CUIDADORES ===")
        print("1. Adicionar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Qual o nome do remédio? ")
            horario = input("Qual o horário? (Ex: 08:00): ")
            sucesso, msg = adicionar_medicamento(nome, horario, medicamentos)
            print(msg)
        elif opcao == '2':
            print(listar_medicamentos(medicamentos))
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()