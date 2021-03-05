import pymysql

class Conexion():

    def conexionmysql(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sensores'
        )
        
