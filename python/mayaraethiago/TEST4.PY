funcionarios = ["Admin", "Gerente", "Suporte"]

for usuario in funcionarios:

 senha = input(f"Olá {usuario}, digite a senha de acesso: ")

if senha == "python123":
 print(f"Login efetuado! Bem-vindo(a), {usuario}.")
else:
 print(f"Acesso Negado! {usuario} digitou a senha errada.")

#O for é uma palavra reservada que sinaliza o inicio de um ciclo. Ele diz ao computador:
#"Prepare-se, pois vamos repetir as instruções que vêm logo abaixo para um grupo de coisas".

#usuario (A Variável Temporária): Este nome você inventa. Pense nela como uma caixinha vazia que o
#Python vai usar para carregar um nome de cada vez.

#in funcionarios (A Origem): Aqui você indica onde o Python deve buscar os dados, funcionarios
#é o nome da sua lista original que contém os três cargos.

#O Python não entende o significado das palavras (ele não sabe o que é um "usuario" ou um "gerente"),
#ele apenas segue a regra:
#"Pegue o próximo item da lista e coloque dentro deste nome que eu inventei".

#funcionarios (O Nome da Lista): É o nome que você deu para esse grupo. É como o rótulo da pasta.






