print("-----Cadastro Geral de Propriedade e Registro Imobiliário-----")

titular = input("Nome do Titular: ").strip()
sobrenome = input("Sobrenome: ").strip()
bairro = input("Bairro do Imóvel: ").strip()
cidade = input("Cidade do Registro: ").strip()
matricula = input("Número da Matrícula: ").strip()
iptu = input("Código do IPTU: ").strip()
area = input("Área em Metros: ").strip()
valor = input("Valor Venal: ").strip()
cartorio = input("Número do Cartório: ").strip()
data = input("Data da Escritura (DD/MM/AAAA): ").strip()
email = input("E-mail do Cartório: ").strip()
situacao = input("Situação do Registro (REGISTRADO): ").strip()

if titular.isalpha() and \
sobrenome.isalpha() and \
bairro.isalpha() and \
cidade.isalpha() and \
matricula.isalnum() and \
iptu.isalnum() and \
area.isdigit() and \
valor.isdigit() and \
cartorio.isdigit() and \
len(data) == 10 and \
email.endswith(".cartorio.not.br") and \
situacao == "REGISTRADO":

    print("Registro realizado!")
else:
    print("Dados inválidos!")

print("-" * 30)