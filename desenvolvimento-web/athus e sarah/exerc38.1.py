print('-----Registro de Ponto Eletrônico-----')
for tentativa in range(3):
    func = input("Nome do funcionário: ")
    unidade = input("Unidade: ")
    id_cracha = input("ID do crachá: ")
    cargo = input("Cargo: ")
    hora_entrada = input("")
    cod_verif = input("Código de verificação: ")
    if func > 3 and unidade == "SUL" and \
    id_cracha == 5 and id_cracha.isdigit() and \
    cargo.isalpha() and hora_entrada == 4 and hora_entrada.isdigit() and \
    cod_verif != "123":
      print("Registrado com sucesso!")
      break
    else:
      print("ERRO.")
      print("-" *21)
else:
       print("SISTEMA BLOQUEADO.")