from flask import Flask, render_template

app=Flask(__name__)

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



# Con esto inicializamos el archivo
if __name__ == '__main__':
    app.run(debug=True)