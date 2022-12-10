from flask import Flask
import requests

app = Flask(__name__)


@app.route('/PruebasPCR')
def consulta_recurso():
    consulta_datos_pcr = requests.get("https://www.datos.gov.co/resource/8835-5baf.json")
    data_json = consulta_datos_pcr.json()
    return data_json

if __name__ == "__main__":
    app.run()
