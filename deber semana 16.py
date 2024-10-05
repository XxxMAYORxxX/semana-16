# Abrir el archivo en modo de escritura (w) para crear el archivo y escribir en él
with open("my_notes.txt", "w") as file:
    # Escribir tres líneas de notas personales
    file.write("Primera nota: Estudiar Python para mejorar mis habilidades.\n")
    file.write("Segunda nota: Practicar la programación todos los días.\n")
    file.write("Tercera nota: Completar todos los proyectos de la universidad.\n")

# Abrir el archivo en modo de lectura (r)
with open("my_notes.txt", "r") as file:
    # Leer el contenido línea por línea
    for line in file:
        # Mostrar cada línea en la consola
        print(line, end="")  # Utilizamos end="" para evitar dobles saltos de línea
