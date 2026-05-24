import pymysql
import streamlit as st

# Datos de conexión
config = {
    "host": "mysql-1acf5854-juanantoniolobillo-8121.e.aivencloud.com",
    "port": 19559,
    "user": "avnadmin",
    "password": "AVNS_5mPcs7yPojZ3h6FiB8w",
    "database": "defaultdb",
    "ssl": {"fake_flag_to_enable_ssl": True},
    "connect_timeout": 10
}

def crear_tabla():
    conexion = pymysql.connect(**config)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            email VARCHAR(100),
            edad INT
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)",
            [
                ("Ana García", "ana@email.com", 25),
                ("Carlos López", "carlos@email.com", 30),
                ("María Martínez", "maria@email.com", 22),
                ("Juan Pérez", "juan@email.com", 35),
            ]
        )
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_datos():
    conexion = pymysql.connect(**config)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

# Interfaz Streamlit
st.title("Panel de Usuarios")
st.write("Datos almacenados en MySQL en Aiven")

if st.button("Cargar datos"):
    try:
        crear_tabla()
        datos = obtener_datos()
        st.success("Conectado correctamente")
        st.table(datos)
    except Exception as e:
        st.error(f"Error de conexión: {e}")