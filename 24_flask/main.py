from flask import Flask, flash, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)       #Creamos el objeto flask (aplicación)

#Hemos de crear una clave secreta para determinadas funciones
app.secret_key = 'clave_secreta_flask'

#Conexión DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

# Content processors
@app.context_processor
def date_now():
    return {'now': datetime.utcnow()}


# Endpoints
# Definimos rutas (cada ruta va asociada a una función)
@app.route('/')             #Ruta principal
def index():
    edad = 15
    personas = ['Luis', 'Marta', 'David', 'Felisa']
    return render_template('index.html', 
                            edad=edad,
                            dato1="Valor1",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"],
                            personas = personas)

#Ruta con parámetros
# @app.route('/informacion/<string:nombre>/<string:apellido>')
# def informacion(nombre, apellido):
#     return f"""<h1>Página de información</h1>
#                 <p>Esta es la página de información</p>
#                 <h3>Bienvenido {nombre} {apellido}</h3>"""

#Ruta con parámetros opcionales 
@app.route('/masinfo') #Sin parámetro
@app.route('/masinfo/<string:nombre>') #Con parámetro (opcional)
def masinfo(nombre = None): #Hay que poner un valor por defecto
    texto = ""
    if nombre != None:
        texto=f"Bienveni@ {nombre}"
    return render_template('informacion.html', texto=texto)

#Ruta con redirección
#Hay que importar las funciones  redirect y url_for
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
    
    
@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')

@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        #return f"{marca}, {modelo}, {precio}, {ciudad}"
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL,%s,%s,%s,%s)",
                      (marca, modelo, precio, ciudad))
        cursor.connection.commit()

        flash('El vehiculo ya esta en la base de datos!')
        return redirect(url_for('index'))
    return render_template('crear_coche.html')

@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches")
    coches = cursor.fetchall()
    cursor.close()

    return render_template("coches.html", coches = coches)

@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template("coche.html", coche = coche[0])

@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor()
    #Con la misma sintaxis que la del SELECT pero utilizamos otra forma distinta como ejemplo
    cursor.execute("DELETE FROM coches WHERE id=%s", (coche_id))
    cursor.connection.commit()

    flash('El coche ha sido eliminado !!')
    return redirect(url_for('coches'))

@app.route('/editar_coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        cursor = mysql.connection.cursor()

        cursor.execute('''
                        UPDATE coches
                        SET marca = %s,
                            modelo = %s,
                            precio = %s,
                            ciudad = %s
                        WHERE id = %s''',
                      (marca, modelo, precio, ciudad, coche_id))
        cursor.connection.commit()

        flash('Acabas de editar el coche!')
        return redirect(url_for('coches'))
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()
    return render_template("crear_coche.html", coche = coche[0])



#Finalmente ejecutatos la app
#Arranque del servidor
if __name__ == '__main__':
    app.run(debug=True)  

'''
Para arrancar el servidor ejecutar: python main.py
'''