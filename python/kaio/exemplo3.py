#o range (3)faz o codigo repetir 0,1 e 2(total de 3 vezes).
#Este "else" pertence a o "for". Ele se roda se o laço terminar SEM o break.

senha_correta = "abacate"
for tentativa in range(3):
    chute = input ("Digite a senha: ")
    if chute == senha_correta:
        print("Senha correta! Entrando... ")
        break # O break interrope o "for imediatamente se ele acertar."
    else:
        print("Senha icorreta")
else:
    # Este "else" pertence ao 'for.' Ele so roda se o laço terminar sem o break.
    print("Conta bloqueada após 3 tentativas falhas.")