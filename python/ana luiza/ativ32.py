print('----- Matricula de aluno em Universidade-----')
for tentativa in range (3):
    nome = input ("Nome do aluno:").strip()
    curso =input ("curso (apenas letras):").strip()
    matricula = input ("nº matricula (6 numeros):").strip()
    ano = input ("ano de ingresso (4 numeros):").strip()
    campus = input (" campus (digite CENTRAL):").strip()
    senha= input ("crie uma senha:").strip()

    if nome.isalpha() and curso.isalpha() and \
       len(matricula)== 6 and matricula.isdigit() and\
       len(ano)== 4 and ano.isdigit()and\
       campus == "CENTRAL" and senha != "123456":
        
        print("Matrícula realizada com sucesso!")
        break
    else:
        print("Erro: Verifique os dados.")
else: 
    print("Muitas tentativas. Procure a secretaria.")
print("-"*42)