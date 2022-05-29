
from mmap import ACCESS_COPY
from pkg_resources import Distribution
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Parroquia, Establecimiento
# from genera_tablas import Provincia, Canton
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# Se crea el enlace del gestor de base de datos
# BDD: SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
#Lectura del archivos
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    # Omitir la primera fila del csv 
    next(reader)
    # Ciclo repetitivo sobre el archivo csv para poder llenar las entidades 
    for i in reader:
        # Trasnformacion de datos tipo String a tipo Int para guardar en las tablas
        estudiantes_num=int(i[14], base=0)
        docentes_num=int(i[15], base=0)
        # Variable para guardar el id de la parroquia a la que pertenece el establecimiento
        id_p= session.query(Parroquia).filter_by(nombre = i[7]).one()
        # Creación del objeto establecimiento
        est = Establecimiento(codigo_AMIE=i[0], nombre_e=i[1], sostenimiento=i[9],tipo_educacion=i[10],
        modalidad=i[11], jornada=i[12], acceso=i[13],num_estudiantes=estudiantes_num,num_docentes=docentes_num, parroquia_id=id_p.id)
        # Agregar los objetos de provincia mediante la sesion 
        session.add(est)
#commit de transacciones   
session.commit()
# 0 = Codigo AMIE
# 1 = Nombre de la Institucion Educativa
# 2 = Codigo de division politica administrativa (Provincia)
# 3 = Provincia
# 4 = Codigo de division politica administrativa (Canton)
# 5 = Canton
# 6 = Codigo de division politica administrativa (Parroquia)
# 7 = Parroquia
# 8 = Codigo de Distrito
# 9 = Sostenimieto
# 10 = Tipo de Educacion
# 11 = Modalidad
# 12 = Jornada
# 13 = Acceso
# 14 = Numero de estudiantes
# 15 = Numero de Docentes