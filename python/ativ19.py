print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------")

codigo = "410"
senha = "01040"

for chute in range(3):
    codigo_digitada = input ("Digite o codigo:")
    senha_digitada = input ("Digite a senha: ")

    if codigo_digitada == "codigo" and "senha_digitada" ==  senha:
        print("Acesso aceito!")
        break
    else:
             print(f"Dados incorretos!")
else:
     print("Acesso negado. Tente nas proximas horas.")
