senha_celular = "1234"
for tentativa in range(4):
    senha = input("Digite a senha do celular:")


    if  senha == senha_celular:
     print("Aparelho desbloqueado")
     break
else:
    print("Celular inoperante por 30 min.")
