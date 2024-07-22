import statistics

entrada = input('Escreva uma lista de numeros espaçados e te darei a media deles\n')
media = entrada.split()
media = list(map(int, entrada.split()))
amedia = statistics.mean(media)
print('A media desses numeros é',amedia)