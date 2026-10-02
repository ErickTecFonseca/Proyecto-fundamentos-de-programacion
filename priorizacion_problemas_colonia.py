# El usuario ingresa las diferentes colonias y sus caracteristicas, el programa nos dara un resultado
# de la prioridad que tiene cada colonia para recibir recursos publicos.
# Calcula la prioridad de una colonia para recibir recursos publicos.


def calcular_puntuacion(problemas, gravedad, iluminacion, areas_verdes,
                        habitantes):
    """Regresa la puntuacion total (0 a 100) de la colonia."""
    puntos_infra = problemas * gravedad
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
    nombre = input("Nombre de la colonia: ")
    habitantes = int(input("Numero de habitantes: "))
    problemas = int(input("Numero de problemas de infraestructura: "))
    gravedad = int(input("Gravedad de los problemas (1 a 10): "))
    iluminacion = float(input("Porcentaje de iluminacion (0 a 100): "))
    areas_verdes = float(input("Porcentaje de areas verdes (0 a 100): "))

    if habitantes <= 0 or problemas < 0:
        print("Habitantes o problemas invalidos.")
    elif gravedad < 1 or gravedad > 10:
        print("La gravedad debe estar entre 1 y 10.")
    elif iluminacion < 0 or iluminacion > 100:
        print("La iluminacion debe estar entre 0 y 100.")
    elif areas_verdes < 0 or areas_verdes > 100:
        print("Las areas verdes deben estar entre 0 y 100.")
    else:
        total = calcular_puntuacion(problemas, gravedad, iluminacion,
                                    areas_verdes, habitantes)
        print(f"Puntuacion de {nombre}: {total:.2f}")

        if total >= 70:
            print("Prioridad: Alta")
        elif total >= 40:
            print("Prioridad: Media")
        else:
            print("Prioridad: Baja")
