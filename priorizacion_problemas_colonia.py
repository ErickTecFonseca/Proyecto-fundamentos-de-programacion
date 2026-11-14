# Calcula la prioridad de varias colonias para recibir recursos publicos.
 
def pedir_nombre():
    while True:
        nombre = input("Nombre de la colonia: ").strip()
        
        if nombre.replace(" ", "").isalpha():
            return nombre.title()  #Funcion super interesante que hace mayusculas las letras del inicio       
        print("  Usa solo letras y espacios.") 

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
 
 
def obtener_prioridad(puntuacion):
    if puntuacion >= 70:
        return "Alta"
    elif puntuacion >= 40:
        return "Media"
    else:
        return "Baja"
 
 
def main():
   
    matriz = []
    otra = "s"
 
    while otra == "s":
        nombre = pedir_nombre()
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
        prioridad = obtener_prioridad(total)
 
        matriz.append([nombre, total, prioridad])
        otra = input("Registrar otra colonia? (s/n): ").lower()
 
   
    print("\n--- Resultados ---")
    for fila in matriz:
        print(f"Puntuacion de {fila[0]}: {fila[1]:.2f}")
        print(f"Prioridad: {fila[2]}")

 #ramon ramirez estuvo aqui

    mayor = matriz[0]
    for fila in matriz:
        if fila[1] > mayor[1]:
            mayor = fila
 
    print(f"\nColonia con mayor prioridad: {mayor[0]} ({mayor[1]:.2f})")

 
if __name__ == "__main__":
    main()


