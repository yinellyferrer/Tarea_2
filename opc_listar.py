# la opcion cuatro es la que vamos hacer 

    elif opcion == 4:
        for nombre, cedula in agenda.items():
            print(nombre,"->",cedula)


    # la opcion 5 para salir del programa
    elif opcion == 5:
        os.system('cls')
        break
    else:
        print("Opción incorrecta")         