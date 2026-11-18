print("---- REGISTRO DE STARTUP NO VALE DO SILÍCIO ----")

for tentativa in range(3):

    nome = input("Digite o nome da startup: ").strip()
    fundador = input("Digite o fundador: ").strip()
    email = input("Digite o e-mail: ").strip().lower()
    setor = input("Digite o setor: ").strip()
    ano = input("Digite o ano de fundação: ").strip()
    cnpj = input("Digite o CNPJ (somente números): ").strip()
    investimento = input("Digite o investimento (somente números): ").strip()
    moeda = input("Digite a moeda (USD): ").strip().upper()
    sede = input("Digite a sede: ").strip().upper()
    funcionarios = input("Digite a quantidade de funcionários: ").strip()
    site = input("Digite o site: ").strip()
    linguagem = input("Digite a linguagem principal: ").strip()
    versao = input("Digite a versão: ").strip()
    servidor = input("Digite o servidor: ").strip()
    termos = input("Aceita os termos de uso? (ACEITO): ").strip().upper()

    if nome.replace(" ", "").isalpha() and \
       setor.replace(" ", "").isalpha() and \
       moeda == "USD" and \
       cnpj.isdigit() and \
       investimento.isdigit() and \
       sede != "CASA" and \
       termos == "ACEITO":

        print(f"Cadastro aprovado! Startup {nome} registrada com sucesso.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO. Registro encerrado.")