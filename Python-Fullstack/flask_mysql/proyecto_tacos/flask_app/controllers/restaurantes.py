from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.restaurante import Restaurante
from controllers import tacos

@app.route('/restaurantes')
def restaurantes():
    return render_template('restaurantes.html', todos_restaurantes=Restaurante.get_all())

@app.route('/restaurante/crear', methods=['POST'])
def crear_restaurante():
    datos = {
        "nombre": request.form['nombre']
    }
    Restaurante.save(datos)
    return redirect('/')
