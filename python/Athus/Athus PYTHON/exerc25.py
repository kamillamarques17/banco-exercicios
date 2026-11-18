print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------")
produto = input("Olá! Especifique o produto: ").strip()
codigo_carga = input("Agora, digite o código: ").strip()
destino = input("Por último, marque o destino: ").strip()
for tentativa in range(3):
    if len(produto) != "PROIBIDO" and len(codigo_carga) == 6 and len(destino) > 3:
         print("Registrado com sucesso!")
         break
else:
     print("Falha em registrar.")
print('-'*30)