funcionarios = ["adm","gerente","suporte"]
for usuario in funcionarios:
    senha=input(f"olá {usuario},digite a senha de acesso:")
if senha=="python123":
   print(f"login efetuado!bem-vindo,{usuario}.")
else:
    print (f"acesso negado!{usuario} digitou a senha errada!")

# O for  é uma palavra reservada que sinaliza o início de um ciclo. Ele diz ao computador:
#"Prepare-se, pois vamos repetir as intruções que vem logo abaixo para um grupo de coisas".

#usuario (A Variável Temporária): Este nome você inventa. Pense nela coomo uma caixinha vazia que  python vai usar para carregar o nome de uma vez
#in funcionarios (A origem): Aqui você indica o python deve buscar os dados. Funcionarios é o nome da sua lista original que contém os três cargos.

#O python não entende o significado das palavras (ele não sabe o que é um "usuario" ou um "gerente"), pegue o proximo item da lista e  coloque dentro deste nome que eu inventei".
#Funiconarios (O nome da Lista): É o nome que você deu para esse grupo. É como o rótulo da pasta
