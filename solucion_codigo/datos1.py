from itertools import count
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import * 

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

consulta1 = session.query(Establecimiento.nombre_e).join(Parroquia, Canton, Provincia).filter(Parroquia.cod_division_politica.like("110553")).all()

print("----------------Consulta 1----------------------")
print("\033[0;m"+"Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553."+'\033[0;m') 
for r in consulta1:
    print("-------------------------------------------------")
    cadena = " | Nombre Establecimiento: %s |" %(str(r).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)



consulta2 = session.query(Establecimiento.nombre_e).join(Parroquia, Canton, Provincia).filter(Provincia.nombre == 'EL ORO').all()

print("----------------Consulta 2----------------------")
print("\033[0;m"+"Todos los establecimientos de la provincia del Oro.."+'\033[0;m')
for elemento in consulta2:
    print("-------------------------------------------------")
    salida = " | Nombre Establecimiento: %s |" %(str(elemento).replace("('",""))
    salida = salida.replace("',)", "")
    print(salida)




consulta3 = session.query(Establecimiento.nombre_e).join(Parroquia, Canton, Provincia).filter(Canton.nombre == 'PORTOVELO').all()
print("----------------Consulta 3----------------------")
print("\033[0;m"+"Todos los establecimientos de la provincia del Portovelo.."+'\033[0;m')
for r in consulta3:
    print("-------------------------------------------------")
    salida = " | Nombre Establecimiento: %s |" %(str(r).replace("('",""))
    salida = salida.replace("',)", "")
    print(salida)


establecimiento = session.query(Establecimiento.nombre_e).join(Parroquia, Canton, Provincia).filter(Canton.nombre == 'ZAMORA').all()
print("----------------Consulta 4----------------------")
print("\033[0;m"+"Todos los establecimientos de la provincia del Zamora.."+'\033[0;m')
for r in establecimiento:
    print("-------------------------------------------------")
    salida = "| Nombre Establecimiento: %s |" %(str(r).replace("('",""))
    salida = salida.replace("',)", "")
    print(salida)




