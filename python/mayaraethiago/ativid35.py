print("-----------Validação de embarque Nacional-----------")
cliente = input("Nome: ")
veiculo = input("Veiculo: ")
cor = input("Cor: ")
cnh = input("CNH: ")
dias = input("Por quanto tempo desejas reservar? ")
seguro = input("Incluir seguro? ")

if cor.isdigit() and \
len(cnh) == 9 and veiculo == "SEDAN":
    print("Reservado com sucessso!")
print("-"*50)