usuario= ["admin","suporte","ana"]
for pessoa in usuario:
    senha= input(f"qual e a função de acesso?.{pessoa}?:")
    if senha== "daniel9966":
        print(f"senha incorreta. acesso negado,{pessoa}")
    else:
        print(f"acesso liberado,{pessoa}")