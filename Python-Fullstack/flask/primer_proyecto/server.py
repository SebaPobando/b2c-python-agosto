from flask import Flask, render_template

app = Flask(__name__)

cursos = [
    {"nombre": "Python Básico", "nivel": "Fácil", "activo": True},
    {"nombre": "Flask Web", "nivel": "Intermedio", "activo": True},
    {"nombre": "Bases de Datos con MySQL", "nivel": "Intermedio", "activo": False},
]

@app.route('/cursos')
def listar_cursos():
    return render_template('cursos.html', cursos=cursos)

@app.route('/')
def hola_mundo():
    return render_template('index.html')

@app.route('/adios')
def adios_mundo():
    return '¡Adiós Mundo!'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'

@app.route('/saludo/<nombre>/<int:num>')
def hola_cantidad(nombre, num):
   return f'¡Hola {nombre}!'*num

if __name__ == "__main__":
    app.run(debug=True)