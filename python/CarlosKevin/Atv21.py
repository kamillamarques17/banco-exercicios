print('---------- SENHA SEGURA COM CONFIRMAÇÃO E TAMANHO ----------')

for tentativa in range(3):
    senha = input('Digite sua senha (8 caracteres)? ').strip()
    if len(senha) == 8:
        print('Senha definida com sucesso')
        break
    else:
        print('Tente novamente')
else:
    print('Senha inválida: ela deve ter exatamente 8 caracteres.')

print('-'*60)