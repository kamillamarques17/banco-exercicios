print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------" )
nome = input("Olá! Digite seu nome: ").strip()
cidade = input("Agora digite sua cidade: ").strip()
sigla = input("Por último, digite a sigla: ").strip()
for tentativa in range(3):
    if len(nome) > 3 and len(cidade) > 4 and len(sigla) == 2:
         print("Perfil criado com sucesso!")
         break
else:
     print("Sem sucesso.")
print('-'*30)