print("---- MANIFESTO DE CARGA ----")

for tentativa in range(3):

    navio = input("Navio: ").strip()
    capitao = input("Capitão: ").strip()
    origem = input("Origem: ").strip()
    destino = input("Destino: ").strip().upper()
    carga = input("Carga: ").strip()
    peso = input("Peso: ").strip()
    containers = input("Containers: ").strip()
    valor = input("Valor: ").strip()
    seguro = input("Seguro: ").strip()
    porto = input("Porto: ").strip()
    empresa = input("Empresa: ").strip().upper()
    licenca = input("Licença: ").strip()
    rota = input("Rota: ").strip().upper()
    combustivel = input("Combustível: ").strip()
    chegada = input("Chegada: ").strip()

    if (capitao.isalpha() and
        origem.isalpha() and
        licenca.isdigit() and len(licenca) == 8 and
        peso.isdigit() and
        destino == "EUROPA" and
        empresa != "FANTASMA" and
        rota == "SUL"):

        print("Manifesto aprovado.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO.")


