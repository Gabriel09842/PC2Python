"""Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.
"""

def fibonacci(n):
    resultado = []
    a = 0
    b = 1
    while a <= n:
        resultado.append(a)
        a, b = b, a + b
    return resultado

print("Serie fibonacci entre el numero 0 y 50:")
print(fibonacci(50))
