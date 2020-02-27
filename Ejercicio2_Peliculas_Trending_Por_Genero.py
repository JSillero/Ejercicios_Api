'''2. Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.

Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org

Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending

'''
import null as null
import requests
import json

api='f63dcb759885c0a18d48e5e6c33e1060'

p_tiempo=""
while(p_tiempo==""):
    respuesta=input("¿Quiere consultar las peliculas de esta semana o de este día?\nIntroduzca el numero asignado a cada opción:\n 1. Dia \n 2. Semana\n")
    if(respuesta== "1"):
        p_tiempo = "day"
    elif(respuesta == "2"):
        p_tiempo = "week"
    else:
        print("ERROR: INTRODUZCA LOS VALORES 1 O 2")

puerta_genero=null
while(puerta_genero is null):
    respuesta=input("¿Quiere filtrar los resultados por genero? \nIntroduzca el numero asignado a cada opción:\n 1. Si \n 2. No\n")
    if (respuesta == "1"):
        puerta_genero = True
    elif (respuesta == "2"):
        puerta_genero = False
    else:
        print("ERROR: INTRODUZCA LOS VALORES 1 O 2")


if(puerta_genero):
    url_g="https://api.themoviedb.org/3/genre/movie/list?"
    parametros_g = {'api_key':api,'language':'es'}

    r=requests.get(url_g,params=parametros_g)

    datos_g=r.json()
    generos_id=[]
    for x in datos_g['genres']:
        print(x['name']," con el identificador ",x['id'])
        generos_id.append(x['id'])

    genero= null
    while(genero is null):
        respuesta = int(input("Introduzca el identificador del genero que quiere consultar:\n"))
        for x in generos_id:
            if(respuesta==x):
                genero=respuesta
                break
        if(genero is null):
            print("ERROR: el genero tiene que coincidir con unos de los listados anteriormente:\n")

numero_a_mostrar=5
cantidad=0
pagina=1
print("Las 5 peliculas trending de acuerdo a los criterios establecidos son: ")
while (cantidad<numero_a_mostrar):

    url="https://api.themoviedb.org/3/trending/movie/"+p_tiempo+"?"
    parametros = {'api_key':api,'page':str(pagina),'language':'es'}

    r=requests.get(url,params=parametros)

    datos=r.json()

    if(puerta_genero):

        for x in datos['results']:
            for y in x['genre_ids']:
                if(y==genero):
                    print(x['title'])
                    cantidad+=1
                    break
            if (cantidad > numero_a_mostrar - 1):
                break

    else:
        for x in datos['results']:
            print(x['title'])
            cantidad+=1
            if(cantidad>numero_a_mostrar-1):
                break
    pagina+=1