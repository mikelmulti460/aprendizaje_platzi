
def factorial(n):
    """calcula el factorial de n
    int n > 0 
    returns n!
    """
    print(n)
    if n ==1:
        return 1
    
    return n * factorial(n-1)

def main():
    n = int(input("Ingresa un número entero: "))
    print(factorial(n))
    

if __name__ == "__main__":
    main()