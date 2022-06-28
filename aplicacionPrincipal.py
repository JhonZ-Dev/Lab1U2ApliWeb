import glob # importamos glob
import io # importamos io
import os # importamos os
import uuid # importamos uuid

# importar la libreria flask
from flask import Flask, render_template # importamos render_template
from flask import Flask, redirect, request,render_template, url_for # importamos render_template


app = Flask(__name__) # creamos una instancia de la clase Flask
app.secret_key = "s3cr3t" # creamos una clave secreta para la aplicacion
app.debug = False # indicamos que no estamos en modo debug
app._static_folder = os.path.abspath("templates/static/") # indicamos que la carpeta static esta en la carpeta templates


@app.route('/') # indicamos que la ruta es '/'
def principal(): # creamos una funcion principal
    """
    Esta función esta encarga de abrir la página principal
    para luego poder llamar a las demas subpáginas

    Returns:
        Retorna la página principal, denomindad index.html
    """
    #Index es nuestra página principal
    return render_template('layouts/index.html') # retornamos la página index.html 

if __name__ == '__main__': # si el archivo es el principal
    app.run(debug=True) # ejecutamos la aplicacion	en modo debug