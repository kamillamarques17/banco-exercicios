print("-----------RH----------------")
for tentativa in range(3):
    funcionário = input("funcionário: ").strip()
    unidade = input("unidade: ").strip()
    id = input("id (5 números): ").strip()
    cargo = input("cargo: ").strip()
    entrada = input("entrada (4 números): ").strip()
    código = input("código: ").strip()

    if funcionário.isalpha() > 3 and  unidade.isalpha() == "SUL" and \
       len(id) == 5 and id.isdigit() and \
       cargo.isalpha > 3 and entrada.isdigit() == 4 and \
       código != "123":

       print("Registro feito.")
       break 
    else: 
       print("Erro no registro.")
       print("-" * 30)
else:
  print("tentativas feitas ")
