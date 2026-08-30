#El usuario ingresa las diferentes colonias y sus caracteristicas, el programa nos dara un resultado de la prioridad que tiene cada colonia para recibir recursos publicos.
nombre_de_la_colonia = input ("ingrese el nombre de la colonia:")
numero_de_habitantes = int(input("ingrese el numero de habitantes:"))
numero_de_problemas_infraestructura = int (input("ingrese el numero de problemas de infraestructura:"))
gravedad_infraestructura = int (input("ingrese la gravedad de los problemas en una escala del 1 al 10 siendo 1 poco grave y 10 muy grave:"))
porcentaje_iluminacion = float (input("ingrese el porcentaje que cree que tiene de iluminacion en la colonia:"))
porcentaje_areas_verdes = float (input("ingrese el porcentaje que cree que tiene de areas verdes en la colonia:"))

#Para la creacion de una formula que nos permita priorizar los recursos que recibe cada colonia tomare en cuenta las siguientes afirmaciones:
#1: mas personas afectadas = a mayor prioridad
#2: mas numero de problemas de infraestructura = a mayor prioridad
#3: menos iluminacion de la colonia = a mayor prioridad
#4: menos areas verdes = a mayor prioridad
#La importancia de cada uno de los factores sera la siguiente:
#1: la importancia sera baja ya que la cantidad de personas no define la magnitud de los problemas que se le presentan. 10%
#2: la importancia sera muy alta debido a que la infraestructura es un factor determinante para el desarrollo de la colonia. 40%
#3: la importancia sera alta ya que la iluminacion es un factor determinante casi igual que l infraestructura para el desarrollo de la colonia. 30%
#4: la importancia sera media ya que las areas verdes son importantes pero no tan determinantes como lo son la infraestructura y la iluminacion. 20%

puntuacion_infraestructura = (numero_de_problemas_infraestructura * gravedad_infraestructura) * 0.4
print ("La puntuacion de infraestructura es:", puntuacion_infraestructura)
