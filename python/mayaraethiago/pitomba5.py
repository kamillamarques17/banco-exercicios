print ("-----Automação Industrial-----")

for tentativa in range(5):

    nome = input("Nome do operador: ").strip()
    turno = input("Turno de trabalho: ").strip()
    sigla = input("Sigla da turbina: ").strip()
    código = input("Código do gerador: ").strip()
    rotação = input("RPM").strip()
    nível = input("Nível da represa: ").strip()
    vazão = input("Vazão da água: ").strip()
    temperatura = input("Temperatura dos maciais: ").strip()
    sala = input("Sala de comando: ").strip()
    data = input("Data de leitura: ").strip()
    email = input("E-mail da usima: ").strip()
    alarme = input("Alarme geral: ").strip()

    if nome.isalpha() and turno.isalpha() and \
        sigla.isalnum() and código.isalnum() and \
        rotação.isdigit() and nível.isdigit() and \
        vazão.isdigit() and temperatura.isdigit() and \
        sala.isalpha() and len(data) == 10 and \
        email.count("@gmail.com") and alarme == "NORLMAL" :

        print("")
        break
else:
        print("")
        print("*-* 40 ")

