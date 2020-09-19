import os # Importa la libreria os
os.system('cls') # Hace el llamado para cls "limpiar la pantalla"
agenda = {} # Diccionario 
while True: # creacion de menu, se crean print para cada opcion del menu
    print("------Bienvenido al menu de opciones------")
    print("\n")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción:")) # Primera opcion del menu
    if opcion == 1: # Cuando seleccionan la opcion 1
        nombre = input("Digite el nombre del funcionario:")  # Solicita el nombre del funcionario
        if nombre in agenda: # Analiza si el nombre ingresado esta en el diccionario
            print("%s ya existe su numero de cedula es: %s" % (nombre,agenda[nombre])) # Manda un mensaje de que el funcionario ya existe y muestra su cedula
            print("%s ya existe su cargo es: %s" % (nombre,agenda[nombre])) 
            print("%s ya existe su salario es: %s" % (nombre,agenda[nombre])) 
            opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar.") # Manda un mensaje que solicita si desea modificar el funcionario existente
            if opcion == "s": # Opcion de cambiar la cedula del funcionario
                cedula = input("Digite su nuevo número de cedula:") # Solicita el nuevo numero de cedula
                agenda[nombre]=cedula # Agrega el nuevo numero de cedula al diccionario
        else:
            # Solicitar los datos del nuevo funcionario a ingresar y los guarda en el diccionario
            cedula = input("Digite su número de cedula:") # Solicita la cedula del funcionario
            agenda[nombre]=cedula # Agrega la cedula al diccionario
            cargo = input("Digite su cargo en la empresa:") 
            agenda[nombre]=cargo 
            salario = input("Digite su salario:") 
            agenda[nombre]=salario 
        os.system('cls') # limpia la pantalla

    elif opcion == 2:
        cadena = input("Digite el nombre del funcionario a buscar:") 
        for nombre, cedula in agenda.items():
            if nombre.startswith(cadena):
                print("El número de cedula de %s es el %s" % (nombre,agenda[nombre]))
                print("El cargo de %s es el %s" % (nombre,agenda[nombre]))
                print("El  salario de %s es el %s" % (nombre,agenda[nombre]))
            else:
              print("El nombre del funcionario no existe")


    elif opcion == 3:
        nombre = input("Digite el nombre del funcionario a borrar:")    
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto")

    elif opcion == 4:
        for nombre, cedula in agenda.items():
            print(nombre,"->",cedula)


    # la opcion 5 para salir del programa
    elif opcion == 5:
        os.system('cls')
        break
    else:
        print("Opción incorrecta")   