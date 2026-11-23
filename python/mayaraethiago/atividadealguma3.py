print("-----Sistema de Acesso Seguro ao Servidor de Dados-----")

for tentativa in range (5):
    adm = input ("Nome do Administrador: ").strip()
    cargo = input ("Cargo do Usúrio: ").strip()
    servidor = input("Código do Servidor: ").strip()
    IP = input ("IP do terminal: ").strip()
    rede = input ("Porta de rede: ").strip()
    setor = input ("Setor responsável: ").strip()
    protocolo = input ("Protocolo de rede: ").strip()
    senha = input ("Sua senha provisória: ").strip()
    dominio = input ("Domínio Corporativo: ").strip()
    segurança = input ("Confirmação de segurança (digite: LIBERADO): ").strip()

    if servidor.isalnum() and protocolo.isalnum() and \
    rede.isdigit() and IP.isdigit() and cargo.isalpha() and \
    setor.isalpha() and dominio.endswith(".org") and \
    len (senha) < 8 and \
    segurança == "LIBERADO":

           print(
             f"\nSUCESSO: administrador {adm}, "
             f"confirmação liberada {segurança} liberado"
           )
           break
    else: 
          print(
                "\nERRO: senha inválida, tentativa {tentativa + 1} de 5")
          print("-" * 40)

else:
      print(
            "\nBLOQUEADO: limite de 5 tentativas excedido. "
            "Procure o suporte da corretora."
      )
     