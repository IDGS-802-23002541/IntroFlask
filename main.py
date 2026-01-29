from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms
import math

app=Flask(__name__)
app.secret_key='Clave secreta'
csrf=CSRFProtect()

# Renderizamos un archivo estático html [DEBE ESTAR EN LA CARPETA TEMPLEATES]
@app.route('/')
def index():
    titulo="IDGS-802-Flask"
    listado=['Juan', 'Karla', 'Miguel']
    return render_template('index.html', titulo=titulo, lista=listado)

# Ruta para otra página
@app.route("/formularios")
def formularios():
    return render_template('formularios.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

@app.route('/distancia', methods=["GET", "POST"])
def distancia():
    x1=0
    x2=0
    y1=0
    y2=0
    res=0
    if request.method == "POST":
        x1=int(request.form.get("x1"))
        x2=int(request.form.get("x2"))
        y1=int(request.form.get("y1"))
        y2=int(request.form.get("y2"))
        res = math.sqrt(((x2 - x1)*(x2-x1) + (y2 - y1)*(y2 - y1)))
    return render_template('distancia.html',x1=x1,x2=x2,y1=y1,y2=y2,res=res)

@app.route('/usuarios', methods=["GET", "POST"])
def usuarios():
    matricula=0
    nom=''
    apa=''
    ama=''
    correo=''
    usuarios_class=forms.UserForm(request.form)

    if request.method == "POST" and usuarios_class.validate():
        matricula=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        correo=usuarios_class.correo.data

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("usuarios.html",form=usuarios_class, matricula=matricula, nom=nom, apa=apa, ama=ama, correo=correo)

@app.route('/cinepolis', methods=["GET", "POST"])
def cinepolis():
    Nombre = ""
    Compradores = 0
    tarjCine = ""
    Boletos = 0
    total = 0
    error = None

    if request.method == "POST":
        Nombre = request.form.get("Nombre")
        Compradores = int(request.form.get("Compradores"))
        tarjCine = request.form.get("tarjCine") == "true"
        Boletos = int(request.form.get("Boletos"))

        if not Boletos or not Compradores:
            error = "Error: Debes ingresar un número de boletos o compradores."
            return render_template('cinepolis.html', error=error, total=total)
        
        if Boletos > Compradores * 7:
            error = "Error: No se pueden comprar más de 7 boletos por comprador."
            return render_template('cinepolis.html', error=error, total=total)
        
        total = Boletos * 12
        if Boletos > 5:
            total = total - (total * 0.15)  # Aplicar descuento del 15% si son 5 boletos
        if Boletos >= 3 and Boletos <= 5:
            total = total - (total * 0.10)  # Aplicar descuento del 10% si son entre 3 y 5 boletos

        if tarjCine:
            total = total - (total * 0.10)  # Aplicar descuento del 10% por tarjeta Cinépolis
        print(total)
    return render_template('cinepolis.html', Nombre=Nombre, Compradores=Compradores, tarjCine=tarjCine, Boletos=Boletos, total=total)

# Otra ruta que tiene un metodo que retorna un saludo
@app.route('/hola')
def hola():
    return "Hola al cuadrado!"

# Podemos poner una variable en la ruta
@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!!!!!"
# f"mensaje {user}"" es igual a .format(user)

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

# Se sobreescribe el valor si existe
@app.route("/default/")
@app.route("/default/<string:param>")
def function(param="juan"):
    return f"<h1>¡Hola, {param}!<h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label for="name">Nombre:</label>
            <input type="text" id="name" name="name" required>

            <label for="appP">Apellido Paterno:</label>
            <input type="text" id="appP" name="appP" required>
        </form>
    '''

@app.route("/operasBas",  methods=["GET", "POST"])
def operas1():
    n1=0
    n2=0
    res=0
    operacion=''
    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        operacion=request.form.get("opera")

    if operacion == "suma":
        res = float(n1) + float(n2)
    elif operacion == "resta":
        res = float(n1) - float(n2)
    elif operacion == "multip":
        res = float(n1) * float(n2)
    elif operacion == "division":
        res = float(n1) / float(n2)
    else:
        res = 0
    return render_template("operasBas.html",operacion=operacion,n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    operacion=request.form.get("opera")

    if operacion == "suma":
        res = float(n1) + float(n2)
    elif operacion == "resta":
        res = float(n1) - float(n2)
    elif operacion == "multip":
        res = float(n1) * float(n2)
    elif operacion == "division":
        res = float(n1) / float(n2)
    else:
        res = 0
    return f"El resultado de la operación {operacion} es: {res}"

# Con esto inicializamos el archivo
if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)