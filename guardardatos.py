from conexion import Conexion
from datetime import date, datetime
from io import open
from pymongo import MongoClient
import pymysql

class guardardatos():

    def guardarmysql(self,vsensor,sensor):
        now = datetime.now()
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        conexion = Conexion()
        self.cursor = conexion.conexionmysql().cursor()
        print('--------------------------------------------\nConexion establecida\n--------------------------------------------')
        sql = 'insert into sensores (valores) values(%s)'
        val = str(vsensor)
        self.cursor.execute(sql,val)
        conexion.conexionmysql().commit()
        conexion.conexionmysql().close()
        print("--------------------------------------------\nDato insertado correctamente en MySQL\n--------------------------------------------")

    def guardarmongo(self,vsensor,sensor):
        now = datetime.now()
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
        db = client['Sensores']
        col = db['Sensores']
        col.insert_one({
        'Sensor': sensor,
        'Valor': vsensor,
        'Fecha_Hora' : self._HyM
        })
        print("---------------------------------")
        print("Dato insertado en MongoDB correctamente")
        print("---------------------------------")
        client.close()

    def guardardatostxt(self,vsensor,sensor):
        now = datetime.now()
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        archivo_texto = open("Valores.txt", "a")
        archivo_texto.write(vsensor)
        archivo_texto.write("--------------")
        archivo_texto.write(self._HyM)
        archivo_texto.write("\n")
        archivo_texto.close()
        print("---------------------------------")
        print("Datos guardados correctamente en bloc de notas")
        print("---------------------------------")