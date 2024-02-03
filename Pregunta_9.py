"""Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?
"""
def quitar_vocales(cadena):
    resultado = ""

    for i in cadena:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += i
    return resultado

input = input("Ingrese una cadena de texto: ")
sin_vocales = quitar_vocales(input)

print(f"Texto original: {input}")
print(f"Texto sin vocales: {sin_vocales}")