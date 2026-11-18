print("----------------Controle e Reator de fusão nuclear---------------")
for tentativa in range(3):
    reator = input("Informe o reator: ").strip()
    elemento = input("Qual o elemento: ").strip() 
    massa = input("Digite a massa: ").strip()
    calor = input("Qual o calor? ").strip() 
    pressão = input("Informe a pressão: ").strip() 
    fluxo = input("Digite o fluxo: ").strip()
    técnico = input("Qual o técnico? ").strip() 
    ID_Tec = input("Digite o Id_Tec: (5 digitos) ").strip() 
    Turno = input("Qual o turno: ").strip()
    estação = input("Qual a estação? ").strip()
    resfriamento = input("Informe o resfriamento: ").strip()
    energia = input("Digite a energia: ").strip()
    Status = input("Informe o status: ").strip() 
    emergencia = input("Qual a emergencia? ").strip() 
    chave = input("informe a chave:") 

    if elemento.isalpha() and técnico.isalpha() and calor.isdigit() and \
    pressão.isdigit() and ID_Tec.isdigit == 5  and Status.upper() == "ESTAVEL" and \
    emergencia !="DESATIVADA" and chave == "REATOR_ON" and reator() and massa() and fluxo() and Turno() and estação() and \
    resfriamento() and energia():

        
         print("Controle concluido!")
         break
    else:
       print("Erro no controle.")

       
       print("-" * 30) 
else:
      print("Tentativas bloqueadas")
