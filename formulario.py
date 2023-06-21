from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        date = request.form['Date']

        # Validar los datos (puedes agregar más validaciones según tus necesidades)
        if nombre == '' or email == '' or password == '' or date == '':
            return 'Por favor, completa todos los campos.'

        # Procesar los datos (aquí puedes realizar operaciones en la base de datos)

        # Mostrar un mensaje de éxito
        return f'Registro exitoso. ¡Bienvenido, {nombre}!'
    
    # Renderizar el formulario
    return render_template('registro.html')

if __name__ == '__main__':
    app.run()
