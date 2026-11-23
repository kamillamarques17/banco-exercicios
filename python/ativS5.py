print("---Desenvolvedores e Repositorios GIT ---")
for tentativa in range(5):
    nome = input("Nome do desenvolvedor: ").strip()
    nickname = input("Digite o nickname:: ").strip()
    nome_repos = input("nome do repositório: ").strip()
    ID = input("Digite o ID: ").strip()
    quantidade= input("Digite a quantidade de linhas ").strip()
    branch = input ("Digite o branch principal : ").strip()
    linguagem= input("Digite a linguagem de programação utilizada: ").strip()
    chave_SSH= input("Digite a chave do usuario: ").strip()
    email = input("qual dominio?: ").strip()
    status = input("Status: ").strip()

    if nome.isalpha() and\
    linguagem.isalpha() and\
    nickname.isalnum() and\
    nome_repos.isalnum() and\
    quantidade.isdigit() and\
    email.endswith(".edu.br") and\
    len(chave_SSH) == 12 and\
    status == "SUCESSO!!":
     print(f"\nSUCESSO: CADASTRO {nome}, com o   {nickname} CONCLUIDO!!")
     break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido.")
