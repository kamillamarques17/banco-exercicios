crianças = ["Sarah", "Luanna", "Isabelle"] 

for pessoa in crianças:

    altura = (input(f"Olá, {pessoa}, digite sua altura: "))

    if altura >= "140cm":
        print(f"Pode ir!")

    else:
        print(f"Não pode subir.")