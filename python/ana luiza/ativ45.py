print("---------Prontuārio mdico de cirurgia robótica----------")
for tentativa in range(3):
    paciente = input("Paciente?").strip()
    CPF = input("Qual o CPF?: ").strip()
    idade =input("Qual a idade?: ").strip()
    peso = input("Qual o peso?: ").strip()
    médico = input("Digite o médico?: ").strip()
    CRH = input("Qual CRH?: ").strip() 
    robô = input("Qual robô?: ").strip()
    sala = input("Qual a sala?: ").strip()
    hospital = input("Qual O hospital?: ").strip()
    tipo_sangue = input ("Qual O tipo de sangue?:")
    alergia = input("Tem alguma alergia?: ").strip()
    anestesia = input("Vai ter anestesia?: ").strip()
    batimentos = input("Digite OS batimentos?: ").strip()
    oxigenio = input("Qual oxigenio?: ").strip()
    if paciente.isalpha() and médico.isalpha() and CRH.isdigit() and \
 CPF.isdigit() and robô == "DA_VINCI" and hospital != "TESTE" and tipo_sangue.isdigit() > 3 and batimentos.isdigit() and \
oxigenio.isdigit():
     
     print("Cadastro concluido!")  

    else:

     print("Erro fatal.") 
     print("-"* 20)
else:
  print("Tentativas bloqueadas")