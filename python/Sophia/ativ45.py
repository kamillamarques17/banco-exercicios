print("----------------Prontuário médico de cirurgia robótica----------------")
for tentativa in range(3):
    paciente = input("Paciente?").strip()
    CPF = input("Qual o CPF?: ").strip()
    idade = input("Qual a idade?: ").strip()
    peso = input("Qual o peso?: ").strip()
    médico = input("Digite o médico?: ").strip()
    CRM = input("Qual o CRM?: ").strip()
    robô = input("Qual o robô?: ").strip()
    sala = input("Qual a sala?: ").strip()
    hospital = input("Qual o hospital?: ").strip()
    tipo_sangue = input("Qual o tipo de sangue?: ").strip()
    alergia = input("Tem alguma alergia?: ").strip()
    anestesia = input("Vai ter anestesia?: ").strip()
    batimentos = input("Digite os batimesntos?: ").strip()
    oxigenio = input("Qual o oxigenio?: ").strip()




    if paciente.isalpha() and médico.isalpha() and CRM.isdigit() and \
    CPF.isdigit() and robô == "DA_VINCI" and hospital != "TESTE" and tipo_sangue.isdigit() > 3 and batimentos.isdigit() and \
    oxigenio.isdigit():
       
       print("Cadastro concluido!")
       break
    else:
       print("Erro fatal.")
       print("-" * 30)


else:
   print("Tentativas bloqueadas")

