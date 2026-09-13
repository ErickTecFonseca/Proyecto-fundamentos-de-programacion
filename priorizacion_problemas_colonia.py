# El usuario ingresa las diferentes colonias y sus caracteristicas, el programa nos dara un resultado
# de la prioridad que tiene cada colonia para recibir recursos publicos.
def pedir_datos_colonia():
    """Solicita al usuario los datos de una colonia y los regresa."""
    nombre_de_la_colonia = input("ingrese el nombre de la colonia: ")
    numero_de_habitantes = int(input("ingrese el numero de habitantes: "))
    numero_de_problemas_infraestructura = int(input("ingrese el numero de problemas de infraestructura: "))
    gravedad_infraestructura = int(input("ingrese la gravedad de los problemas en una escala del 1 al 10 siendo 1 poco grave y 10 muy grave: "))
    porcentaje_iluminacion = float(input("ingrese el porcentaje que cree que tiene de iluminacion en la colonia: "))
    porcentaje_areas_verdes = float(input("ingrese el porcentaje que cree que tiene de areas verdes en la colonia: "))

    return {
        "nombre": nombre_de_la_colonia,
        "habitantes": numero_de_habitantes,
        "numero_problemas_infra": numero_de_problemas_infraestructura,
        "gravedad_infra": gravedad_infraestructura,
        "porcentaje_iluminacion": porcentaje_iluminacion,
        "porcentaje_areas_verdes": porcentaje_areas_verdes,
    }


def calcular_puntuacion_infraestructura(numero_de_problemas, gravedad):
    """Peso 40%. Mas problemas y mayor gravedad = mayor puntuacion."""
    return (numero_de_problemas * gravedad) * 0.4


def calcular_puntuacion_iluminacion(porcentaje_iluminacion):
    """Peso 30%. Menos iluminacion = mayor puntuacion (se invierte el porcentaje)."""
    return (100 - porcentaje_iluminacion) * 0.3


def calcular_puntuacion_areas_verdes(porcentaje_areas_verdes):
    """Peso 20%. Menos areas verdes = mayor puntuacion (se invierte el porcentaje)."""
    return (100 - porcentaje_areas_verdes) * 0.2


def calcular_puntuacion_habitantes(numero_de_habitantes, habitantes_referencia=50000):
    """
    Peso 10%. Mas habitantes afectados = mayor puntuacion.
    Se normaliza contra un numero de referencia (ajustable) para obtener un porcentaje 0-100,
    y se limita a 100 por si la colonia supera ese numero de referencia.
    """
    porcentaje_habitantes = min((numero_de_habitantes / habitantes_referencia) * 100, 100)
    return porcentaje_habitantes * 0.1


def calcular_prioridad_total(puntuacion_infra, puntuacion_iluminacion, puntuacion_areas_verdes, puntuacion_habitantes):
    """Suma las cuatro puntuaciones ponderadas."""
    return puntuacion_infra + puntuacion_iluminacion + puntuacion_areas_verdes + puntuacion_habitantes


def clasificar_prioridad(puntuacion_total):
    """Clasifica la puntuacion final en una categoria de prioridad."""
    if puntuacion_total >= 70:
        return "Alta"
    elif puntuacion_total >= 40:
        return "Media"
    else:
        return "Baja"


def mostrar_resultado(nombre_colonia, puntuacion_infra, puntuacion_iluminacion, puntuacion_areas_verdes, puntuacion_habitantes, puntuacion_total):
    """Imprime el desglose y el resultado final de la colonia."""
    print(f"\n--- Resultado para la colonia: {nombre_colonia} ---")
    print(f"Puntuacion de infraestructura: {puntuacion_infra:.2f}")
    print(f"Puntuacion de iluminacion: {puntuacion_iluminacion:.2f}")
    print(f"Puntuacion de areas verdes: {puntuacion_areas_verdes:.2f}")
    print(f"Puntuacion de habitantes: {puntuacion_habitantes:.2f}")
    print(f"Puntuacion total de prioridad: {puntuacion_total:.2f}")
    print(f"Nivel de prioridad: {clasificar_prioridad(puntuacion_total)}")


def main():
    datos = pedir_datos_colonia()

    puntuacion_infra = calcular_puntuacion_infraestructura(
        datos["numero_problemas_infra"], datos["gravedad_infra"]
    )
    puntuacion_iluminacion = calcular_puntuacion_iluminacion(datos["porcentaje_iluminacion"])
    puntuacion_areas_verdes = calcular_puntuacion_areas_verdes(datos["porcentaje_areas_verdes"])
    puntuacion_habitantes = calcular_puntuacion_habitantes(datos["habitantes"])

    puntuacion_total = calcular_prioridad_total(
        puntuacion_infra, puntuacion_iluminacion, puntuacion_areas_verdes, puntuacion_habitantes
    )

    mostrar_resultado(
        datos["nombre"], puntuacion_infra, puntuacion_iluminacion,
        puntuacion_areas_verdes, puntuacion_habitantes, puntuacion_total
    )


if __name__ == "__main__":
    main()
