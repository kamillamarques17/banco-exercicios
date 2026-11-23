print ("-----Desafio integrador: Gerenciador de tráfego aéreo-----")

for tentativa in range(5):
    id_prefixo = input ("Prefixo aeronave: ").strip()
    companhia = input ("Companhia aérea: ").strip()
    codigo = input ("Código de Voo: ").strip()
    altitude = input ("Altitude de Cruzeiro: ").strip()
    velocidade = input ("Velocidade em nós: ").strip()
    pouso = input ("Pista de pouso: ").strip()
    destino = input ("Aeroporto: ").strip()
    transponder = input ("Codigo: ").strip()
    email = input ("E-mail da torre de controle: ").strip()
    autorização = input ("Autoarização de pouso (Digite: PERMITIDO)").strip()

    if id_prefixo.isalnum() and companhia.isalpha() and codigo.isalnum() and \
    altitude.isdigit() and velocidade.isdigit() and \
    pouso.isalnum() and destino.isalpha() and transponder.isdigit() and \
    email.count("@") == 1 and email.endswith("aircontrol.com") and \
    autorização == "PERMITIDO" :

         print(f"\nSUCESSO: aeronave {id_prefixo} avião {codigo} liberado" )        
         break
    else:
         print (f"\nERRO: dados invalidos !tentativa {tentativa+1} de 5 ")
         print ("-" *40)
else:
     print ("\nBLOQUEAR: limite de 5 tentativas excedidos.")

