print("----------Ponto dos funcionários----------")
for tentativa in range(3):
    funcionário = input("Nome do funcionário: ").strip()
    unidade = input("Unidade: ").strip()
    id = input("id do chacrás: ").strip()
    cargo = input("Cargo: ").strip()
    hora_entrada = input("Digite a hora de entrada: ").strip()
    cod_verificação = input("cod_verificação: ").strip()

    if funcionário.isalpha() > 3 and unidade == "SUL" and id > 5 and cargo.isalpha and hora_entrada.isdigit> 4 and cod_verificação != "123":
       print("Registro concluído!")
       break
    else:
        print("Erro fatal.")
else:
    print("Tentativas bloqueadas.")
    print("-"*30)
    