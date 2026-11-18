print("---- SISTEMA DE SEGURANÇA DO BANCO CENTRAL ----")

for tentativa in range(3):

    gerente = input("Digite o nome do gerente : ").strip()
    cidade = input("Digite a cidade: ").strip()
    cpf = input("Digite o CPF:(NUMERO) ").strip()
    agencia = input("Digite a agência:(NUMERO) ").strip()
    conta = input("Digite a conta:(NUMERO) ").strip()
    nivel = input("Digite o nível (diretor): ").strip().upper()
    senha = input("Digite a senha (nao pode ser 123): ").strip()
    chave = input("Digite a chave de acesso (ALPHA): ").strip().upper()

    if gerente.isalpha() and cidade.isalpha() and \
       cpf.isdigit() and agencia.isdigit() and \
       conta.isdigit() and nivel == "DIRETOR" and \
       senha != "123" and chave == "ALPHA":

        print(f"Acesso liberado! Bem-vindo ao sistema, {gerente}.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO. Alerta de invasão enviado à segurança.")

