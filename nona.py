entrada = (input('Escreva uma lista de numeros separados e te direi qual o maior nome\n'))
lista_numeros = entrada.split()
lista_numeros = [int(num) for num in lista_numeros]
maior_numero = min(lista_numeros)
print('o menor numero é', maior_numero)