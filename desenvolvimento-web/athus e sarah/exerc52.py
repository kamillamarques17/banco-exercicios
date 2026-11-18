print('-----Registro de Software em Nuvem-----')
app = input("Nome do app: ").strip()
versao = input("Versão do app: ").strip()
linguagem = input("Linguagem usada: ").strip()
servidor = input("Número do servidor: ").strip()
ip = input("Número do IP: ").strip()
porta = input("Número da porta: ").strip()
desenvolvedor = input("Nome do desenvolvedor: ").strip()
cpf = ("Digite o CPF do desenvolvedor: ").strip()
email = input("Digite o e-mail do desenvolvedor: ").strip()
empresa = input("Nome da empresa: ").strip()
cnpj = input("Digite o CNPJ da empresa: ").strip()
pais = input("País da sede da empresa: ").strip()
licenca = input("A empresa tem licença? ").strip()
data = input("Digite a data: ").strip()
status = input("status:")
if linguagem.isalpha() and pais.isalpha() and \
porta.isdigit() and cpf.isdigit() and cnpj.isdigit() and licenca.isdigit() and \
app.isupper() and servidor.isupper() and empresa.isupper() and status.isupper() and \
versao.isalnum() and email.count("@") == 1 and email.endswith(".com") and data.count("/") == 2:
    print("Registrado com sucesso.")
print("-" * 42)