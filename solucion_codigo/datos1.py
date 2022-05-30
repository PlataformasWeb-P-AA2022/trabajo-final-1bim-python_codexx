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




# establecimientos = session.query(Establecimiento, Parroquia).join(Establecimiento).\
#     filter(Parroquia.cod_division_politica.like("110553")).all()

# print("----------------Consulta 1----------------------")
# for r in establecimientos:
#     print("______________________________________________")
#     print("Nombre: %s | Parroquia: %s | Codigo Division Politica: %s" % (r.Establecimiento.nombre_e, r.Parroquia.nombre, r.Parroquia.cod_division_politica))



# establecimientos2 = session.query(Establecimiento, Provincia).\
#     filter(Provincia.nombre.like("El Oro"))


# print("----------------Consulta 2----------------------")
# for n in establecimientos2:
#     print("______________________________________________")
#     print("| Nombre: %s | Provincia: %s |" % ( n.Establecimiento.nombre_e, n.Provincia.nombre))




# establecimientos3 = session.query(Establecimiento, Canton).\
#     #filter(Canton.nombre.like("Portovelo")).all()

# print("----------------Consulta 3----------------------")
# for s in establecimientos3:
#     print("______________________________________________")
#     print("Nombre: %s | Canton: %s" % (s.Establecimiento.nombre_e, s.Canton.nombre))




establecimientos4 = session.query(Establecimiento, Canton).filter(Canton.nombre == "Zamora").join().all() 

cont = 1
print("----------------Consulta 4----------------------")
for s in establecimientos4:
    print("______________________________________________")
    print("| Id: %s | Nombre: %s | Canton: %s |" % (cont ,s.Establecimiento.nombre_e, s.Canton.nombre))
    cont = cont+1



