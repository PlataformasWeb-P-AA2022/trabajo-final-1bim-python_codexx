from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and y or
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Consulta 1
# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
print('Consulta 1 - Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.') 

consulta1 = session.query(Establecimiento).filter(and_(Establecimiento.num_docentes > 40, Establecimiento.tipo_educacion == "Educacion Regular")).order_by(Parroquia.nombre).all()
for x in consulta1:
    print(x)
    print("---------------------------------------------------------------------------------------------")
print(len(consulta1))

# Consulta 2
#Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.
print("Consulta 2 - Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.") 

consulta2 = session.query(Establecimiento).join(Provincia).filter(Provincia.codigo_distrito == "11D04").order_by(Establecimiento.sostenimiento).all()
for x in consulta2:
    print(x)
    print("---------------------------------------------------------------------------------------------")
print(len(consulta2))