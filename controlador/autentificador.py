class Autentificador:
    def __init__(self, usuario_dao):
        self.usuario_dao = usuario_dao

    def auth(self, cedula, password):

        usuarios = self.usuario_dao.obtener_usuarios()

        # Validaciones
        if not cedula or not password:
            return "Faltan datos"

        if not cedula.isdigit():
            return "Cédula solo números"

        if len(cedula) != 10:
            return "La cédula debe tener 10 dígitos"

        # Validar contra BD
        for c, p in usuarios:
            if c == cedula and p == password:
                return "OK"

        return "Credenciales incorrectas"