print("---Entrega por aplicativo---")

entregador = input("Nome do entregador: ").strip()
veiculo = input("Veículo: ").strip()
codigo = input("Código de entrega: ").strip()
distancia = input("Distância calculada: ").strip()
cidade = input("Cidade: ").strip()
observacao = input("Observações: ").strip()

if (
    len(entregador) > 0 and entregador.isalpha() and \
    len(veiculo) > 3 and veiculo.isalpha() and \
    len(codigo) == 6 and codigo.isdigit() and \
    int(distancia) > 2 and distancia.isdigit() and \
    cidade != "BRASILIA" and cidade.isalpha() and \
    observacao != "nenhuma" and observacao.isalpha()
):
    print("Entrega registrada com sucesso!")

else:
    print("Erro: não foi possível registrar sua entrega")

print("-" * 30)