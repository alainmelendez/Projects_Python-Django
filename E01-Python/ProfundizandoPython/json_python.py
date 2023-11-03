# Leer archivo json
# JSON = JavaScript Object Notation
import json
import urllib.request

req = urllib.request.Request('http://globalmentoring.com.mx/api/personas.json',

data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
print(req)
with urllib.request.urlopen(req) as mensaje:
    respuesta = mensaje.read()
    print(respuesta)
# Procesamos la respuesta
with urllib.request.urlopen(req) as mensaje:
    json_respuesta = json.loads(mensaje.read().decode('utf-8'))
    print(json_respuesta)
# Imprimir solo los nombres de las personas
# JSON se convierte a listas  y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')
# Accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')