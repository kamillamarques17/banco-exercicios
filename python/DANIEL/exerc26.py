for tentativas in range(3):
    nome = input("digite seu nome (nome tem que ter mais de 3 caracteres):").strip()
    senha = input("digite sua senha (a senha tem que ter 4 caracteres):").strip()
    frase = input("digite sua frase. (deve conter mais de 10 caracteres):").strip()

    if len(nome) == 3 and len(senha) >4 and  len(frase) >10:
     print(f"digite seu nome {nome} digite sua senha {senha} sua frase e {frase}")
    break
else:
  print("o nome tem que ter mais de 3 caracteres ")