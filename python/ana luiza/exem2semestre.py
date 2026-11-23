print("--- SISTEMA DE LANÇAMENTO ESPACIAL ---")

for tentativa in range(5):

    missao = input("Nome da Missão: ").strip()
    cod_foguete = input("Código do Foguete (Ex: APOLLO11): ").strip().upper()
    data = input("Data do Lançamento (DD/MM/AAAA): ").strip()
    id_astronauta = input("ID Digital do Astronauta: ").strip()
    email_base = input("E-mail da Base: ").strip().lower()
    combustivel = input("Nível de Combustível (Apenas números): ").strip()
    carga = input("Carga Espacial: ").strip()
    pressao = input("Pressão da Cabine: ").strip()
    cidade = input("Cidade de Origem: ").strip()
    status = input("Status do Sistema (Digite APROVADO): ").strip().upper()

    
    if cod_foguete.isalnum() and\
    carga.isalnum() and\
    id_astronauta.isdigit() and\
    combustivel.isdigit() and\
    pressao.isdigit() and\
    cidade.isalpha() and\
    email_base.endswith(".gov.br") and\
    len(data) == 10 and \
    status == "APROVADO":

     
     print(f"\nSUCESSO: Astronauta {id_astronauta}, foguete {cod_foguete} liberado!") 
     break
    else:
      
       print(f"\nERRO: Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")