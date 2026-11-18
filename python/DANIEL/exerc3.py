#clima
temperatura = float (input("qual e a temperatura atual em °C?"))

if temperatura >30:
    print("esta calor! use roupas leves.")
elif temperatura >= 20:
    print ("clima agradavél, use camisa.")
elif temperatura >= 10:
    print("o clima esfriou, leve um casaco leve.")
else:
    print ("esta muito frio, use roupas pesadas.")
