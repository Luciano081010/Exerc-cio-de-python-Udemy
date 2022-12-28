# Exercicio:
# Peça ao usuario para digitar seu nome:
# Peça ao usuario para digitar sua idade:
# Se nome e idade forem digitados:
# Exiba:
# Seu nome é {nome}
# Seu nome invertido é {nome invertido}
# Se nome contém (ou não) espaços
# Seu nome tem {n} letras
# A primeira letra do seu nome é {letra}
# A  última letra do seu nome é {letra}
# se nada for digitado em nome ou idade:
#     exiba "Desculpa, você deixou campos vazios."

#___________________________________________________________________
#Peça ao usuario para digitar seu nome, sua idade e exibir:

nome = input("Olá, digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é: {nome} e você tem, {idade} anos de idade.')

#___________________________________________________________________
#Seu nome invertido:
    print(f'Seu nome invertido é {nome[::-1]}')
#____________________________________________________________________
#Identificar se seu nome tem ou não tem espaço.
    if ' ' in nome:
        print(f'O nome, {nome} tem espaço.')
    else:
        print(f'O nome {nome}, não tem espaço.')
#___________________________________________________________________
#Quantidade de letras do seu nome:
    print (f'Seu nome contém {len(nome)} letras.')
#___________________________________________________________________
#Identificar a primeira letra do nome:
    print(f'A primeira letra do seu nome é: {nome[0]}')
#____________________________________________________________________
#Identificar a última letra do nome:
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print("Algum campo faltou ser preenchido.")












