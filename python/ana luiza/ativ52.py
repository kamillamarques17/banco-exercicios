print("-------REGISTRO DE SOFTWARE EM NUVEM-------")
for tentativa in range (3):
    app=input("qual o app?") .strip()
    versão = input("Qual a versão?").strip()
    linguagem = input("Qual a linguagem?")
    servidor = input ("Qual o servidor?:")
    IP = input ("Digite o IP:")
    porta = input ("Informe a porta:")
    desenvolvedor = input ("Informe o desenvolvedor:")
    CPF = input("Informe o CPF:")
    email = input("Informe o email:")
    empresa = input("Informe a empresa:")
    CNPJ = input("Informe o CNPJ:")
    país = input("Qual o país?")
    licença = input("Lincença:")
    data = input("Data: (DD/MM/AAAA)")
    status = input("Qual o status?:")

    if linguagem.isalpha() and país.isalpha() and \
    porta.isdigit() and CPF.isdigit() and licença.isdigit() and\
    app.upper() and servidor.upper() and empresa.upper() and status.upper() and\
    versão.isalnum() and email.endswith(".com") and data.count("/") == 2 and\
    status == "ATIVO:":

     print(f"SUCESSO: Registrado!")
     break
    else:
     print(f"ERRO: Dados inválidos! Tentativa {tentativa + 1} de 3.")
     print("-"*40)

else:
    print("BLOQUEADO: Muitas falhas.")