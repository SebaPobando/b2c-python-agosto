from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app) 

@app.route("/")
def index():
   usuarios = Usuario.get_all()
   print(usuarios)
   return render_template("index.html", todos_usuarios = usuarios)

@app.route("/nuevo")
def nuevo():
   usuarios = Usuario.get_all()
   return render_template("mostrar_usuarios.html", todos_usuarios=usuarios)

@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
   pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
   datos = {
       "nombre": request.form['nombre'],
       "apellido": request.form['apellido'],
       "email": request.form['email'],
       'password': pass_hasheado
   }
   if not Usuario.validar_usuario(request.form):
       return redirect('/')
   nuevo_id = Usuario.save(datos)
   session['usuario_id'] = nuevo_id
   return redirect('/nuevo')

@app.route("/usuario/<int:id>")
def ver_usuario(id):
   data = { "id": id }
   usuario = Usuario.get_by_id(data)
   return render_template("mostrar_uno.html", un_usuario=usuario)

@app.route("/usuario/eliminar/<int:id>")
def borrar_usuario(id):
   data = { "id": id }
   Usuario.delete(data)
   return redirect('/nuevo')

@app.route("/usuario/actualizar/<int:id>", methods=['POST'])
def actualizar_usuario(id):
    datos = {
        "id": id,
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.update(datos)
    return redirect('/nuevo')
 
@app.route("/usuario/editar/<int:id>")
def cargar_editar(id):
    data = { "id": id }
    usuario = Usuario.get_by_id(data)
    print(usuario)
    return render_template("editar.html", un_usuario=usuario)
 
@app.route("/login", methods=['POST'])
def login():
    data = { "email": request.form['email'] }
    usuario_en_bd = Usuario.get_by_email(data)
    if not usuario_en_bd:
        flash("Email no registrado.")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario_en_bd.password, request.form['password']):
        flash("Contraseña incorrecta.")
        return redirect('/')
    session['usuario_id'] = usuario_en_bd.id
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión primero.")
        return redirect('/')
    data = {"id": session['usuario_id']}
    usuario = Usuario.get_by_id(data)
    return render_template("dashboard.html", usuario=usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')