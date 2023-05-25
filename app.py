from flask import Flask, render_template, abort, request
import requests
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)
url_base = "https://apifootball.com/documentation/"

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.environ["API_KEY"]

# Ruta de inicio
@app.route('/')
def inicio():
    return render_template("inicio.html")

# Ruta de competiciones de liga
@app.route('/competiciones', methods=["GET", "POST"])
def competiciones():
    url = f"https://apiv3.apifootball.com/?action=get_leagues&country_id=6&APIkey={api_key}"

    if request.method == "GET":
        # Realizar solicitud GET a la API
        response = requests.get(url)
        data = response.json()

        # Verificar si se obtuvo una respuesta válida de la API
        if not isinstance(data, list):
            return "Error al obtener los datos de la API"

        # Crear una lista vacía para almacenar las competiciones
        competiciones = []

        # Recorrer los datos obtenidos y agregar cada competición a la lista
        for competicion in data:
            # Verificar si el objeto competición es un diccionario
            if not isinstance(competicion, dict):
                continue

            competicion_dict = {
                "country_id": competicion.get("country_id", ""),
                "country_name": competicion.get("country_name", ""),
                "league_id": competicion.get("league_id", ""),
                "league_name": competicion.get("league_name", ""),
                "league_season": competicion.get("league_season", ""),
            }
            competiciones.append(competicion_dict)

        return render_template("competiciones.html", competiciones=competiciones)

    elif request.method == "POST":
        # Realizar solicitud POST a la API
        # ...
        return "Realizando solicitud POST a la API"

# Ruta de países
@app.route('/paises', methods=["GET", "POST"])
def paises():
    url = f"https://apiv3.apifootball.com/?action=get_countries&APIkey={api_key}"

    if request.method == "GET":
        # Realizar solicitud GET a la API
        response = requests.get(url)
        data = response.json()

        # Verificar si se obtuvo una respuesta válida de la API
        if not isinstance(data, list):
            return "Error al obtener los datos de la API"

        # Crear una lista vacía para almacenar los países
        paises = []

        # Recorrer los datos obtenidos y agregar cada país con su ID a la lista
        for pais in data:
            # Verificar si el objeto país es un diccionario
            if not isinstance(pais, dict):
                continue

            pais_dict = {
                "country_id": pais.get("country_id", ""),
                "country_name": pais.get("country_name", ""),
                "country_logo": pais.get("country_logo", "")
            }
            paises.append(pais_dict)

        return render_template("paises.html", paises=paises)



if __name__ == '__main__':
    app.run()
