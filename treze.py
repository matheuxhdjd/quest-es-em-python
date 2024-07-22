entrada = (input('Escreva uma lista de nomes separados e te direi quais começam com a letra "A" \n'))
nomes = entrada.split()
nomes_comeca_com_A = [nome for nome in nomes if nome.startswith('A') or nome.startswith('a')]
print("OS nomes que começam com A são", nomes_comeca_com_A)