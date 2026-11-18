crianças=["bruno", "carla","diego"]

for pessoa in crianças:

    altura = int(input(f"digite a altura de {pessoa}em centimetros:"))
    
if altura > 140:
    print(f"pode subir:{pessoa}.")
else:
    print(f"não pode subir:{pessoa}.")