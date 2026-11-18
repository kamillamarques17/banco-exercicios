print ("----sistema de auditoria completo ----")

for tentativa in range (3) :
    maquina = input("digite o nome da maquina:")
    codigo = input("digite sua serie:")
    operador = input("digite seu nome de operador:")
    turno = input ("digite o seu turno de trabalho:")
    peca_dia = input ("digite o numero de peças:")
    defeitos = input("digite o numero de defeitos:")
    email_T = input ("digite seu Email_T")
    fabrica = input ("qual e o nome da fabrica :")
    setor = input ("digite seu setor:")
    corredor = input ("digite seu crredor :")
    gaveta = input ("digite o numero da sua gaveta:")
    fornecedor = input ("digite seu fornecedor:")
    CNPJ_F = input ("digite seub cnpj (14num):")
    data_manut = input("data (aa/mm/aaaa):")
    status = input ("status deve ser operacional:")

    if setor.isalpha() and \
       fornecedor.isalpha() and \
       peca_dia.isdigit() and \
       defeitos.isdigit() and \
       gaveta.isdigit() and \
       CNPJ_F.isdigit() and \
       serie.isalnum() and \
       email_T.count("@") == 1 and email_T.endswith(".com") and \
       data_manut.count("//") == 2 and \
       status == "operacional":

        print (f"\nSUCESSO status {status}, seu {CNPJ_F} foi enviado!")
        break

    else:
        print(*f"\n")