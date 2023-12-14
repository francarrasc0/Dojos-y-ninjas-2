from app_flask.config.mysqlconnection import connectToMySQL
from app_flask import BASE_DATOS

class Ninja:
    def __init__(self, datos):
        self.id = datos['id']
        self.first_name = datos['first_name']
        self.last_name = datos['last_name']
        self.age = datos['age']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.dojos_id = datos['dojos_id']
    
    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO ninjas(first_name, last_name, age, dojos_id)
                VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojos_id)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)