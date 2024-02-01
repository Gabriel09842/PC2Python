"""
Problema 5:
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count.
"""
def contar(numero, digito):
    nCadena = str(numero)
    cantidad = nCadena.count(str(digito))
    return cantidad

num = int(input("Ingrese un numero: "))
digito = int(input("Ingrese el digito que desea verificar la cantidad: "))

cantidad_veces = contar(num, digito)

print(f"Número ingresado: {num} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {cantidad_veces}")
