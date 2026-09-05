# 01_variable = 10 #Nombre no valido
_variable = 10 #valido
variable_01 = 10 #valido

# mi_variable = 10 # Corrección: mi_variable = 10
numero_entero = 123
numero_decimal = 123.45
booleano = True #False
variable_string = "Hola mundo"
#compuestos o complejos
lista = [1, 2, 3, 4]
#operador de asignacion
mi_variable = 123
#operadores matematicos
suma = 5 + 9.5
resta = 24 - 123
multiplicacion = 4 * 6
division = 15 / 3
division_entera = 45 // 7
modulo_residuo = 45 % 7
potencia = 2 ** 8
raiz = 2 ** (1/2)

#jerarquia
# 1. Paréntesis
# 2. Potencias y raíces
# 3. Multiplicación, división, división entera y módulo
# 4. Suma y resta

#operdores relacionales / booleanos
# ==, !=, >, <, >=, <=, ===
igual = 5 == 5
distinto = 5 != 5
mayor = 5 > 5
menor = 5 < 5
mayor_igual = 5 >= 5
menor_igual = 5 <= 5

celsius = 689
fahrenheit = (celsius * 9/5) + 32

print("hola mundo")
print(f"La temperatura en Fahrenheit es: {fahrenheit}") #1272.2
#Imprimir valores en la terminal
print (f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

# Pedir informacion al usuario
calificacion_1 = float(input("Ingrese la primera calificacion: "))
calificacion_2 = float(input("Ingrese la segunda calificacion: "))
calificacion_3 = float(input("Ingrese la tercera calificacion: "))
promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3
print(f"El promedio de las calificaciones es: {promedio}")