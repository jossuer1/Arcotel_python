from modelo.conexion import conectar
from dao.usuario_dao import UsuarioDAO
from controlador.autentificador import Autentificador
from vista.vista_login import LoginView
from logica.lectura_Archivos import lectura_archivos_exel
from controlador.insertar_datos import insertar_datos

def main():

    conn = conectar()

    usuario_dao = UsuarioDAO(conn)
    auth = Autentificador(usuario_dao)

    #  LOGIN
    login = LoginView(auth)
    login.run()

    # si login correcto
    #df = lectura_archivos_exel("data/Arcontel.xlsx")
    #insertar_datos(conn, df)

    conn.close()

if __name__ == "__main__":
    main()