print("----------------------------Sistema de hotel-----------------------------")
hospede = input("Digite o nome do hospede: ").strip()
pais = input("Digite seu pais ( Deve conter mais de 3 letras): ").strip()
passaporte = input("Digite seu Passaporte (Deve conter exatamente 6 caracteres) :")
Data = input("Digite a data (Deve conter exatamente 8 letras) :")
codigo = input("Digite seu codigo (Deve ser diferente de 0000) :")
quarto = input("Digite o numero do seu quarto (Deve conter exatamente 3 numeros) :")

if len(hospede) and len(pais) == 3 and len(passaporte) > 6 and len(quarto) == 3 and len(Data) == 8 and len(codigo) !="0000":
    print(f"O nome do hospede e {hospede}, Seu pais e {pais}, Seu passaporte e {passaporte}, a data e {Data}, seu turno e {codigo}, seu quarto e {quarto}")
else:
    print("nome do hospede, data, passaporte, pais, codigo e quarto esta incorreto(a)!. Tente novamente mais tarde")