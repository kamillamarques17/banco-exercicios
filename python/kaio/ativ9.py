
Usuario = ["Admin", "suporte", "daniel"]


for pessoa in Usuario:

   
    senha = input(f"Qual é a senha de acesso, {pessoa}?:")

    
    if senha == "kaio22":
       
        print(f"senha incorreta. Acesso negado, {pessoa}")
       
    else:
      
        print(f"Acesso liberado,{pessoa}")