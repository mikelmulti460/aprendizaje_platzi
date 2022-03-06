def es_primo(num):
    
    for i in range(1,num+1):
        if i<num and i>1 and num%i==0:
            return False
    

def main():
    num_final = int(input("ingrese hasta que número quiere calcular: "))
    print(f"Los numeros primos desde el 1 hasta el {num_final} son: \n")
    for i in range(1,num_final+1):
        if es_primo(i)!=False and i!=1:
            print(i)


if __name__ == "__main__":
    main()