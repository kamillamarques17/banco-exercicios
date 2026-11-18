usuario = ["Mimi", "Isabela", "Vitória","Ana", "carlos"]

for pessoa in usuario:

    senha = input (f"Qual a senha?, {pessoa}:")

    if senha == "1212":
       
       print (f"acesso liberado,{pessoa}")

else: 
    
    print(f"senha incorreta, acesso negado {pessoa}")