from conexion import Conexion
from datetime import date, datetime
from io import open
from pymongo import MongoClient
import pymysql

class guardardatos():

    def guardarmysql(self,vsensor,sensor,type):
        now = datetime.now()
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        conexion = Conexion()
        self.cursor = conexion.conexionmysql().cursor()
        print('--------------------------------------------\nConexion establecida\n--------------------------------------------')
        if type == 1:
            sql = 'insert into valores(SensorID,1,`Fecha y hora`) values(%s,%s,%s)'
            val = int(sensor),int(vsensor),self._HyM
        if type == 2:
            sql = 'insert into valores(SensorID,2,`Fecha y hora`) values(%s,%s,%s)'
            val = int(sensor),float(vsensor),self._HyM
        if type == 3:
            sql = 'insert into valores(SensorID,3,`Fecha y hora`) values(%s,%s,%s)'
            val = int(sensor),str(vsensor),self._HyM
        
        self.cursor.execute(sql,val)
        conexion.conexionmysql().commit()
        
        print("--------------------------------------------\nDato insertado correctamente en MySQL\n--------------------------------------------")

    def guardarmongo(self,vsensor,sensor):
        now = datetime.now()
        if sensor == 1:
            snsr = "Ultrasonico"
        if sensor == 2:
            snsr = "PIR"
        if sensor == 3:
            snsr = "Temperatura"
        if sensor == 4:
            snsr = "Humedad"
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
        db = client['Sensores']
        col = db['Sensores']
        col.insert_one({
        'Sensor': snsr,
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
        if sensor == 1:
            archivo_texto.write("Ultrasonico")
        if sensor == 2:
            archivo_texto.write("PIR")
        if sensor == 3:
            archivo_texto.write("Temperatura")
        if sensor == 4:
            archivo_texto.write("Humedad")
        archivo_texto.write(vsensor)
        archivo_texto.write("--------------")
        archivo_texto.write(self._HyM)
        archivo_texto.write("\n")
        archivo_texto.close()
        print("---------------------------------")
        print("Datos guardados correctamente en bloc de notas")
        print("---------------------------------")