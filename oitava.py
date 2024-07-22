entrada = (input('Escreva uma lista de numeros separados e te direi qual o maior nome\n'))
lista_numeros = entrada.split()
lista_numeros = [int(num) for num in lista_numeros]
maior_numero = max(lista_numeros)
print('o maior numero é', maior_numero)