print('---------- LOGIN COM NOME DE USUÁRIO ----------')

for tentativa in range(3):
    nome = input('Qual seu nome? ').strip()
    if len(nome) > 4:
        print('Usuário Aceito')
        break
    else:
        print('Tente novamente')
else:
    print('Nome muito curto!')

print('-'*47)