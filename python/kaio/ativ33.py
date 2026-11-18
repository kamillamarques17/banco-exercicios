cliente = input("Nome do cliente: ").strip()
veiculo = input("Digite o modelo do veiculo (Deve ser > 3 letras: )").strip()
placa = input("Digite sua placa (Deve ter exatamente 7 caracteres: )").strip()
km = input("Digite o km (Deve conter apenas numeros: )").strip()
serviços = input("Digite o serviço desejado (Não pode ser 'TESTE': )").strip()
codigo = input("Digite o codigo do tecnico (Deve ser exatamente T100)").strip() 

if cliente.isalpha() == 3 and \
   veiculo.isalpha() == 3 and \
   len(placa) == 7 and placa.isalpha() and \
   km.isdigit() and \
   serviços.isdigit != "TESTE" and \
   codigo.isalpha == "T100":

    print("Serviço agendado com sucesso!")
else:
    print("Erro: Verifique se esta tudo correto ")
    print("-" * 30)