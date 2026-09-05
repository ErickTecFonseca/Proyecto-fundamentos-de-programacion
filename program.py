def dolares_a_pesos(dolares):
    return (dolares*19.41)


dolares_a_pesos (1)

def costo_hotel(noches):
    return (noches*185.0)

costo_hotel (1)


def costo_avion(pasajeros):
    return (pasajeros*410.0)

costo_avion (1)

def costo_viaje(noches, pasajeros):
    return dolares_a_pesos(costo_hotel(noches) + costo_avion(pasajeros))



costo_viaje (1, 1)

# pide opción y dependiendo de la opción llama una función diferente
opcion = int(input())     
if(opcion == 1):
    dolares  = float(input())
    print(dolares_a_pesos(dolares))
elif(opcion == 2):
    noches  = int(input())
    print(costo_hotel(noches))
elif(opcion == 3):
    pasajeros  = int(input())
    print(costo_avion(pasajeros))
elif(opcion == 4):
    noches  = int(input())
    pasajeros  = int(input())
    print(costo_viaje(noches,pasajeros))