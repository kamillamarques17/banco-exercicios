print("------------Verificador Nomes Proibidos---------------")
for tentativa in range(3):
    nome = input("Digite o nome do usuário:")
if len(nome) < 15 and nome.lower() not in ["admin", "root", "suporte"]:
    print("Nome aceito. Digite sua senha para continuar.")
else:    print("Nome proibido. Tente novamente.")
print("-" *30)