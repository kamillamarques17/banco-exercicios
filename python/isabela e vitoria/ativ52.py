print ("---------Registro de Software em Nuvem---------")
app = input("App: ")
versao = input("Versão: ")
linguagem = input("Linguagem: ")
servidor = input("Servidor: ")
ip = input("IP: ")
porta = input("Porta: ")
desenvolvedor = input("Desenvolvedor: ")
cpf = input("CPF: ")
email = input("E-mail: ")
empresa = input("Empresa: ")
cnpj = input("CNPJ: ")
pais = input("País: ")
licenca = input("Licença: ")
data = input("Data: ")
status = input("Status: ")

if (linguagem.isalpha() and
    pais.isalpha() and
    porta.isdigit() and
    cpf.isdigit() and len(cpf) == 11 and
    cnpj.isdigit() and len(cnpj) == 14 and
    licenca.isdigit() and
    app.upper() and
    servidor.upper() and
    empresa.upper() and
    status.upper() and
    versao.isalnum() and
    email.endswith(".com") and
    data.count("/") == 2 and
    status == "ATIVO"):

    print("Registro válido!")
else:
    print("Registro inválido!")

