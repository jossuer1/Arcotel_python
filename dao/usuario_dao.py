class UsuarioDAO:
    def __init__(self, conn):
        self.conn = conn

    def obtener_usuarios(self):
        cursor = self.conn.cursor()
        query = "SELECT cedula, contraseña FROM empleados"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data