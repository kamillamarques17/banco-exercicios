print("-------------Registro de Aeronave Executiva--------")
modelo = input("Modelo: ")
piloto = input("Piloto: ")
fabricante = input("Fabricante: ")
ano = input("Ano: ")
horas = input("Horas: ")
pista = input("Pista: ")
cpf = input("CPF: ")
email = input("E-mail: ")
base = input("Base: ")
cidade = input("Cidade: ")
uf = input("UF: ")
carga = input("Carga: ")
tanque = input("Tanque: ")
torno = input("Torno: ")
termos = input("Termos: ")

if (fabricante.isalpha() and
    piloto.isalpha() and
    ano.isdigit() and
    horas.isdigit() and
    cpf.isdigit() and len(cpf) == 11 and
    carga.isdigit() and
    tanque.isdigit() and
    modelo.isupper() and
    base.isupper() and
    uf.isupper() and len(uf) == 2 and
    torno.isupper() and
    pista.isalnum() and
    torno.isalnum() and
    "@" in email and email.endswith(".com") and
    termos == "SIM"):

    print("Cadastro válido!")
else:
    print("Cadastro inválido!")