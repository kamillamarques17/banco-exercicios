print("------------Desbloqueio do celular---------------")
senha_salvo = "12345"

for tentativa in range(4):
    senha_digitada = input("Digite a senha do celular")
    
    if senha_digitada == senha_salvo:
        print("Aparelho desbloqueado!")
        break
    else:
        print(f"Senha errada, tente novamente")
        
else:
    print("Celular inativo por 30 minutos.")