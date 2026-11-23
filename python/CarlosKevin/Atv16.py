senha_correta = "cafe2026"
erros = 0

for i in range(3):
    senha = input("Digite a senha do Wi-Fi: ")
    
    if senha == senha_correta:
        print("Wi-Fi Liberado")
        break
    else:
        erros += 1

if erros == 3:
    print("Acesso bloqueado")