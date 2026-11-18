print("------------------------- MATRÍCULA DE VEÍCULO PESADO--------------------------")

propietário= input("Digite o propietário(mais de 2 caracteres): ").strip()
modelo = input("Digite o modelo ( mais de  2 caracteres): ").strip()
placa = input("Digite a placa (7 caracteres): ").strip()
chassi = input("Digite a chassi (10 caracteres): ").strip()
cor = input("Digite a cor ( mais de 2 caracteres): ").strip()
ano = input("Digite o ano (4 caracteres): ").strip()

if len(ano) == 4 and ano != "2000":

    if (len(propietário) > 2 and
        len(modelo) > 2 and
        len(placa) == 7 and
        len(chassi) ==10 and
        len(ano)  ==4 and
        len(cor) > 2):

        print(f"Sucesso! propietário: {propietário}, modelo: {modelo}, placa: {placa}, chassi: {chassi}, cor: {cor}, ano: {ano} são esses")
    else:   
        print("Acesso negado, verifique suas respostas")
