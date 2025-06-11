from flask import Flask, render_template, request, redirect, url_for, flash
from utils.utils import obtener_conversiones, crear_conversion

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesaria para usar flash messages

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/temperaturas/', methods=['GET'], strict_slashes=False)
def get_temperaturas():
    conversiones = obtener_conversiones()
    return render_template('get_temperaturas.html', conversiones=conversiones)

@app.route('/temperaturas/crear/', methods=['GET', 'POST'], strict_slashes=False)
def create_temperatura():
    if request.method == 'POST':
        temperatura = request.form['temperatura']  # Obtener temperatura del formulario
        tipo = request.form['tipo']  # Obtener tipo de conversión del formulario
        exito = crear_conversion(temperatura, tipo)  # Llamar a crear_conversion
        if exito:
            flash('Conversión creada exitosamente', 'success')
            return redirect(url_for('get_temperaturas'))
        else:
            flash('Error al crear la conversión', 'danger')
    return render_template('create_temperatura.html')

if __name__ == '__main__':
    app.run(debug=True)
