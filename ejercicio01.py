def sistema_registro_cientificos():
    print("\n--- SISTEMA DE REGISTRO DE CIENTÍFICOS ---")
    cantidad_cientificos = 0
    while cantidad_cientificos <= 0:
        try:
            cantidad_cientificos = int(input("¿Cuántos científicos desea registrar? (Entero positivo): "))
            if cantidad_cientificos <= 0:
                print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
        except:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
            cantidad_cientificos = 0
    total_investigadores_principales = 0
    total_investigadores_asistentes = 0
    for indice in range(1, cantidad_cientificos + 1):
        print(f"\nRegistrando al científico {indice} de {cantidad_cientificos}:")
        id_valido = False
        id_cientifico = ""
        while not id_valido:
            try:
                id_cientifico = input("Ingrese el ID del científico (mínimo 6 caracteres, sin espacios): ")
                if " " in id_cientifico:
                    print("¡Error! El ID no debe incluir espacios.")
                elif len(id_cientifico) <=6 :
                    print("¡Error! El ID debe tener al menos 6 caracteres.")
                else:
                    id_valido = True
            except:
                print("Ocurrió un error al procesar el ID. Intente nuevamente.")
        numero_publicaciones = -1
        while numero_publicaciones < 0:
            try:
                numero_publicaciones = int(input("Ingrese el número de publicaciones: "))
                if numero_publicaciones < 0:
                    print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
            except:
                print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
                numero_publicaciones = -1

        # Clasificación del científico según las publicaciones
        if numero_publicaciones > 10:
            total_investigadores_principales += 1
            print("Clasificado como: Investigador Principal")
        else:
            total_investigadores_asistentes += 1
            print("Clasificado como: Investigador Asistente")

    # Resumen final de la clasificación
    print(f"¡El instituto cuenta con {total_investigadores_principales} Investigadores Principales y {total_investigadores_asistentes} Investigadores Asistentes! ¡Ciencia en marcha!")
sistema_registro_cientificos()