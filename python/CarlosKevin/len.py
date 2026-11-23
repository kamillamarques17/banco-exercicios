senha = input('Digite sua senha: ').strip() #Borracha inteligente

if len(senha) < 8:
    print('Sua senha é curta demais!')

else:
    print('Senha aceita.')