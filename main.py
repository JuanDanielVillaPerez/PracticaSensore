from guardardatos import guardardatos
from sensor import sensor

sensor = sensor()
gd = guardardatos()

#1_Ultrasonico
vsensor = sensor.ultrasonico()
gd.guardarmysql(vsensor,1,2)
gd.guardarmongo(vsensor,1)
gd.guardardatostxt(vsensor,1)



