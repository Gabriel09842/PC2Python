"""Problema 7:
Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no.
"""
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese un número para verificar si es primo: "))

if primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
