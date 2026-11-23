print("-------------PAINEL DE CONTROLE DE FOGUETE ESPACIAL-------------")
for tentaive in range(3):
 nome_missão= input("Nome da missão:" ) .strip()
 código_foguete= input("Código do Foguete: ") .strip()
 data_lanc= input("Data de lançamento (DD/MM/AAAA): ") .strip()
 iddigital_astronauta= input ("ID digital do astronauta:") .strip()
 email_base= input("E-mail da base:") .strip()
 combustível= input("Combustível:") .strip()
 carga_espacial= input("Carga espacial:") .strip().upper()
 status_sistemas= input("Status do sistema") .strip()

 if código_foguete.isalnum() and carga_espacial.isalnum() and \
    iddigital_astronauta.isdigit() and combustível.isdigit() and \
    email_base.count("@") and email_base.endswith(",com") and data_lanc.count ("/") == 2 and \
    status_sistemas == "APROVADO":

    print("Registro feito com sucesso")
    break
 else: 
     print("Registro incorreto")
     print("-"*40)
else: 
 print("Bloqueio, tentativas falhas!")