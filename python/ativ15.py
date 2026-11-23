pessoa={"Hayzel", "Tyler", "Liam", "Elias", "Dante", "Ashley", "Mauricio", "Jasper", "Luna"}
for cliente in pessoa:
    
    camisa=input(f"Quantas caisas você deseja compra, {cliente}? ")
    if camisa<= "5":
        print("Venda realizada!")
    else:
        print("Quantidade indisponível no estoque.")