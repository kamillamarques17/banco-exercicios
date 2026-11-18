print("----- DESAFIO INTEGRADOR: GERENCIADOR DE TRAFEGO AEREO -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    prefixo_aeronave = input("qual o prefixo da aeronave: ").strip()
    companhia = input("Nome da companhia: ").strip()
    codigo= input("codigo: ").strip()
    altitude = input("altitude: ").strip()
    velocidade = input("velocidade: ").strip()
    pista = input("pista: ").strip()
    aeroporto= input("qual o aeroporto de destino: ").strip()
    codigo = input("qual a conta: ").strip()
    email = input("email: ").strip()
    status = input("Confirmar status (digite PERMITIDO): ").strip().upper()

    # Validação direta com IF + AND
    if prefixo_aeronave.isalnum() and \
       codigo.isalnum() and \
       pista.isalnum() and \
       companhia.isalpha() and \
       aeroporto.isalpha() and \
       altitude.isdigit and \
       velocidade.isdigit and \
       codigo.isdigit and \
       len(codigo) == 6 and \
        email.endswith("@AIRCONTROL.COM") and \
               status == "PERMITIDO":
       print(
            f"\nSUCESSO: cliente, "
            f"tudo certo"
        )
       break
    else:
        # Exibe a tentativa amigável (1 a 5)
        print(f"\nERRO: dados inválidos, tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
 print(
        "\nBLOQUEADO: limite de 5 tentativas excedido. "
        "Procure o suporte da corretora."
    )

   