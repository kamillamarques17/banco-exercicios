print("---servidor de dados ---")
for tentativa in range(5):
    nome = input("Nome do paciente: ").strip()
    especialidade = input("especialidade: ").strip()
    numero_pront = input("numero do prontuario: ").strip()
    CRM = input("Digite o CRM: ").strip()
    codigo_convenio= input("Digite o codigo do convenio ").strip()
    batimentos_BPM = input ("Batimentos : ").strip()
    temperatura= input("Digite a temperatura do cliente: ").strip()
    sala = input("Digite a sala de atnendiemento: ").strip()
    email = input("qual dominio?: ").strip()
    status= input("Status: ").strip()

    if nome.isalpha() and\
    especialidade.isalpha() and\
    numero_pront.isdigit() and\
    batimentos_BPM.isdigit() and\
    sala.isdigit() and\
    CRM.isalnum() and len(CRM) == 7 and\
    email.count("@") and email.endswith(".med.br") and\
    status == "URGENTE!":
     print(f"\nSUCESSO: SALA DE TRIAGEM {nome}, com o  {numero_pront} venha até a sala 2!!") 
     break
    else:
       print(f"\nERRO:Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO:Limite e 5 tentativas excedido. ")