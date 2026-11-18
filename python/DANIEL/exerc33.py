cliente = input("nome do cliente ").strip()
veiculo = input("digite o modelo do veiculo (deve ser mais de 3 letras ) ").strip()
placa = input("digite sua placa (deve conter 3 caracteres ) ").strip()
KM = input("digite o km ( deve conter apenas numeros :)").strip()
serviço = input("digite o serviço desejado (não pode ser )").strip()
codigo = input("digite o codigo do tecnico (deveser axatamente T100)").strip()

if cliente.isalpha() == 3 and \
   veiculo.isalpha() == 3 and \
   len(placa) == 7 and placa.isalpha() and \
   KM.isdigit() and \
   serviços.isdigit != "TESTE" and \
   codigo.isalpha == "T100":

    print("serviços agendado com suceso!")
else:
    print("erro! verifique se esta tudo correto")
    print("-" * 30)