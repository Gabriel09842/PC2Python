"""Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad.
"""

listaAlumnos = []

num = int(input("Ingrese el número de alumnos: "))

for _ in range(num):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []

    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i+1} para {nombre}: "))
        notas.append(calificacion)

    alumno = {"Alumno": nombre, 
              "Notas": notas}
    listaAlumnos.append(alumno)
print("""---------------------------------------
Lista de alumnos:
""")
for alumno in listaAlumnos:
    print(f"Alumno: {alumno['Alumno']},\nNotas: {alumno['Notas']}\n")
