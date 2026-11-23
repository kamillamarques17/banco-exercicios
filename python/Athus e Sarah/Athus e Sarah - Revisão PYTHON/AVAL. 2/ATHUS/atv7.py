print("-----Sistema de Defesa Cibernética e Monitoramento de SOC-----")

analista = input("Nome do Analista: ").strip()
equipe = input("Equipe de Resposta: ").strip()
incidente = input("Código do Incidente: ").strip()
ip_origem = input("IP de Origem: ").strip()
ip_destino = input("IP de Destino: ").strip()
porta = input("Porta do Protocolo: ").strip()
ameaca = input("Tipo de Ameaça: ").strip()
severidade = input("Severidade Numérica: ").strip()
patch = input("Código do Patch: ").strip()
data = input("Data do Alerta (DD/MM/AAAA): ").strip()
email = input("E-mail do SOC: ").strip()
resposta = input("Resposta ao Incidente (MITIGADO): ").strip()

if analista.isalpha() and \
equipe.isalpha() and \
ameaca.isalpha() and \
incidente.isalnum() and \
patch.isalnum() and \
ip_origem.isalnum() and \
ip_destino.isalnum() and \
porta.isdigit() and \
severidade.isdigit() and \
len(incidente) == 8 and \
email.endswith(".soc.sec") and \
resposta == "MITIGADO":

    print("Incidente mitigado!")
else:
    print("Dados inválidos!")

print("-" * 30)