passageiro=["Gisele","Ana","Marcos","Rafinha","Nathan","Isabela","Lionel","Cristiano","Manuelle","Kelly"]
for pessoa in passageiro:
    peso=input(f"Olá,{pessoa}. Qual o peso da sua mala?")
    if peso<= "23":
        print("Bagagem liberada!")
    else:
        print("É necessário pagar uma taxa.")