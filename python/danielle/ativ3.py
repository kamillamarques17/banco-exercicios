rede_social = input("Digite seu perfil (1: Instagram  / 2: TikTok / 3: Twitter / 4: não está no banco de dados)")

if rede_social == "1":
    print("Se quiser ver fotos (instagram).")
elif rede_social == "2":
    print("se quiser ver vídeos (TikTok).")

elif rede_social == "3":
    print("Se quiser ver notícias (Twitter).")

else: 
    print("Essa opção não está,no banco de dados.")
