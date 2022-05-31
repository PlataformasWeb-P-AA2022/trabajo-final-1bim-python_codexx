from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from sqlalchemy import asc

from genera_tablas import Provincia, Canton, Establecimiento, Parroquia


from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Consulta 1
# Los establecimientos ordenados por número de estudiantes que tengan más de 100 profesores.
print("===============Consulta 1==============")
print("\033[0;m"+"Los establecimientos ordenados por número de estudiantes que tengan más de 100 profesores."+'\033[0;m') 
consulta1 = session.query(Establecimiento.nombre_e, Establecimiento.num_estudiantes).filter(Establecimiento.num_docentes > 100)\
    .order_by(asc(Establecimiento.num_estudiantes)).all()

for r in consulta1:
    print("------------------------------------------------")
    salida = "| Nombre del Establecimiento: %s | Num Estudiantes: %s |" %(str(r[0]).replace("('",""), r[1])
    salida = salida.replace("',)", "")
    print(salida)


# Consulta 1
# Los establecimientos ordenados por número de profesores que tengan más de 100 profesores.
print("===============Consulta 2==============")
print("\033[0;m"+"Los establecimientos ordenados por número de profesores que tengan más de 100 profesores."+'\033[0;m') 

consulta2 = session.query(Establecimiento.nombre_e, Establecimiento.num_docentes).filter(
    Establecimiento.num_docentes > 100).order_by(asc(Establecimiento.num_docentes)).all()

for r in consulta2:
    print("------------------------------------------------")
    salida = "| Nombre del Establecimiento: %s | Num Docentes: %s |" %(str(r[0]).replace("('",""), r[1])
    salida = salida.replace("',)", "")
    salida = salida.replace(")","")
    print(salida)
