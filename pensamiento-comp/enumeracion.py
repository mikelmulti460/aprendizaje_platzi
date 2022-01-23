objetivo = int(input("Escribe un entero: "))
aprox = objetivo*0.8
respuesta = (objetivo/(2*(aprox))+((aprox/2)/2))
iteraciones = 200
i=0

while i <= iteraciones:
    respuesta = (objetivo/(2*(respuesta))+((respuesta)/2))
    print(respuesta)
    i+=1

print (respuesta)
