'''1. Usando esta API de OpenWeather que nos da el pronóstico del
tiempo para una ciudad que se le pide al usuario de los siguientes
 cinco días, mostrar:

Temperatura media, mínima y máxima (en grados Celsius) para cada
 día y global.

Temperatura media, mínima y máxima para cada día y global.

Tened en cuenta que las respuestas de esta api referentes
a los días y horas usan el tiempo en formato UNIX (UTC).
@author: Jose Sillero
'''
import requests
import json

print("Introduzca el nombre de la ciudad para la que quiere comprobar el tiempo.")

ciudad="Cordoba"


apikey="3ad17004b56c3977e6536ac7a6ee46e3"
url="https://api.openweathermap.org/data/2.5/forecast"
parametros = {'q':ciudad,'mode':'json','units':'metric','APPID':'3ad17004b56c3977e6536ac7a6ee46e3','cnt': 50}

r=requests.get(url,params=parametros)
'''
para comprobar datos descomentar
print(r.url)
print(r.headers)
'''
datos=r.json()
'''
para comprobar datos descomentar
print(datos)
'''

'''se coge la primera fecha y se le suman 24 horas en segundos para que la siguiente que se muestre sea dentro de 1 dia'''
fecha_sec=datos['list'][0]["dt"]+86400

'''Coge la fecha en la que se saca la temperatura y quita la hora'''
fecha=datos['list'][0]["dt_txt"][0:10]

print("Temperatura media hoy ",fecha," en ", ciudad ,": ", datos['list'][0]["main"]["temp"])
print("Temperatura maxima hoy ",fecha ," en ", ciudad ,": ", datos['list'][0]["main"]["temp_max"])
print("Temperatura minima hoy ",fecha," en", ciudad ,": ", datos['list'][0]["main"]["temp_min"])
print()

cantidad=0

cnt=1
'''repite hasta que se muestren las temperaturas 4 veces más'''
while(cantidad<4):
    '''restringe el mostrar las temperaturas a no ser que el dt sea mayor que el anterior por más de 86400(24 horas en segundos'''
    if(datos['list'][cnt]["dt"]>fecha_sec):
        cantidad+=1
        fecha_sec+=+86400
        fecha=datos['list'][cnt]["dt_txt"][0:10]
        print("Temperatura media a",fecha," en ", ciudad ,": ", datos['list'][cnt]["main"]["temp"])
        print("Temperatura maxima a",fecha ," en ", ciudad ,": ", datos['list'][cnt]["main"]["temp_max"])
        print("Temperatura minima a",fecha," en", ciudad ,": ", datos['list'][cnt]["main"]["temp_min"])
        print()

    cnt+=1

