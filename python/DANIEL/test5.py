#o range(3) faz o codigo repetir 0,1e2 (total de 3 vezes)
#este "else" pertence ao "for" . ele só roda se o laço termina SEM o break.
senha_correta="daniel9966"
for tentativa  in range(3):
    chute = input("digite sua senha:")
    if chute ==senha_correta:
        print("senha correta! entrando...")
        break #o break interrompe o "for" imediatamente se ele acertar .
    else:
        print("senha incorreta!")
else:
    #este "else" pertence ao "for". ele só roda se o laço terminar sem o break.
    print("conta bloqueada após 3 tentativas falhas.")
