from guardardatos import guardardatos

sensor1 = guardardatos()
#Sustituir variable para utilizar del sensor.
valort = 22
itemp = str(valort)
valorh = 33
ihume = str(valorh)
valoru = 67
iultrasonico = str(valoru)
ipir = 'Se detecta movimiento'
valortemp = str(itemp)
valorhume = str(ihume)
valorultra = str(iultrasonico)
#Mando al bloc de notas
sensor1.guardardatostxt(valortemp,valorhume)
#Mando al MySQL 
sensor1.guardarmysql(valortemp,valorhume)
#Mando a MongoDB
sensor1.guardarmongo(valortemp,valorhume)



