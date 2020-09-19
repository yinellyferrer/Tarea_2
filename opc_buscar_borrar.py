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