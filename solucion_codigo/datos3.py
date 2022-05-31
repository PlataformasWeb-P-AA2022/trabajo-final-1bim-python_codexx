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

datos3 = session.query(Establecimiento, Parroquia, Canton).join(Establecimiento, Canton).\
    filter(Establecimiento.num_docentes.in_(['0', '5', '11'])).order_by(Establecimiento.num_docentes).all()

print("\n----------------Consulta 1----------------------\n")
count = 1
print("\033[0;m"+"Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores"+'\033[0;m')
for s in datos3:
    print("_____________________________________________________________________________")
    print("| Id: %s | Nombre: %s | Canton: %s | Profesores: %s |" % (count, s.Establecimiento.nombre_e, s.Canton.nombre, s.Establecimiento.num_docentes))
    count = count + 1

datos3_2 = session.query(Establecimiento, Parroquia).join(Parroquia).\
filter(and_(Establecimiento.num_estudiantes >= 21, Parroquia.nombre == 'PINDAL')).order_by(Establecimiento.num_estudiantes).all()

print("\n----------------Consulta 2----------------------\n")
count2 = 1
print("\033[0;m"+"Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21"+'\033[0;m')

for s in datos3_2:
    print("_____________________________________________________________________________")
    print("| Id: %s | Nombre: %s | Parroquia: %s | Estudiantes: %s |" % (count2, s.Establecimiento.nombre_e, \
        s.Parroquia.nombre, s.Establecimiento.num_estudiantes))
    count2 = count2 + 1