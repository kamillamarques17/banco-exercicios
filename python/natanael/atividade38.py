print("-------------Ponto dos funcionários-------------")
for tentativa in range(3):
     funcionario = input("Digite o nome do funcionário:").strip()
     unidade = input("Digite a unidade do funcionário:").strip()
     id = input("Digite o ID do funcionário:").strip()
     cargo = input("Digite o cargo do funcionário:").strip()
     hora_entrada = input("Digite a hora de entrada do funcionário:").strip()
     cod_verificação = input("Digite o código de verificação do funcionário:").strip()
     if funcionario.isalpha() >3 and unidade =="SUL" and id> 5 and\
          cargo.isalpha() and hora_entrada.isdigit> 4 and cod_verificação !="123":
               print("Funcionário registrado com sucesso.")
               break
     else:
          print("Erro: Verificar os dados.")
else:  
     print("Número máximo de tentativas atingido. Tente novamente mais tarde.")