import urllib.request
req = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

with urllib.request.urlopen(req) as mensaje:
    contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena
print('Número de veces Universidad: ', contenido.count('Universidad'))

# upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# lower convierte en minúsculas un str
print(contenido.lower())

# buscamos las cadena python en el contenido
print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe Python?: ','Python'.upper() in contenido.upper())

# startswith -Inicia con
print('Inicia con: ', contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con: ', contenido.lower().endswith('GlobalMentoring.com.mx'.lower()))

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

# Alinear cadenas

# center - Centrar un str
titulo = 'Sitio web de GlobalMentoring.com.mx'
#print(len(titulo))
# print(titulo.center(50, '*'))
# print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+ 10, '-'))

# ljust- alinea a la izquierda
#print(titulo.ljust(50, '*'))
print(titulo.ljust(len(titulo)+ 10, '-'))

# rjust alinea a la derecha
print(titulo.rjust(50, '*'))
print(titulo.rjust(len(titulo)+ 10, '-'))

# Reemplazar contenido en un str
print(contenido.replace(' ','-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:',titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:',titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:',titulo)

#   leer contenido online
# from urllib.request import urlopen
#
# with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
#     #contenido = mensaje.read()
     #contenido = mensaje.read().decode('utf-8')
#     print(contenido)