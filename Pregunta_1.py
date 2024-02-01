"""Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""
cadena = []
print('Los numeros que son divisibles por 7 y múltiplos de 5, en el rango de 1500 y 2700 son:')
for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        cadena.append(numero)
print(cadena)