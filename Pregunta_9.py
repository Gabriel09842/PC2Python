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
def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    cadena_sin_vocales = ''
    for char in cadena:
        if char not in vocales:
            cadena_sin_vocales += char
    return cadena_sin_vocales

texto_ingresado = input("Ingrese una cadena de texto: ")

resultado = omitir_vocales(texto_ingresado)

print(f"Texto original: {texto_ingresado}")
print(f"Texto con vocales omitidas: {resultado}")
