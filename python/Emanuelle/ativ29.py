print("--------------------Prontuário Médico Simples---------------------")
Paciente = input("Digite o nome do pacinte:").strip() 
Médico = input("Digite o nome do médico:").strip() 
CRM = input("DIgite o CRM:").strip()
Hospital = input("Digite o hospital:").strip()
Ala = input("Digite a ala:").strip()
Sintoma = input("Digite o sintoma:").strip()
if len(Paciente) >4 and len(Médico) >4 and len(CRM) ==5 and len(Hospital) >4 and len(Ala) ==2 and len(Sintoma):
    print("Prontuário Médico Simples")
else:
    print("Prontuário feito!")