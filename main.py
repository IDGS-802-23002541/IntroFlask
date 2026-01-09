from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo :DDDDDDDDD"

@app.route('/hola')
def hola():
    return "Hola al cuadrado!"

if __name__ == '__main__':
    app.run(debug=True)