print("---Painel de controle de foguete especial---")
missão = input('Nome da missão: ').strip()
code = input('Código do Foguete: ').strip()
lancamento = input('Data de Lançamento (DD/MM/AAAA) ').strip()
id = input('ID Digital do Astronauta: ').strip()
mail = input('E-Mail da Base: ').strip()
combustivel = input('Combustível: ').strip()
carga = input('Carga Espacial: ').strip()
status = input('Status do Sistema (APROVADO)').strip()

if (code.isalum() and carga.isalnum() and missão.isalum() and
      lancamento != "dd/mm/eeee" and id.isdigit() and combustivel.isalum() and
      status.isalpha() and mail.count("@") == 1 and mail.endswith(".com")):
    print("Cadastro válido")
else:
    print("Cadastro inválido, tente novamente")