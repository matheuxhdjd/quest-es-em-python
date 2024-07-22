entrada = input('Escreva uma lista de numeros e direi quais são impares\n')
numero = list(map(int, entrada.split()))
impares = [num for num in numero if num % 2 != 0]
print('NUmeros impares', impares)