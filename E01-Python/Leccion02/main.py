print('Proporcione los siguientes datos del libro: ')
nombre = input('Proporciona el nombre: ')
id = int(input('Proporciona el ID: '))
precio = float(input('Proporcione el precio: '))
envioGratuito = input('Indica si el envío es gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor Incorrecto, debe escribir True/False'

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envío Gratuito?: {envioGratuito}
''')
