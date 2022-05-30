from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  

from genera_tablas import Provincia, Canton, Establecimiento, Parroquia


from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Consulta 1
# Los establecimientos ordenados por número de estudiantes que tengan más de 100 profesores.
print("\033[0;m"+"Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores."+'\033[0;m') 

consulta1 = session.query(Establecimiento.nombre_e).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_estudiantes).all()
for i in consulta1:
    print(i)
print(len(consulta1))

# Consulta 1
# Los establecimientos ordenados por número de profesores que tengan más de 100 profesores.
print("\033[0;m"+"Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores."+'\033[0;m') 

consulta2 = session.query(Establecimiento.nombre_e).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_docentes).all()
for i in consulta2:
    print(i)
print(len(consulta2))

