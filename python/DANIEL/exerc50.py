print("--aeronave executiva --")

for tentativa in range(3):
    modelo = input("digite o modelo:").strip().upper()
    prefixo = input("digite o prefixo:").strip()
    fabricante = input("digite seu fabricante:").strip()
    ano = input("digite o ano:").strip()
    horas = input("digite o seu horario:").strip()
    piloto = input("digite o nome do piloto: ").strip()
    CPF = input("digite seu cpf (11num):").strip()
    email = input("digite seu email:").strip()
    Base = input("digite sua base:").strip()
    cidade = input("digite a cidade:").strip()
    uf = input("digite o uf:").strip()
    carga = input("digite a sua carga: ").strip()
    tanque = input("digite o tanque: ").strip()
    torre = input("digite a torre:").strip().upper()
    termos = input("digite os termos:").strip().upper()

    if modelo.isalpha() and \
        prefixo.isalpha() and \
        fabricante.isalpha() and \
        piloto.isalpha() and \
        ano.isdigit() and \
        horas.isdigit() and \
        CPF.isdigit() and \
        Base.isalpha() and \
        cidade.isalpha() and \
        uf.isalpha() and \
        carga.isdigit() and \
        tanque.isdigit() and \
        torre.isalpha() and \
        termos == "SIM" and \
        email.count("@") == 1 and \
        email.endswith(".com"):

        print(f"acesso liberado! bem vindo ao sistema, {modelo}")
        break

    else:
        print("SISTEMA BLOQUEADO. ALERTA DE INTRUSÃO ENVIADO À SEGURANÇA.")