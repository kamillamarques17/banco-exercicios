print("----------------Registro de Startup no Vale do Silício----------------")
for tentativa in range(3):
    nome_startup = input("Qual o nome do startup?").strip()
    fundador = input("Qual o fundador? ").strip()
    email = input("Qual o e-mail? ").strip()
    setor = input("Qual o setor? ").strip()
    ano_fundação = input("Digite o ano da fundação? ").strip()
    CNPJ = input("Qual o CNPJ (14 numeros)?").strip()
    investimento = input("qual o investimento? ").strip()
    moeda = input("qual a moeda? (USD)")
    sede = input("Qual a sede?")
    funcionários = ("Nome do funcionáro:")
    site = ("site:")
    linguagem_principal = ("lingua:")
    versão = ("qual a versão?")
    servidor = ("Qual servidor?")
    termos_uso = ("termos de uso:")

    if nome_startup.isalpha() and fundador.isalpha() and email.lower() and setor.isalpha() and \
    ano_fundação.isdigit() and CNPJ.isdigit() ==14 and investimento.isdigit() and moeda.upper( ) == "USD" and \
    sede != "CASA" and funcionários.isalpha() and  site() and linguagem_principal() and \
    versão() and servidor() and termos_uso() == "ACEITO":
       
       print("Registro concluido!")
       break
    else:
       print("Registro errado.")
       print("-" * 30)

else:
   print("Tentativas bloqueadas")

