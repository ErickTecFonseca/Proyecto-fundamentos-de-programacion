# Calcula la prioridad de varias colonias para recibir recursos publicos.


def pedir_numero(mensaje, minimo, maximo, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"  Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("  Escribe un numero valido.")


def calcular_puntuacion(gravedades, iluminacion, areas_verdes, habitantes):
    puntos_infra = sum(gravedades)
    if puntos_infra > 100:
        puntos_infra = 100

    puntos_habitantes = habitantes / 50000 * 100
    if puntos_habitantes > 100:
        puntos_habitantes = 100

    return (puntos_infra * 0.4
            + (100 - iluminacion) * 0.3
            + (100 - areas_verdes) * 0.2
            + puntos_habitantes * 0.1)


def main():
    colonias = []
    otra = "s"

    while otra == "s":
        nombre = input("Nombre de la colonia: ")
        habitantes = pedir_numero("Numero de habitantes: ", 1, 10_000_000, int)
        problemas = pedir_numero(
            "Numero de problemas de infraestructura: ", 0, 100, int)

        gravedades = []
        for i in range(problemas):
            gravedades.append(pedir_numero(
                f"Gravedad del problema {i + 1} (1 a 10): ", 1, 10, int))

        iluminacion = pedir_numero("Porcentaje de iluminacion (0 a 100): ",
                                   0, 100)
        areas_verdes = pedir_numero("Porcentaje de areas verdes (0 a 100): ",
                                    0, 100)

        total = calcular_puntuacion(gravedades, iluminacion, areas_verdes,
                                    habitantes)
        colonias.append([nombre, total])
        otra = input("Registrar otra colonia? (s/n): ").lower()

    for colonia in colonias:
        print(f"Puntuacion de {colonia[0]}: {colonia[1]:.2f}")
        if colonia[1] >= 70:
            print("Prioridad: Alta")
        elif colonia[1] >= 40:
            print("Prioridad: Media")
        else:
            print("Prioridad: Baja")


if __name__ == "__main__":
    main()
