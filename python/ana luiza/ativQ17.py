print("--- REGISTRO ACADÊMICO SUPERIOR ---")
for tentativa in range(5):
    diplomado = input("Nome do Diplomado: ").strip().title()
    sobrenome = input("Sobrenome: ").strip().title()
    curso = input("Nome do Curso Superior: ").strip().title()
    cidade = input("Cidade do Campus: ").strip().title()
    diploma = input("Código do Diploma (Ex: DIP-01): ").strip()
    livro = input("Livro de Registro: ").strip()
    ch = input("Carga Horária Cumprida: ").strip()
    media = input("Média Geral de Conclusão: ").strip()
    data = input("Data da Colação de Grau (DD-MM-AAAA): ").strip()
    email = input("E-mail da Reitoria: ").strip().lower()
    hash_cert = input("Código Hash do Certificado: ").strip()
    status = input("Status do Diploma (REGISTRADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if diplomado.isalpha() and \
       sobrenome.isalpha() and \
       curso.isalpha() and \
       cidade.isalpha() and \
       diploma.startswith("DIP-") and \
       livro.isalnum() and \
       ch.isdigit() and \
       media.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".universidade.edu.br") and \
       status == "REGISTRADO":
        
        hash_oculto = "*" * len(hash_cert)
        print(f"\nSUCESSO: Diploma de {diplomado} {sobrenome} no curso de {curso} registrado!")
        print(f"Data Padronizada: {data_formatada} | Hash Protegido: {hash_oculto}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")
