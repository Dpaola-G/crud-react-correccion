from flask import Flask, session, render_template,redirect
from controller.usuarioController import login, logout

app = Flask(__name__)
app.secret_key = "clave_secreta"  # Clave secreta para manejar sesiones

# //////////////////////////////////AL INICIAR ////////////////////////////////////////////

@app.route('/')
def inicio():
    if 'usuario' in session:
        usuario = session['usuario']
        return render_template('tabla.html', usuario=usuario)
    return redirect('/login ')


#//////////////////////////////////AL PASAR EL FORMUULARIO/////////////////////////////////
@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return login()


#//////////////////////////////////CERRAR SESION//////////////////////////////////////


@app.route('/logout')
def logout_route():
    return logout()




if __name__ == '__main__':
    app.run(debug=True)
