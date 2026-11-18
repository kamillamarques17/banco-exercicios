print('-----Prontuário Médico Simples-----')
nome = input ("Qual seu nome? ")
medico = input ("Qual o nome do médico responsável? ")
crm = input ("Qual o CRM do médico responsável? ")
hospital = input("Qual o nome do hospital? ")
ala = input("Qual a ala do hospital? ")
sintoma = input("Qual(is) seu(s) sintoma(s)? ")
if len(nome) > 4 and len(medico) > 4 and len(crm) == 5 and len(hospital) > 4 and len(ala) == 2 and sintoma != "Nada":
        print(f"Pronto! Seus dados foram registrados.")
else:
    print("Falha nos dados. Tente novamente.")
print('-'*42)