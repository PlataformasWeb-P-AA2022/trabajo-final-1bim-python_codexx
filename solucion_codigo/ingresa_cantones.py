from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas
from genera_tablas import Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se crea el enlace del gestor de base de datos
# BDD: SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivo
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    # No tomar en cuenta la primera fila del csv
    next(reader)

    # Lista donde se guardan los cantones (vacia)
    cantones=[]

    # Ciclo repetitivo sobre el archivo csv para poder llenar las entidades 
    for row in reader:
        # Condicional para evitar que se guarden valores repetidos
        if row[5] not in cantones:
            # Agrega los cantones la lista cantones
            cantones.append(row[5])
            # Variable para guardar la provincia de la consulta para obtener el id y agregarlo al canton
            id_p= session.query(Provincia).filter_by(nombre = row[3]).first()  

            # Creación del objeto de tipo Canton
            can = Canton(nombre=row[5], cod_division_politica=row[4], provincia_id=id_p.id)

            #Agregar el objeto Canton mediante la sesion
            session.add(can)
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