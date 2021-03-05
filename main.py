from guardardatos import guardardatos
from sensor import sensor

sensor = sensor()
gd = guardardatos()

#1_Ultrasonico
vsensor = sensor.ultrasonico()
gd.guardarmysql(vsensor)
gd.guardarmongo(vsensor)
gd.guardardatostxt(vsensor)



