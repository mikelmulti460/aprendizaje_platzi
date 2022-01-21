palabra = input("Escribe una palabra:")

if palabra == palabra[::-1]:
    print(f"{palabra}Es palíndromo")
else:
    print("no es palindromo")
