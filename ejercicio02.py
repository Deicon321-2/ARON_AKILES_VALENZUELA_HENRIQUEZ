def sistema_gestion_equipos():
    print("Bienvenida ¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Inves-tigación!")
    equipos_disponibles = 20  
    capacidad_maxima_laboratorio = 20
    historial_usos = 0  
    
    opcion_menu = 0
    while opcion_menu != 5:
        print("=== MENÚ PRINCIPAL ===")
        print("1.- Equipos disponibles.")
        print("2.- Asignar equipo.")
        print("3.- Liberar equipo.")
        print("4.- Historial de usos.")
        print("5.- Salir.")
        try:
            opcion_menu = int(input("Ingrese una opción (1-5): "))
        except:
            print("Ha ocurrido un error. Ingrese un número de opción válido.")
            opcion_menu = 0
            continue
        if opcion_menu == 1:
            print(f"Equipos disponibles actualmente: {equipos_disponibles}")
        elif opcion_menu == 2:
            try:
                cantidad_asignar = int(input("Ingrese la cantidad de equipos a asignar: "))
                if cantidad_asignar <= 0:
                    print("Error: La cantidad a asignar no puede ser menor o igual a 0.")
                elif cantidad_asignar > equipos_disponibles:
                    print(f"Error: No hay suficientes equipos disponibles. Disponibles: {equipos_disponibles}")
                else:
                    equipos_disponibles -= cantidad_asignar
                    historial_usos += cantidad_asignar
                    print(f"¡Asignación exitosa! Equipos asignados: {cantidad_asignar}. Disponibles restantes: {equipos_disponibles}")
            except:
                print("Ha ocurrido un error al procesar la asignación.")
        elif opcion_menu == 3:
            try:
                cantidad_liberar = int(input("Ingrese la cantidad de equipos a liberar: "))
                if cantidad_liberar <= 0:
                    print("Error: La cantidad a liberar debe ser mayor a 0.")
                elif (equipos_disponibles + cantidad_liberar) > capacidad_maxima_laboratorio:
                    print(f"Error: Supera la capacidad máxima del laboratorio ({capacidad_maxima_laboratorio} equipos).")
                else:
                    equipos_disponibles += cantidad_liberar
                    historial_usos -= cantidad_liberar
                    if historial_usos < 0:
                        historial_usos = 0
                    print(f"¡Liberación exitosa! Equipos liberados: {cantidad_liberar}. Disponibles actuales: {equipos_disponibles}")
            except:
                print("Ha ocurrido un error al procesar la liberación.")
        elif opcion_menu == 4:
            print(f"Historial de usos: {historial_usos} equipos asignados durante esta sesión.")
        elif opcion_menu == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
        else:
            print("Opción inválida. Por favor, elija una opción comprendida entre 1 y 5.")
sistema_gestion_equipos()
