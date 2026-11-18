print("-------------------------CADRASTO DE PERFIL DE USUARIO--------------------------")
for tentativas in range(3) :
 nome=input("digite o seu nome(3 carcteres): "). strip()
 cidade= input("digite sua cidade (4 carcteres): "). strip ()
 sigla= input("digite sua cidade (2 carcteres): "). strip ()

 if len(nome) > 3 and len( cidade) >4 and len (sigla) ==2:
      print(f"sucesso, nome {nome}, cidade{cidade}, e sigla {sigla} aceitos")
      break
else:
   print("acesso negado")

 