# *************************
# definicion de funciones
# *************************
#funciones que no reciben parametros
def mostrar_menu():
    print ("1.- Sumar dos numeros.")
    print ("2.- Calcular promedio.")
    opcion = int(input("elige una opcion: "))  
    return opcion

def calcular_promedio(num1, num2, num3):
    print ("calcular promedio")
    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))
    num3 = float(input("ingresa el tercer numero: "))
    promedio = ((num1+num2+num3)/3)
    return promedio



# uso de funciones
opcion = mostrar_menu()


print (f"la opcion elegida es: {opcion}")

print ("-----------------")
mostrar_menu()




#**************************
#uso e funciones 
#**************************


