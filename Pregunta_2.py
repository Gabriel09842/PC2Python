"""
Problema 2:
Escriba un programa en Python para construir el siguiente patrón.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

n = int(input('Ingrese un numero: '))

for i in range(1,n+1):
    print("* "*i)
for i in range(1,n+1):
    print("* "*(n-i))
