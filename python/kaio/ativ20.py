for tentativa in range(3):
 senha = input("Digite seu nome de usuario: ").strip()

 if len(senha) >= 5:
    print(f"Usuario aceito! {senha}")
    break
 else:
    print("Nome muito curto! Digite novamente!")
else:
 print("Acabaram as tentativas")