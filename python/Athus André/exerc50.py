print('-----Registro de Aeronave Executiva-----')
modelo = input("Digite o modelo: ").strip()
prefixo = input("qual o prefixo? ").strip()
fabricante = ("Qual o fabricante? ").strip()
ano = input("Digite o ano: ").strip()
horas = input("Digite a QTDE. de horas: ").strip()
piloto = input("Qual o piloto? ").strip()
cpf = input("Digite o CPF: ").strip()
email = ("Digite o e-mail: ").strip()
base = input("Qual a base? ").strip()
cidade = input("Qual a cidade? ").strip()
uf = input("UF: ").strip()
carga = ("Peso da carga: ").strip()
tanque = ("Capacidade do tanque: ").strip()
torre = ("Digite a torre: ").strip()
termos = input("Concorda com os termos? ").strip()
if fabricante.isalpha() and piloto.isalpha() and \
ano.isdigit() and horas.isdigit() and cpf.isdigit() and carga.isdigit() and tanque.isdigit() and \
modelo.isupper() and base.isupper() and uf.isupper() and torre.isupper() and \
prefixo.isalnum() and torre.isalnum() and \
email.count("@") == 1 and email.endswith(".com") and termos == "SIM":
    print("Registrado com sucesso. Boa viagem!")
print("-" * 42)