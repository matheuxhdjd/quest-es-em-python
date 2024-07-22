def main():

    entrada = input("Digite uma lista de números separados por espaço: ")

    lista_numeros = entrada.split()

    numeros = []
    for numero in lista_numeros:
        try:
            numeros.append(float(numero))
        except ValueError:
            print(f"'{numero}' não é um número válido e será ignorado.")

    soma = sum(numeros)
    

    print("A soma dos números é:", soma)

if __name__ == "__main__":
    main()
