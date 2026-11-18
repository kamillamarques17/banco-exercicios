senha_correta = "Lua"
for tentativa in range(3):
    
    chute = input ("Digite a senha: ")
    if chute == senha_correta:
        print("Senha correta! Entrando... ")
        break 
    else:
        print("Senha icorreta")
else:
    
    print("Conta bloqueada após 3 tentativas falhas.")