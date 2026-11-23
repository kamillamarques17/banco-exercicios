senha_correta = "1234"
erros = 0

for i in range(4):
    senha = input("Digite a senha do celular: ")
    
    if senha == senha_correta:
        print("Aparelho Desbloqueado")
        break
    else:
        erros += 1

if erros == 4:
    print("Celular Inoperante por 30 minutos")