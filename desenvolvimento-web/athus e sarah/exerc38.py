print('-----Ponto dos Funcionários-----')
for tentativa in range(3):
    funcionário = input("Nome do funcionário: ").strip()
    unidade = input("Unidade: ")
    id = input ("ID do crachá: ").strip()
    cargo = input ("Cargo: ").strip()
    hora_entrada = input ("Digite a hora de entrada: ").strip()
    cord_verificação = input("Código de verificação: ").strip()
    if funcionário.isalpha() > 3 and unidade == "SUL" and id > 5 and cargo.isalpha and hora_entrada.isdigit > 4 and cord_verificação != "123":
      print("Registro concluído")
      break
    else:
      print("Erro fatal.")
      print("-" *30)
else:
       print("Tentativas bloqueadas")   