entrada = input('Escreva uma lista de nomes separados e te direi qual o maior nome\n')
lista_palavras = entrada.split()
palavra_mais_longa = max(lista_palavras, key=len)
print('A palavra mais longa é', palavra_mais_longa)