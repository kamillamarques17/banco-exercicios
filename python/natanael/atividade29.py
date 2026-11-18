print("-------------------------------Prontuário Médico Simples-----------------------------------------")
paciente = input("digite o nome do paciente:").strip()
médico = input("Digite o nome do médico:").strip()
CRM = input("Digite o CRM:").strip()
hospital = input("digite o hospital:").strip()
ala = input("digite a ala:").strip()
sintoma = input("digite o sintoma:").strip()
if len(paciente) >4 and len(médico) >4 and len(CRM) ==5 and len(hospital) >4 and len(ala) ==2 and len (sintoma):
    print("Prontuário Médico Simples")
else:
    print("Prontuário feito!")