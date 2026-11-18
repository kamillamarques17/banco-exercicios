crianca=["Kevin","Pietro","Carlos","Geovana","Ana Júlia","Vitória"]
for pessoa in crianca:
    peso=input(f"Qual o seu peso,{pessoa}?")
    if peso<= "40":
        print(f"Você pode balançar, {pessoa}!")
    else:
        print(f"Desculpe {pessoa}, você não pode balançar.")