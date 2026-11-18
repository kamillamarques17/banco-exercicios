funcionarios =["adm","gerente","suporte"]
for usuario in funcionarios:
    senha=input(f"Olá {usuario}, digite a senha de acesso")
    if senha=="Messimelhordomundo":
        print(f"login efetuado! Bem vindo, {usuario}.")
    else:
        print(f"Acesso Negado! {usuario} digitou a senha errada.")
    
    #O for é uma palavra reservada que sinaliza o início de um ciclo. Ele diz ao computador:
    #"Prepare-se, pois vamos repetir as instruções que vêm logo abaixo para um grupo de coisas."
    
    #usuario (A variável Temporária): Este nome você inventa. Pense nela como uma caixa vazia que o python vai usar para carregar o nome de
    #in funcionarios (A origem): Aqui vicê indica o python tem que buscar os dados. FUncionarios é o nome da sua lista original que contém os três cargos.
    
    #O Python não entende o significado das palavras (ele não sabe o que é um "usuario" ou um "gerente"),
    # ele apenas segue a regra:
    # "Pegue o próximo item da lista e coloque dentro deste nome que eu inventei".
    #funcionarios (O Nome da lista): É o nome que você deu para esse grupo. É como o rótulo da pasta.