from flask import render_template, redirect, request
from app_flask.modelos.modelo_dojos import Dojo
from app_flask.modelos.modelo_ninjas import Ninja
from app_flask import app

@app.route('/formulario/ninja', methods=['GET'])
def desplegar_formulario_ninja():
    lista_dojos = Dojo.seleccionar_todos()
    return render_template('formulario_ninja.html', lista_dojos=lista_dojos)

@app.route('/nuevo/ninja', methods=['POST'])
def crear_ninja():
    nuevo_ninja = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojos_id" : request.form['dojos_id']
    }
    Ninja.agregar_uno(nuevo_ninja)
    return redirect(f'/dojos/{request.form["dojos_id"]}')