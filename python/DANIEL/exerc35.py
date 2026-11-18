for tentativa in range(3):
    print(f"\n--- Reserva de Veículo (Tentativa {tentativa + 1}/3) ---")
    
    cliente = input("Nome do Cliente: ").strip()
    veiculo = input("Modelo do Veiculo (ex: SEDAN): ").strip()
    cor = input("Cor do Veiculo: ").strip()
    cnh = input("CNH (9 caracteres): ").strip()
    dias = input("Quantidade de dias: ").strip()
    seguro = input("Tipo de Seguro: ").strip()

    if veiculo.upper() == "SEDAN" and \
       cor.isalpha() and \
       len(cnh) == 9 and \
       dias.isdigit():

        print("\nSucesso: Reserva de Veiculo de Luxo concluída!")
        break
    else:
        print("\nErro: Verifique se o veiculo é SEDAN, se a cor não tem números e se a CNH tem 9 digitos.")
        print("-" * 40)
else:
    print("\nERRO FATAL: Limite de tentativas excedido. Sistema de reservas bloqueado.")