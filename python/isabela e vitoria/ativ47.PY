print("---- CADASTRO DE AGENTE DA INTERPOL ----")

for tentativa in range(3):

    agente = input("Agente: ").strip()
    codinome = input("Codinome: ").strip()
    pais = input("País: ").strip()
    id_agente = input("ID: ").strip()
    nivel = input("Nível: ").strip().upper()
    cargo = input("Cargo: ").strip()
    especialidade = input("Especialidade: ").strip()
    senha = input("Senha: ").strip()
    pin = input("PIN: ").strip()
    unidade = input("Unidade: ").strip().upper()
    superior = input("Superior: ").strip()
    missao = input("Missão: ").strip()
    arma = input("Arma: ").strip()
    veiculo = input("Veículo: ").strip()
    status = input("Status: ").strip().upper()

    if (agente.isalpha() and
        codinome.isalpha() and
        id_agente.isdigit() and len(id_agente) == 7 and
        pin.isdigit() and len(pin) == 4 and
        unidade == "INTERPOL" and
        status != "INATIVO" and
        nivel == "TOP_SECRET"):


        print("Agente cadastrado com sucesso.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO.")