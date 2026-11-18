print("-----sturp---")

for tentativa in range(3):
    nomedaStarptup= input ("digite seu nome:").strip
    email = input ("digite seu email:").strip
    setor = input ("digite seu setor").strip
    anodefundação = input ("digite seu ano de fundação").strip
    CNPJ = input ("14 num ").strip
    investimento = input("digite seu investimento ").strip
    moeda = input ("USD").strip().upper()
    sede = input ("digite sua sede").strip().upper()
    funcionarios = input ("digite seu nome de funcionarios: ").strip()
    site = input ("digite o link do site").strip()
    linguagem = input ("digite a linguagem").strip()
    versão = input ("digite sua versão").strip()

    if nomedaStarptup.isalpha() and nomedaStarptup.isalpha() and \
      email.isalpha () and \
      setor.isalpha () and \
      anodefundação.isalpha () and \
      CNPJ.isdigit () and \
      investimento.isdigit () and \
      len(moeda) and moeda.isalpha() == "USD" and \
      len(sede) and sede.isalpha() == "aceito":
    
       print (f"acesso liberado! BEM-VINDO ao sistema.{nomedaStarptup}")
       break
else:
    print("sistema bloqueado. alerta de instrução enviado à segurança.")