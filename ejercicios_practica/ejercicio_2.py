# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número entero a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número entero a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números enteros solicitados
# print(....)
print (numero_1)
print (numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multi = numero_1 * numero_2
divi = numero_1 / numero_2

# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
print ('El resultado de sumar ' + str(numero_1) + ' y ' + str(numero_2) + ' es ' + str(suma))

# Resta
print ('El resultado de restar ' + str(numero_1) + ' y ' + str(numero_2) + ' es ' + str(resta))

# División
print ('El resultado de dividir ' + str(numero_1) + ' y ' + str(numero_2) + ' es ' + str(round(divi,2)))

# Multiplicación
print ('El resultado de multiplicar ' + str(numero_1) + ' y ' + str(numero_2) + ' es ' + str(multi))
