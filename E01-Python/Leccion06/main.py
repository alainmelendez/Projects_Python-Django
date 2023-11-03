# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * factorial(numero - 1)
#
# numero = 3
# resultado = factorial(numero)
# print(f'El resultado de {numero} es: {resultado}')

# def calcular_total(pago_sin_impuesto, impuesto):
#     costo = (impuesto / 100) * pago_sin_impuesto
#     total = pago_sin_impuesto + costo
#     return total
# pago = float(input('El pago proporcionado sin impuesto sería: '))
# impuesto = float(input('Proporciona el impuesto en porcentaje: '))
# resultado = calcular_total(pago, impuesto)
# print(f'El pago total con impuesto seria: {resultado}')
#
# def celsius_fahrenheit(celsius):
#     conversion = celsius * 9/5 + 32
#     return conversion
#
# def fahrenheit_celsius(fahrenheit):
#     conversion = (fahrenheit-32) * 5/9
#     return conversion
#
# celsius = float(input('Introduzca el valor que desea convertir a fahrenheit :'))
# resultado1 =  celsius_fahrenheit(celsius)
# print(f'El valor obtenido a grados fahrenheit es: {resultado1}')
# fahrenheit = float(input('Introduzca el valor que desea convertir a celsius:'))
# resultado2 = fahrenheit_celsius(fahrenheit)
# print(f'El valor obtenido a grados celsius es: {resultado2}')


#Definición de funcion que convierte de °C --> °F

def celsius_fahrenheit(celsius):

    F = celsius * 9/5 + 32

    return F



#Definición de función que convierte de °F --> °C

def fahrenheit_celsius(fahrenheit):

    C = (fahrenheit - 32) * 5/9

    return C



#Prueba de conversión de °C --> °F

celsius = float(input('Introduzca el valor en celsius que desea convertir a fahrenheit: '))

resultado = celsius_fahrenheit(celsius)

print(f'{celsius}°C equivale a: {resultado}°F')



#Prueba de conversión de °F --> °C

fahrenheit = float(input('Introduzca el valor en fahrenheit que desea convertir a celsius: '))

resultado = fahrenheit_celsius(fahrenheit)

print(f'{fahrenheit}°F equivale a: {resultado}°C')