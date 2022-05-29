from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import  Canton, Parroquia
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

    #  No tomar en cuenta la primera fila del csv
    next(reader)

    # Lista donde se guardan las parroquias (vacia)
    parroquia=[]    

    # Ciclo repetitivo sobre el archivo csv para poder llenar las entidades 
    for row in reader:
          # Condicional para evitar que se guarden valores repetidos
        if row[7] not in parroquia:
            # Agrega las parroquias a la lista parroquia
            parroquia.append(row[7]) 
            # Variable para guardar el canton de la consulta para obtener el id y agregarlo a la parroquia
            id_c= session.query(Canton).filter_by(nombre = row[5]).first()

            # Creación del objeto de tipo Parroquia
            par = Parroquia(nombre=row[7], cod_division_politica=row[6], codigo_distrito=row[8],canton_id=id_c.id)
           
            # Agregar los objetos de provincia mediante la sesion 
            session.add(par)

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