print('-----Cadastro de Produto Químico Controlado-----')
substancia = input("Qual substância deseja licenciar? ").strip()
tipo = input("Qual o tipo? ").strip()
lote = input("Nº lote: ").strip()
responsavel = input("Nome do(a) responsável: ").strip()
crm = input("Nº CRM: ").strip()
validade = input("Validade: ").strip()
if len(crm) == 5 and len(validade) == 8 and \
lote != "000" and tipo == "SOLVENTE": 
   print("Cadastrado com sucesso!")
print('-'*42)