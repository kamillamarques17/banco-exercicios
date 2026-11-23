print("Registro de Startup")
for tentativa in range(3):
    nome_startup = input("Startup?:").strip()
    fundador = input("Qual o fundador?: ").strip()
    email = input("Qual o e-mail?: ").strip()
    setor = input("Qual ○ setor?: ").strip() 
    fundador_ano = input("Digite ano fundador?: ").strip()
    CNPJ = input("Qual o cnpj?: ").strip()
    investimento = input("Qual o investimento?: ").strip()
    moeda = input("Qual a moeda?: ").strip()
    sede = input("Qual a sede?: ").strip()
    funcionarios = input("Quantos funcionarios?: ").strip()
    site = input("Qual o site?: ").strip() 
    linguagem_principal = input("Qual a linguagem principal?:").strip()
    versão = input("Qual a versão?: ").strip()
    servidor = input("Qual O servidor?: ").strip()
    termos = input("Quais or termos de uso?: ").strip()
    if nome_startup.isalpha() and setor.isalpha() and email.lower() and moeda.upper() -- "USD" and \
    CNPJ.isdigit and investimento.isdigit and sede != "CASA" and termos == "ACEITO":
       print("Cadastro concluido!")
       break
    else:
       print("Erro fatal.")
       print("-"*30)
else:
       print("Tentativas bloqueadas")