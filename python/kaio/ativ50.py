print("---Aeronave executiva---")

for tentativa in range(3): 

    modelo = input("Digite o modelo:").strip().upper()
    prefixo = input("Digite o prefixo:").strip()
    fabricante = input("Digite o seu fabricante:").strip()
    ano = input("Digite o Ano :").strip()
    horas = input("Digite o horario:").strip()
    piloto = input("Digite o nome do piloto :").strip()
    cpf = input("Digite o seu cpf (11 num):").strip()
    email = input("Digite seu email").strip()
    base = input("Digite a base:").strip()
    cidade = input("Digite a cidade :").strip()
    uf = input("Digite o UF (2 carac):").strip().upper()
    carga = input("Digite a carga:").strip()
    tanque = input("Digite o tanque :").strip()
    torre = input("Digite a torre:").strip().upper()
    termos = input("Digite os termos:").strip().upper()

    if modelo.isalpha() and modelo.isalpha() and \
       prefixo.isalnum() and \
       fabricante.isalpha() and \
       piloto.isalpha() and \
       ano.isdigit() and \
       horas.isdigit() and \
       piloto.isalpha() and \
       cpf.isdigit() and \
       base.isalpha() and \
       cidade.isalpha and \
       uf.isalpha() and \
       carga.isdigit() and \
       tanque.isdigit() and \
       torre.isdigit() and \
       len(termos) and termos.isalpha() == "SIM" and \
       email.count("@") == 1 and email.endswith(".com"):

        print(f"Acesso liberado! Bem-vindo ao sistema, {modelo}.")
        break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")