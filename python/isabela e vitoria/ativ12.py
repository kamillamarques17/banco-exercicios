
convidados= {"Duda", "Isabela", "Leo"}

for pessoa in convidados:

    
    altura = int(input("qual a altura de " + pessoa + "? "))

    
    if altura >= 140: 
    
      print(pessoa, "pode subir. Acesso liberado!")


    else: 
    
     print(pessoa, "não pode subir. Acesso negado!") 