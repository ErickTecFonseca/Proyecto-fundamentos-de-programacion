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
    nombres = []          
    puntuaciones = []     
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
        nombres.append(nombre)        
        puntuaciones.append(total)     
        otra = input("Registrar otra colonia? (s/n): ").lower()

    for i in range(len(nombres)):     
        print(f"Puntuacion de {nombres[i]}: {puntuaciones[i]:.2f}")
        if puntuaciones[i] >= 70:
            print("Prioridad: Alta")
        elif puntuaciones[i] >= 40:
            print("Prioridad: Media")
        else:
            print("Prioridad: Baja")

    mayor = puntuaciones.index(max(puntuaciones))
    print(f"\nColonia con mayor prioridad: {nombres[mayor]} "
          f"({puntuaciones[mayor]:.2f})")


if __name__ == "__main__":
    main()
