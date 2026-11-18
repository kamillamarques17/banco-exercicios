#o usuário digito o que quer fazer 
objetivo = input("o que você quer postar ?(fotos/videos/textos):")
#o pograma recomenda a rede social 
if objetivo == "fotos":
    print("recomendação :instagram")
elif objetivo == "videos":
    print("recomendação : tiktok ou youtube ")
elif objetivo == "noticias"or objetivo == "twitter":
    print("recomendação: X (antigo twitter)ou thereads")
else:
    print("essa opção não esta no banco de dados")