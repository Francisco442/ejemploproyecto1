from flask import Flask, render_template
#Se importa la libreria de flask
# This is a sample Python script.

# Se crea un objeto de flask
app = Flask(__name__)
#Se crea una ruta raiz
@app.route('/')
#Se crea un metodo o función para mostrar la pagina
def index():
    return render_template('index.html')
# Press the green button in the gutter to run the script.
# Se crea un archivo de ejecición
#Se ejecuta la terminal
if __name__ == '__main__':
    app.run(port=80, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

