senha = input("digite sua senha: ").strip()

if len(senha) < 8:
    print("Sua senha é curta demais!")
else:
    print("Senha aceita")
    
    #strip funciona como uma borracha inteligente
    #len() faz uma contagem de caracteres dependendo do que for. Se for um texto (strings)
    #ele conta quantos caracteres existem, e em listas quantos itens tem. O .strip() remove espaço em branco