print("------REGISTRO DE PONTO ELETRONICO------")

for tentativa in range(3):
  funcionario = input("Digite o seu nome: ").strip()
  unidade = input("Digite a sua unidade: ").strip()
  ID= input("Digite o ID: ").strip()
  cargo = input("Digite o seu cargo: ").strip()
  hora_de_entrada= input("Digite a hora de entrada: ").strip()
  codigo_de_verificação = input("Digite o seu codigo de verificação: ").strip()

  if len(funcionario) >3 and len(ID) ==5 and ID.isdigit and \
       hora_de_entrada.isdigit and len(hora_de_entrada) ==4 and \
       codigo_de_verificação != "123":
       cargo.isalpha and \
       unidade == "sul"

       print("Deu tudo certo.")
       break
  else:
        print("Erro: Verifique os dados digitados.")
       
else:
    print("Muitas tentativas falhas.")