print("--- AUDITORIA FORENSE DIGITAL ---")
for tentativa in range(5):
    perito = input("Nome do Perito: ").strip().title()
    especialidade = input("Especialidade Forense: ").strip().title()
    departamento = input("Departamento Policial: ").strip().upper()
    cidade = input("Cidade da Ocorrência: ").strip().title()
    evidencia = input("Código da Evidência: ").strip()
    hash_sha = input("Hash SHA-256 da Imagem: ").strip()
    tamanho = input("Tamanho em Megabytes: ").strip()
    lacre = input("Número do Lacre: ").strip()
    data = input("Data da Apreensão (DD-MM-AAAA): ").strip()
    email = input("E-mail do Instituto de Perícia: ").strip().lower()
    senha = input("Senha do Cofre Digital: ").strip()
    parecer = input("Parecer Forense (INTEGRO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if perito.isalpha() and \
       especialidade.isalpha() and \
       cidade.isalpha() and \
       evidencia.startswith("EVID-") and \
       hash_sha.isalnum() and \
       tamanho.isdigit() and \
       lacre.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".policia.gov.br") and \
       parecer == "INTEGRO":
        
        senha_oculta = "*" * len(senha)
        print(f"\nSUCESSO: Evidência {evidencia} auditada por {perito} em {cidade}!")
        print(f"Data Padronizada: {data_formatada} | Senha Protegida: {senha_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")