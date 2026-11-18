print("---Cadastro de projeto de engenharia-----")

projeto = input("Digite o seu projeto: ").strip()
código = input("Digite o seu código: ").strip()
engenheiro = input("Digite o seu nome: ").strip()
CREA = input("Digite o seu CREA: ").strip()
setor = input("Digite o seu setor: ").strip()
orçamento = input("Digite o seu orçamento: ").strip()
data_inicio = input("Digite a sua data de início (DD/MM/AAAA): ").strip()
data_fim = input("Digite sua data de fim (DD/MM/AAAA): ").strip()
cidade = input("Digite a sua cidade: ").strip()
UF = input("Digite o seu UF: ").strip().upper()
email = input("Digite o seu email: ").strip()
cliente = input("Digite o seu cliente: ").strip()
CNPJ = input("Digite o seu CNPJ: ").strip()
prioridade = input("Digite a sua prioridade: ").strip()
status = input("Digite o seu status: ").strip().upper()

if (
    projeto.isalnum() and 
    código.isalnum() and 
    engenheiro.replace(" ", "").isalpha() and  
    CREA.isdigit() and 
    setor.isalnum() and 
    orçamento.replace(".", "", 1).isdigit() and  
    data_inicio.count("/") == 2 and 
    data_fim.count("/") == 2 and 
    cidade.replace(" ", "").isalpha() and     
    UF.isalpha() and len(UF) == 2 and 
    email.count("@") == 1 and 
    cliente.replace(" ", "").isalpha() and     
    CNPJ.isdigit() and len(CNPJ) == 14 and 
    prioridade.isdigit() and 
    status == "APROVADO"
):
    print(f"\nAcesso liberado! Bem-vindo ao sistema, {engenheiro}.")
else:
    print("\nSISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")
