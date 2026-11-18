print("-------------------------O VERIFICADOR DE LISTA DE NOMES PROIBIDOS--------------------------")
nome_proibido = "adm" "root" "suporte"
for tentativas in range(3) :


     chute = input("Digite o codigo de area: ")
     senha = input("Digite a senha correta: ")
     if chute == codigo_de_area and senha == senha_pessoal:
        print("senha correta")
        break
     else:
         print("senha incorreta")
else:
 print("muitas falhas, contra bloqueada")