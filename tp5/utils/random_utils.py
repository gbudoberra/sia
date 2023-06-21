def mostrar_progreso(numero):
    if numero < 0 or numero > 100:
        print("El número debe estar entre 1 y 100.")
        return

    completado = int(numero)
    restante = 100 - completado

    # Calcula el porcentaje completado
    porcentaje_completado = completado / 100 * 100

    # Imprime la ilustración de barras
    print("Completado: [{}{}] {}%".format('#' * completado, ' ' * restante, porcentaje_completado))
