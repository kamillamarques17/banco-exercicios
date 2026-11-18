print("-------------------------CADRASTO DE PERFIL DE USUARIO--------------------------")
nome_proibido = "PROIBIDO"
for tentativas in range(3) :
 produto=input("digite o seu produto(3 carcteres): "). strip()
 codigo= input("digite o seu codigo(6 carcteres): "). strip ()
 destino= input("digite seu destino (2 carcteres): "). strip ()

 if len(produto) >3 and len( codigo) ==4 and len (destino) >2:
      print(f"sucesso, o produto {produto}, tem o codigo{codigo}, e destino {destino}")
      break
else:
   print("acesso negado")

 