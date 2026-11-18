print("---sistema de auditoria completo---")
#coletando e tratando os dados
#removi o traço antes de checar o .isalnum() para a lógica funcionar
codigo = input("cód. relatório (ex: REL101):").strip().upper()
data = input("data (DD/MM/AAAA):" ).strip()
email = input("e-mail do auditor").strip().lower()
id_auditor = input("ID númerico do auditor").strip()
status = input("status (digite APROVADO):").strip().upper()

#EXPLICAÇÃO DA LÓGICA
#O .isalnum() verifica se o código contém apenas letras e números (sem símblo ou espaços)
#O .count("/") == 2 verifica se existem exatamente DUS barra na data.
#O .count("@") == 1 verific e existe exatamente UM arroba no e-mail.
# .edswith(".com") garante que o e-mail termine corretamente
# .isdigit() garante que o ID do auditor seja apenas númerico
if codigo.isalnum() and \
data.count("/") == 2 and \
email.count("@") == 1 and email.endswith(".com") and \
id_auditor.isdigit() and \
statu == "APRROVADO":
    
    print(f\n SUCESSO: Auditor {id_auditor}, seu relatório  {codigo} foi enviado!)
          break
          
else:
#exibe o número da tentativa amigável (1, 2 ou 3)
print(f"\nX erro: Dados inválido! Tentativa {tentativa + 1} de 3.")
print("-" * 40)
else:
print("\n BLOQUEADO; Muitas falhas. Procure o Diretor de Segurança.")

""