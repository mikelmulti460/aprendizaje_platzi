texto = """
Bienvenido a la app para calcular cambio de monedas a dólares!
Eija una opción:
1) Soles
2) Pesos Mexicanos
3) Pesos Argentinos

"""
def cambiarMoneda(moneda,tc):
    cantidad = float(input(f"¿Cuántos {moneda} quieres cambiar?: "))
    
    dolares = cantidad/tc
    print(f'El cambio por {cantidad} {moneda} es: ${round(dolares,2)} dólares')


moneda = int(input(texto))
if moneda == 1:
    moneda = "Soles"
    tc = 3.82
    cambiarMoneda(moneda, tc)
elif moneda==2:
    tc = 25.54
    moneda = "Pesos Mexicanos"
    cambiarMoneda(moneda, tc)
elif moneda==3:
    tc = 50.58
    moneda = "Pesos Argentinos"
    cambiarMoneda(moneda, tc)
else:
    print("opción incorrecta, el programa se cerrará")

