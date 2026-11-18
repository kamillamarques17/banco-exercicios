convidados= {"Duda", "Isabela", "Leo", "Samara", "pedro", "luis", "paulo", "anitta", "jose", "amora"}

for pessoa in convidados:

    
    peso = int(input("qual o peso da mala de " + pessoa + "? "))

    
    if peso <= 23: 
    
      print(pessoa, "pode embarcar. Acesso liberado!")


    else: 
    
     print(pessoa, "não pode embarcar. Acesso negado!") 