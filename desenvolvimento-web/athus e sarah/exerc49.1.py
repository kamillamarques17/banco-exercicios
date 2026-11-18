print('-----Controle de Reator de Fusão Nuclear-----')
reator = input("Qual o reator? ").strip()
elemento = input("Qual o elemento? ").strip()
massa = input("Qual a massa? ").strip()
calor = input("Digite o calor: ").strip()
pressao = input("Digite a pressão: ").strip()
fluxo = input("Digite o fluxo: ").strip()
tecnico = input("QUal o técnico? ").strip()
id_tec = input("Digite o ID do técnico: ").strip()
turno = input("Emn qual turno? ").strip()
estacao = input("Qual a estação? ").strip()
resfriamento = input("Digite o resfriamento: ").strip()
energia = input("Digite a energia: ").strip()
status = input("Qual o status? ").strip()
emergencia = input("Digite a palavra de emergência: ").strip()
chave = input("Qual a chave? ").strip()
if elemento.isalpha() and tecnico.isalpha() and \
calor.isdigit() and pressao.isdigit() and id_tec.isdigit() and id_tec == 5 and \
status == "ESTÁVEL" and status.upper() and \
emergencia != "DESATIVADA" and chave == "REATOR_ON":
   print("Concluído com sucesso!")
   print("-" * 42)