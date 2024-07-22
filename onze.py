entrada = input('Escreva uma lista de numeros e direi quais são pares\n')
numero = list(map(int, entrada.split()))
pares = [num for num in numero if num % 2 == 0]
print('NUmeros pares', pares)