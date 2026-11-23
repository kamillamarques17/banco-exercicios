print("-----Automação Industrial e Supervisório de Usina Hidrelétrica-----")

operador = input("Nome do Operador: ").strip()
turno = input("Turno de Trabalho: ").strip()
turbina = input("Sigla da Turbina: ").strip()
gerador = input("Código do Gerador: ").strip()
rpm = input("Rotação (RPM): ").strip()
represa = input("Nível da Represa: ").strip()
vazao = input("Vazão da Água: ").strip()
temperatura = input("Temperatura dos Mancais: ").strip()
sala = input("Sala de Comando: ").strip()
data = input("Data da Leitura (DD/MM/AAAA): ").strip()
email = input("E-mail da Usina: ").strip()
alarme = input("Alarme Geral (NORMAL): ").strip()

if operador.isalpha() and \
turno.isalpha() and \
sala.isalpha() and \
turbina.isalnum() and \
gerador.isalnum() and \
rpm.isdigit() and \
represa.isdigit() and \
vazao.isdigit() and \
temperatura.isdigit() and \
len(data) == 10 and \
email.endswith(".energia.ind.br") and \
alarme == "NORMAL":

    print("Sistema normal!")
else:
    print("Dados inválidos!")

print("-" * 30)