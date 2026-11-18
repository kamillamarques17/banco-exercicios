pessoa=["Kamilla","Ana","Maria","Mateus","Chico","Divino","Raskolnikov","Messi", "Antonella"]
for cliente in pessoa:
 camisa=input(f"Quantas camisas você deseja comprar, {cliente}? ")
 if camisa<="5":
     print("Venda realizada!")
 else:
     print("Quantidade indisponível no estoque.") 