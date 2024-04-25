from flask import render_template, request, redirect, session
from pymongo import MongoClient

# Conexión a la base de datos MongoDB (asegúrate de que MongoDB esté en funcionamiento)
client = MongoClient('mongodb://localhost:27017/')
db = client['CrudFlask']
usuarios_collection = db['Usuarios']  # Cambiar el nombre de la colección a "Usuarios"

def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        usuario_encontrado = usuarios_collection.find_one({'correo': correo})
        if usuario_encontrado and usuario_encontrado['contraseña'] == contraseña:
            session['usuario'] = correo
            return redirect('/')
        else:
            mensaje = "Correo o contraseña incorrectos."
            return render_template('login.html', mensaje=mensaje)
    return render_template('login.html')

def logout():
    session.pop('usuario', None)
    return redirect('/')
