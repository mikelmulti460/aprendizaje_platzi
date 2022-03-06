def main():
    LIMITE = 100
    contador = 0
    potencia = 0
    while potencia < LIMITE:
        potencia = 2**contador
        print (f"2 elevado a {contador} es: {potencia}\n")
        contador += 1
if __name__ == '__main__':
    main()
