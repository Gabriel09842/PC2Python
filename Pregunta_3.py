"""
Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
"""
numPares = []
numImpares = []

while True:
    ingreso = input('Desea ingresar un número?: ')
    if ingreso.lower() == 'no':
        break
    if ingreso.lower() == 'si':
        numero = int(input('Ingrese el número:'))
        if numero%2 == 0:
            numPares.append(numero)
        else:
            numImpares.append(numero)
    else:
        print('Ingrese una respuesta válida')
        
print("Números ingresados: ", numPares + numImpares)
print(f"Números pares: {len(numPares)}")
print(f"Números impares: {len(numImpares)}")