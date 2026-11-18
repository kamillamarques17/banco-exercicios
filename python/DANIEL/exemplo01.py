for tentativa in range(3):
  nome = input("Nome: ").strip()
  sobrenome = input("Sobrenome: ").strip()
  cpf = input("CPF (11 números): ").strip()
  agencia = input("Agência (4 números): ").strip()
  senha = input("Senha (6 digitos): ").strip()
  pix = input("Chave Pix: ").strip()
  #\-> Ponte para quebrar a linha
  #.isdigit() -> Garante que idade e carteirinha sejam números
  # == -> Exige que o plano seja exatamente OURO
  #!= -> Proibe que o código do médico seja 000
  # .isalpha() -> 0 setor não pode ter números

  if len(nome) > 2 and len(sobrenome) > 2 and \
    len(cpf) == 11 and cpf.isdigit() and \
    len(agencia) == 4 and agencia.isdigit() and \
    len(senha) == 6 and pix != "TESTE":
   
   print("Conta aberta com sucesso! Bem-vindo ao banco.")
   break
  else:
   print("Erro: Verifique se CPF e Agência são apenas números e se os tamanhos estão corretos.")
   print("-"* 30)
else:
   print("Muitas tentativas falhas. Procure uma agência física.")