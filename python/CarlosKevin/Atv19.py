print('---------- NOMES PROIBIDOS ----------')
nomes = ['']
for tentativa in range(3):
  
    code_area = input('Qual o Código de Área?').strip()
    senha = input('Qual sua Senha Pessoal?').strip()
    if codigo_de_area == code_area and senha_pessoal == senha:
        print('Acesso Completo')
        break
    else:
        print('Tente novamente')
else:
    print('Muitas falhas, conta bloqueada')

print('-'*42)