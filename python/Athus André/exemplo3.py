# O range (3) faz o código 0, 1 e 2 (total de 3 vezes).
# Este 'else' pertence ao 'for'. Ele só roda se o laço terminar SEM o break.

senha_correta = "abacate"
for tentativa in range (3):
    chute = input("Digite a senha: ")
    if chute == senha_correta:
      print("Senha correta! Entrando....")
      break # Obreak intemrrope o 'for' imediatamente se ele acertar.
    else:
       print("Senha incorreta!")
else: 
   print("Conta bloqueada após 3 tentativas falhas.")

