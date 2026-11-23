print('-----Registro de Startup no vale do Silício-----')
for tentativa in range(3):
    nome_startup = input("Nome da startup: ").strip()
    fundador = input("Nome do(a) fundador(a): ").strip()
    email = input ("Digite seu e-mail: ").strip()
    setor = input("Digite o setor: ").strip()
    ano_de_fundac = input("Ano de fundação: ").strip()
    cnpj = input("Digite o CNPJ (14 núm.): ").strip()
    investimento = input("Quanto você deseja investir? ").strip()
    moeda = input("Qual a moeda? ").strip()
    sede = input("Sede: ").strip()
    func = input("QTDE. de funcionários: ").strip()
    site = input("Digite o URL: ").strip()
    linguagem_princ = input("Linguagem principal: ").strip()
    versao = input("Versão: ").strip()
    servidor = input("Servidor: ").strip()
    termos = input("Termos de uso: ").strip()
    if fundador.isalpha() and setor.isalpha() and \
    email.lower() and moeda == "USD" and moeda.upper() and \
    cnpj.isdigit() and investimento.isdigit() and \
    sede != "CASA" and termos == "ACEITO":
        print("Registrado com sucesso!")
else:
    print("Falha nos dados.")
print('-'*42)