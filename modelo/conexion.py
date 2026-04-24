import psycopg2

def conectar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="Arcotel",
            user="postgres",
            password="josueepn23"
        )
        return conexion

    except Exception as e:
        print("Error al conectar:", e)
        return None