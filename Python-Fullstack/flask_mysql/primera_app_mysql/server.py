from flask import Flask, render_template, request, redirect
from mascota import Mascota

app = Flask(__name__)

@app.route("/")
def index():
   mascotas = Mascota.get_all()
   print(mascotas)
   return render_template("index.html", todas_mascotas = mascotas)

@app.route("/crear_mascota", methods=['POST'])
def crear_mascota():
   #Creamos un diccionario a partir del request.form que recibimos de la plantilla
   #IMPORTANTE: las claves deben de coincidir con las variables en el query
   datos = {
       "nombre": request.form['nombre'],
       "tipo": request.form['tipo'],
       "color": request.form['color']
   }
   #Enviamos el diccionario al metodo save de Mascota
   Mascota.save(datos)
   #Dirigimos a la ruta raíz para ver el nuevo registro
   return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)