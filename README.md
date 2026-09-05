# Priorización de problemas en una colonia.

# Contexto

En México es bien sabido que en algunas ocasiones los recursos públicos no se distribuyen de manera eficiente y no siempre llegan a las zonas que presentan mayores necesidades. Los distintos problemas que afectan a una colonia y a sus habitantes pueden ser difíciles de cuantificar y comparar, y es en este punto donde se centra el proyecto.

Conocer qué zonas presentan mayores necesidades y, por lo tanto, deberían tener una mayor prioridad en la atención de sus problemas, es un factor fundamental para contribuir al bienestar de una comunidad. La falta de atención a estas necesidades puede contribuir a diferentes problemáticas, como la desigualdad social, la inseguridad, la división social, la devaluación de las viviendas y la falta de acceso a servicios básicos, entre otras.

Fuente: ( https://mexico.unir.net/noticias/ciencias-sociales/desigualdad-social/ ).

# Objetivo del proyecto.

El objetivo de mi proyecto es hacer que las necesidades y problemáticas presentes en una colonia puedan ser más cuantificables mediante el uso de números y datos. De esta manera, se busca desarrollar un programa que permita analizar diferentes características de una colonia y asignarles un nivel de prioridad, con el propósito de obtener una representación más clara de sus necesidades y facilitar la identificación de aquellas que requieren mayor atención.

# Pseudocodigo
```text
# Pseudocódigo

Entrada

Nombre de la colonia.
Número de habitantes.
Número de problemas de infraestructura.
Gravedad de los problemas de infraestructura (1 al 10).
Porcentaje de iluminación.
Porcentaje de áreas verdes.

Proceso

1. Multiplicar el número de problemas de infraestructura por su gravedad.
2. Multiplicar el resultado de infraestructura por su peso de 40%.
3. Restar el porcentaje de iluminación a 100 para obtener la necesidad de iluminación.
4. Multiplicar la necesidad de iluminación por su peso de 30%.
5. Restar el porcentaje de áreas verdes a 100 para obtener la necesidad de áreas verdes.
6. Multiplicar la necesidad de áreas verdes por su peso de 20%.
7. Convertir el número de habitantes a una escala que permita compararlo con los demás factores.
8. Multiplicar la puntuación de habitantes por su peso de 10%.
9. Sumar las puntuaciones de los cuatro factores para obtener la prioridad total de la colonia.

Salida

Nombre de la colonia.
Puntuación de infraestructura.
Puntuación de iluminación.
Puntuación de áreas verdes.
Puntuación de habitantes.
Índice de prioridad de la colonia.

