"""Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento."""
def factorial(numero):
    if numero < 0:
        return "Ingrese un número positivo"
    elif numero == 0 or numero == 1:
        return 1
    else:
        acumular = 1
        for i in range(2, numero + 1):
            acumular *= i
        return acumular

num = int(input("Ingrese un número entero: "))

resultado = factorial(num)

print(f"El factorial de {num} es: {resultado}")
