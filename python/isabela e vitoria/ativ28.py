print("------------------------- RESERVA DE HOSPEDAGEM INTERNACIONAL --------------------------")

hospedagem = input("Digite a sua hospedagem (mais de 3 caracteres): ").strip()
pais = input("Digite o país (mais de 3 caracteres): ").strip()
passaporte = input("Digite o seu passaporte (6 caracteres): ").strip()
quarto = input("Digite o seu quarto (3 caracteres): ").strip()
email = input("Digite o seu email (8 caracteres): ").strip()
codigo_reserva = input("Digite o seu código de reserva (4 caracteres): ").strip()

if len(codigo_reserva) == 4 and codigo_reserva != "0000":

    if (len(hospedagem) > 3 and
        len(pais) > 3 and
        len(passaporte) == 6 and
        len(quarto) == 3 and
        len(email) == 8):

        print(f"Sucesso! Hospedagem: {hospedagem}, País: {pais}, Passaporte: {passaporte}, Quarto: {quarto}, Email: {email}, Código de reserva: {codigo_reserva}")

    else:
        print("Acesso negado, verifique suas respostas")
