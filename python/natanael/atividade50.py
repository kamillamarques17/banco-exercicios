print("------------Registro de Aeronave Executiva-------------")
modelo = input("Modelo da Aeronave:")
prefixo = input("Prefixo da Aeronave (Ex: PR-ABC):").strip()
Fabricante = input("Fabricante da Aeronave:").strip()
Ano = input("Ano de Fabricação da Aeronave:").strip()
Horas = input("Horas de Voo da Aeronave:").strip()
Piloto = input("Nome do Piloto Responsável:").strip()
CPF = input("CPF do Piloto (somente números):").strip()
email = input("DIgite seu E-mail").strip()
Base = input("Digite a base de operações da aeronave:").strip()
Cidade = input("Digite a cidade onde a aeronave está registrada:").strip()
UF = input("Digite a UF onde a aeronave está registrada:").strip()
Carga = input("Digite a carga máxima da aeronave:").strip()
Tanque = input("Digite a capacidade do tanque de combustível da aeronave:").strip()
Torre = input("Digite o nome da torre de controle responsável pela aeronave:").strip()
Termos = input("Aceita os termos de segurança? (Digite SIM para aceitar):").strip()
if Fabricante.isalpha() and Piloto.isalpha() and Ano.isdigit() and Horas.isdigit() and\
    CPF.isdigit() and Carga.isdigit() and Tanque.isdigit() and modelo.isupper() and\
        Base.isupper() and UF.isupper() and Torre.isupper() and prefixo.isalnum() and Termos== "SIM" and\
            email.count("@") == 1 and email.endswith(".com"):
            print(f"Sucesso: A aeronave {modelo} com prefixo {prefixo} foi registrada com sucesso!")
else:    
    print("Erro: Dados inválidos. O registro da aeronave falhou.")