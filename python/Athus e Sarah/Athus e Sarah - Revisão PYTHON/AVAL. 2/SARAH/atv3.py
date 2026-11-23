print("-----Sistema Hospitalar de Unidade de Terapia Intensiva-----")

paciente = input("Nome do Paciente: ").strip()
especialidade = input("Especialidade Médica: ").strip()
crm = input("CRM do Médico: ").strip()
leito = input("Código do Leito: ").strip()
frequencia = input("Frequência Cardíaca: ").strip()
pressao = input("Pressão Sistólica: ").strip()
saturacao = input("Saturação de Oxigênio: ").strip()
temperatura = input("Temperatura Corporal: ").strip()
medicamento = input("Medicamento Prescrito: ").strip()
data = input("Data da Admissão (DD/MM/AAAA): ").strip()
email = input("E-mail do Hospital: ").strip()
status = input("Status Clínico (ESTAVEL): ").strip()

if paciente.isalpha() and \
especialidade.isalpha() and \
medicamento.isalpha() and \
crm.isalnum() and leito.isalnum() and \
frequencia.isdigit() and \
pressao.isdigit() and \
saturacao.isdigit() and \
temperatura.isdigit() and \
len(crm) == 6 and \
email.count("@") and \
email.endswith(".med.br") and \
status == "ESTAVEL":

    print("Paciente registrado!")
else:
    print("Dados inválidos!")

print("-" * 30)