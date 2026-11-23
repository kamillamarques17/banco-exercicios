print('---Regitro de Criptoativos')

cliente = input('Nome do Cliente: ')
cripto = input('Nome da Criptomoeda: ')
hash = input('Código Hash da Carteira: ')
trans = input('Data da Transação: ')
id = input('ID Númerico do Bloco: ')
mail = input('E-Mail de Suporte: ')
quant = input('Quantidade de Moedas:')
auten = input('Confirmar Autenticação (APROVADO):')

if cripto.isalnum() and hash.isalnum() and \
    id.isdigit() and  quant.isdigit() and\
    trans.count('/') == 2 and\
    mail.count('@') == 1 and mail.endswith('.com'):
    print('Registro Completo')
else:
    print('Registro inválido, tente novamente')

