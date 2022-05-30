from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, _or

from genera_tablas import Provincia, Canton, Establecimiento, Parroquia


from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Consulta 1
# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
print("\033[0;m"+"Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena 'Educación regular' en tipo de educación."+'\033[0;m') 

consulta1 = session.query(Establecimiento.nombre_e).join(Parroquia).filter(and_(Establecimiento.num_docentes > 40,
                    Establecimiento.tipo_educacion.like("%Educación regular%"))).order_by(Parroquia.nombre).all()
for i in consulta1:
    print("Nombre de Establecimiento: %s" % (i))
print(len(consulta1))


# # Consulta 1
# # Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.
print("\033[0;m"+"Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04"+'\033[0;m') 

consulta1 = session.query(Establecimiento).join(Provincia).filter(Provincia.codigo_distrito == '11D04').order_by(Establecimiento.sostenimiento).all()
for i in consulta1:
    print(i)
print(len(consulta1))