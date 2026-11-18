print("------CADASTRO DE PRODUTO QUIMICO CONTROLADO ------")

for tentativa in range(2):
   substancia = input("Digite a sua substancia: ").strip()
   tipo = input("Digite o tipo: ").strip()
   lote = input("Digite o lote: ").strip()
   responsavel = input("Digite o responsavel: ").strip()
   CRM = input("Digite o CRM: ").strip()
   validade = input("Digite a data de validade: ").strip()

   if len(CRM) == 5 and len(validade) ==8 and \
       tipo == "SOLVENTE" and  \
       lote != "0000":
        
     print("Deu tudo certo.")
     break
   else:
        print("Erro: Verifique os dados digitados.")
       
