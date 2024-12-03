import pymysql
from dotenv import load_dotenv
import os

load_dotenv(override=True)  # Forzar recarga del archivo .env
# override=True

# Leer las credenciales de la base de datos desde el archivo .env
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT", 3306))
database_name = os.getenv("DB_NAME")



# Función para establecer la conexión a la base de datos
def conexion():
    try:
        db = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database_name,
            port=port,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = db.cursor()
        print("Conexión establecida con éxito.")
        return db, cursor
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise


def insertar(usuario, edad, sexo, nacionalidad, sentimental, laboral, descendencia, consulta):
    db, cursor = conexion() # llamaanterior funcion conexion y declara db y cursor
    use_db = ''' USE pgf3712_2_database'''   # lee la mia
    cursor.execute(use_db)                             # ejecuta cursor
    cursor.execute('''
    INSERT INTO registro (usuario, edad, sexo, nacionalidad, sentimental, laboral, descendencia, consulta)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''',
    (usuario, edad, sexo, nacionalidad, sentimental, laboral, descendencia, consulta))
    # print("ok")
    db.commit()
    db.close()

























