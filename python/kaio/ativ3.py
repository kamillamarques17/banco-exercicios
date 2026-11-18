tipo_cliente = input("digite oq deseja (1: Fotos / 2: Videos / 3: Noticias):")
if tipo_cliente == "1":
    print("Item recomendado (Instagram).")
elif tipo_cliente == "2":
    print("item recomendado TikTok (Video)")
elif tipo_cliente == "3":
    print("Item recomendado Twitter (Noticias).")
else:
    print(" Essa opção não esta no banco de dados.")