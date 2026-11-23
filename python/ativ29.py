print("--------------Prontuário médio--------------")

paciente= input ("Qual o su nome?: ")
médico = input ("Qual o nome do médico?: ")
hospital = input("Informe o nome do hospital: ")
crm = input("Digite o CRM: ")
ala = input ("Digite a ala em que se encontra: ")
sintomas = input("Digite os sintomas: ")

if len(paciente) == 4 and len(médico) == 4 and len(hospital) == 4 and len(crm) == 5 and(ala) == 2 and (sintomas) !="NADA":
      print(f'Olá, {paciente} você esta no hospital {hospital} se consultando com o {médico}, sua ala é {ala}, o crm é :{crm} seus sintomas são {sintomas}');

else:
      print('Não foi possivel identificar o seu problema...')
print("-"*42)


