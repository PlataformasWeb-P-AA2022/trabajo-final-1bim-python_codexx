from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Establecimiento, Parroquia


from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


print("===============Consulta 1==============")
# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
print("\033[0;m"+"Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena 'Educación regular' en tipo de educación."+'\033[0;m') 

consulta40 = session.query(Establecimiento.nombre_e, Parroquia.nombre).join(Parroquia).filter(
    and_(Establecimiento.num_docentes > 40, Establecimiento.tipo_educacion.like(
        'Educación regular'))).order_by(Parroquia.nombre).all()

for i in consulta40:
    print("------------------------------------------------")
    salida = " | Nombre:| %s | Parroquia: %s |" %(str(i[0]).replace("('",""), str(i[1]).replace(")'",""))
    salida = salida.replace("',)", "")
    salida = salida.replace("'", "")
    salida = salida.replace(")", "")
    print(salida)



print("===============Consulta 1==============")
# # # Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.
print("\033[0;m"+"Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04"+'\033[0;m') 

consulta11D04 = session.query(Establecimiento.nombre_e, Establecimiento.sostenimiento).join(Parroquia, Canton).filter(Canton.codigo_distrito.like('11D04')).order_by(Establecimiento.sostenimiento)

for i in consulta11D04:
    print("------------------------------------------------")
    salida = " | Nombre: %s | Sostenimiento: %s |" %(str(i[0]).replace("('",""), str(i[1]).replace(")'",""))
    salida = salida.replace("',)", "")
    print(salida)
    

