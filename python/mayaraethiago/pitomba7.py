print("-----Sistema de Defesa Cibernética e Monitoramento de SOC-----")

for tentativa in range(5):
    nome = input("Nome do Analista: ").strip()
    equipe = input("Equipe de Resposta: ").strip()
    incidente = input("Código do Incidente: ").strip()
    iporigem = input("IP de Origem: ").strip()
    ipdestino = input("IP de Destino: ").strip()
    porta = input("Porta do Protocolo: ").strip()
    ameaca = input("Tipo de Ameaça: ").strip()
    severidade = input("Severidade Numérica: ").strip()
    patch = input("Código do Patch: ").strip()
    data = input("Data do Alerta (DD/MM/AAAA): ").strip()
    email = input("E-mail do SOC: ").strip().lower()
    resposta = input("Resposta ao Incidente: ").strip().upper()

    if nome.isalpha() and equipe.isalpha() and ameaca.isalpha() and \
       incidente.isalnum() and patch.isalnum() and \
       iporigem.isalnum() and ipdestino.isalnum() and \
       porta.isdigit() and severidade.isdigit() and \
       len(incidente) == 8 and len(data) == 10 and \
       email.endswith(".soc.sec") and \
       "@" in email and \
       resposta == "MITIGADO":

        print(f"\nSUCESSO: incidente {incidente} registrado.")
        break

    else:
        print(f"\nERRO: cadastro inválido, Tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
