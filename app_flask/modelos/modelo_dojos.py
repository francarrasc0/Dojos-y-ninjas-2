from app_flask.config.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_ninjas
from app_flask import BASE_DATOS

class Dojo:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.ninjas = []
    
    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO dojos(nombre)
                VALUES (%(nombre)s);
                """

        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @classmethod
    def seleccionar_todos(cls):
        query = """
                SELECT *
                FROM dojos;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_dojos = []
        for renglon in resultado:
            lista_dojos.append(cls(renglon))
        return lista_dojos

    @classmethod
    def seleccionar_uno_con_ninjas(cls, datos):
        query = """
                SELECT *
                FROM dojos LEFT JOIN ninjas
                    ON dojos.id = ninjas.dojos_id
                WHERE dojos.id = %(dojos_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        dojo = Dojo(resultado[0])
        for renglon in resultado:
            if renglon['age'] != None:
                ninja = {
                    'id' : renglon['ninjas.id'],
                    'first_name' : renglon['first_name'],
                    'last_name' : renglon['last_name'],
                    'age' : renglon['age'],
                    'fecha_creacion' : renglon['ninjas.fecha_creacion'],
                    'fecha_actualizacion' : renglon['ninjas.fecha_actualizacion'],
                    'dojos_id' : renglon['id']
                }
                dojo.ninjas.append(modelo_ninjas.Ninja(ninja))
        return dojo