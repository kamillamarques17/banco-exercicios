print ("------Sistema Hospitalar------")

for tentatiava in range(5): 
    nome = input("nome do paciente: ").strip()
    especialidade = input("especialidade médica: ").strip()
    CRM = input("CRM do médico: ").strip()
    leito = input("Código do leito: ").strip()
    cardíaca = input("frequência cardíaca: ").strip()
    pressão = input("Pressão sistólica: ").strip()
    saturação = input("Saturação de oxigênio: ").strip()
    corporal = input("Temperatura corporal: ").strip()
    prescrito = input("Medicamento prescrito: ").strip()
    data = ("DD/MM/AAAA").strip()
    email = input("E-mail do hospital: ").strip()
    status = input("ESTÁVEL").strip()

    if nome.isalpha() and especialidade.isalpha() and prescrito.isalpha() and\
    CRM.isalnum() and leito.isalnum() and cardíaca.isdigit() and pressão.isdigit() and\
    saturação.isdigit() and corporal.isdigit() and len(cardíaca) == 6 and email.endswith(".med.br") and\
    status == "ESTÁVEL":

          print(
                 f"\nSUCESSO: sistema {nome}, "
                 f"cadastro {status} registrado"
            )
    break
          
else:
        print(f"\nERRO: cadastros inválidos, Tentativa {+ 1}de 5")
        print("-" * 40) 
          
