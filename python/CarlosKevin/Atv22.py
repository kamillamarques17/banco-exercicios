print('---------- Check-in Aeroporto ----------')
for tentativa in range(3):
    voo = input('Qual o Código de Voo? ').strip()
    assento = input('Qual seu assento? ').strip()
    if len(voo) == 4 and len(assento) == 3:
        print(f'Seu voo está correto {voo} e assento {assento} aceitos')
        break
    else:
        print('Acesso Negado!')
print('-'*42)