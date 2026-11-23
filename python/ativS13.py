print("---SISTEMA HOPITALAR---")
for tentativa in range(5):
    nome_paciente = input("Nome do paciente: ").strip()
    especialiade = input("Qual a especalidade medica?: ").strip()
    CRM = input("Digite o CRM de origem:")
    cod_leito = input("Digite o codgo de leito: ").strip()
    frequencia= input("Digite a frequencia cardiaca : ").strip()
    pressao = input("Qual a pressao?:): ").strip()
    medicamento = input("Qual o medicamento?")
    saturação = input ("Qual a saturação?: ").strip()
    temperatura = input("Digite a temperatura corporal: ").strip()
    data= input("Digite a data e admissão: ").strip()
    email = input ("Dgite o email do hopital:")
    status = input("Status:")

    if nome_paciente.isalpha() and\
    especialiade.isalpha() and\
    medicamento.isalpha() and\
    CRM.isalnum() and\
    cod_leito.isalnum() and\
    frequencia.isdigit() and\
    pressao.isdigit() and\
    saturação.isdigit() and\
    temperatura.isdigit() and\
    email.endswith(".med.br") and\
    len(CRM) == 6 and \
    status == "ESTAVEL":
      print(f"\nSUCESSO: o paciente de {nome_paciente}, com o {cod_leito} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   