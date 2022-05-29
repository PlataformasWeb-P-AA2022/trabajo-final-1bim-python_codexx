from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# Se crea el enlace del gestor de base de datos
# BDD: SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivos
with open('../data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    # Omitir la primera fila del csv 
    next(reader)
    # Lista donde se guardan las provincias (vacia)
    provincias=[]

    # Ciclo repetitivo sobre el archivo csv para poder llenar las entidades 
    for i in reader:
        if i[3] not in provincias:
            # Se agregan las provincias
            provincias.append(i[3])
            # Creación del objeto de tipo Provincia
            prov= Provincia(nombre=i[3], cod_division_politica=i[2]) 
            # Agregar los objetos de provincia mediante la sesion 
            session.add(prov)
# commit de transacciones
session.commit()