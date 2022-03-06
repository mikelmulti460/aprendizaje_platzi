def main():
    palabra = input("Escribe una palabra:").lower().strip()
    palabra2 = palabra.replace(' ', '')
    if palabra2 == palabra2[::-1]:
        print(f"{palabra} es palíndromo")
    else:
        print(f"{palabra} no es palindromo")

if __name__ == '__main__':
    main()