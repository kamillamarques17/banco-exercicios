funcionarios = ["Admin", "Gerente", "Suporte"]

for usuario in funcionarios:

    senha = input("olá {usuario}, digite a senha de acesso:")

    if senha == "python123":
        print(f"Login efetuado! Bem-vindo(a), {usuario}.")
    else: 
        print(f"Acesso negado! {usuario} digitou a senha errada.")


#O for é uma palavra reservada que sinaliza o início de um ciclo. Ele diz ao computador:
# "Prepara-se, pois vamos repetir as instrções que vêm logo abaixo para um grupo de coisas".

#usuário (A Variável Temporaria): Este nome você enventa. Pense nela como uma caixinha vazia que o Python 
#vai usar para carregar um nome da cada vez.
#in funcionarios (A origem): Aqui você indica onde o Python deve buscar os dados, funcionarios
# é o nome da sua lista original que contém o três cargos.

#O Python não entende o significado das palavras (ele não sabe o que é um "usuário" ou um"gerente"),
#ele apenas segue a regra:
# "Pegue o proxímo item da lista e coloque dentro deste nome que eu inventei".
#funcionarios ( O nome da lista): É o nome que você deu para esse grupo. É como o rótulo da pasta.   
