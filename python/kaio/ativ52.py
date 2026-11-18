print("---------------------SOFTWARE EM NUVEM-----------------------")

for tentativa in range(1): 
    app = input("Digite o nome do app :").strip()
    versão = input("Digite a versão:").strip()
    linguagem = input("Digite a lingugem:").strip()
    servidor = input("Digite o servidor:").strip()
    ip = input("Digite o ip:").strip()
    porta = input("Digite a porta :").strip()
    desevolvedor = input("Digite o nome desenvolvedor :").strip()
    cpf = input("Digite seu cpf :").strip()
    email = input("Digite o seu email :").strip()
    empresa = input("Digite onome da empresa :").strip()
    cnpj = input("Digite o cnpj :").strip().upper()
    pais = input("Digite o pais :").strip()
    licença = input("Digite a licença :").strip()
    data = input("Digite a data:").strip().upper()
    status = input("Digite o status:").strip().upper()

    if app.isalpha() and app.isalpha() and \
    versão.isdigit() and \
    linguagem.isalpha() and \
    servidor.isdigit() and \
    ip.isdigit() and \
    desevolvedor.isalpha() and \
    porta.isalpha() and \
    cpf.isdigit() and \
    cnpj.isdigit() and \
    pais.isalpha() and \
    porta.isalpha() and \
     len(licença) and licença.isalpha() == 5 and \
    len(pais) and pais.isalpha() == 5 and \
    len(status) and status.isalpha() == "ATIVO" and \
    data.count("/") == 2 and \
    email.count("@") == 1 and email.endswith(".com"):
               
           print(f"Acesso liberado! Bem-vindo ao sistema do {app}.")
           break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")