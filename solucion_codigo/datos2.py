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


datos2 = session.query(Establecimiento, Parroquia).join(Establecimiento).\
    filter(Establecimiento.jornada == "Matutina y Vespertina").all()

print("\n----------------Consulta 1----------------------\n")
count = 1

for s in datos2:
    print("__________________________________________________________________________________________________________________________________________")
    print("| Id: %s | Nombre: %s | Parroquia: %s | Jornada: %s |" % (count, s.Establecimiento.nombre_e, s.Parroquia.nombre, s.Establecimiento.jornada))
    count = count + 1

datos2_2 = session.query(Establecimiento, Parroquia, Canton).join(Establecimiento).\
    filter(Establecimiento.num_estudiantes.in_(['448', '450', '451', '454', '458', '459'])).order_by(Establecimiento.num_estudiantes).all()

print("\n\n----------------Consulta 2----------------------\n")
count2 = 1

for s in datos2_2:
    print("______________________________________________________________________________________")
    print("| Id: %s | Nombre: %s | Canton: %s | Estudiantes: %s |" % (count2, s.Establecimiento.nombre_e, s.Canton.nombre, s.Establecimiento.num_estudiantes))
    count2 = count2 + 1