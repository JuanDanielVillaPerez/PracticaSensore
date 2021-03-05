from conexion import Conexion
from datetime import date, datetime
from io import open
from pymongo import MongoClient
import pymysql

class guardardatos():

    def guardarmysql(self,sensor):
        id = sensor[0]
        vsensor = sensor[2]
        tipo = sensor[3]
        now = datetime.now()
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        conexion = Conexion()
        self.cursor = conexion.conexionmysql().cursor()
        print('--------------------------------------------\nConexion establecida\n--------------------------------------------')
        if tipo == 1:
            sql = 'insert into valores(SensorID,1,`Fecha y hora`) values(%s,%s,%s)'
            val = int(id),int(vsensor),self._HyM
        if tipo == 2:
            sql = 'insert into valores(SensorID,2,`Fecha y hora`) values(%s,%s,%s)'
            val = int(id),float(vsensor),self._HyM
        if tipo == 3:
            sql = 'insert into valores(SensorID,3,`Fecha y hora`) values(%s,%s,%s)'
            val = int(id),str(vsensor),self._HyM
        
        self.cursor.execute(sql,val)
        conexion.conexionmysql().commit()
        
        print("--------------------------------------------\nDato insertado correctamente en MySQL\n--------------------------------------------")

    def guardarmongo(self,sensor):
        snsr = sensor[1]
        vsensor = sensor[2]
        now = datetime.now()
        
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

    def guardardatostxt(self,sensor):
        snsr = sensor[1]
        vsensor = sensor[2]
        now = datetime.now()
        self._HyM = now.strftime("%y/%m/%d, %H:%M:%S")
        archivo_texto = open("Valores.txt", "a")
        archivo_texto.write(snsr)
        archivo_texto.write("----")
        archivo_texto.write(vsensor)
        archivo_texto.write("--------------")
        archivo_texto.write(self._HyM)
        archivo_texto.write("\n")
        archivo_texto.close()
        print("---------------------------------")
        print("Datos guardados correctamente en bloc de notas")
        print("---------------------------------")