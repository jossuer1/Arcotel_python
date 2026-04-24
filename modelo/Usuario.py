class Usuario:
    def __init__(self, id=None, nombre=None, apellido=None, cedula=None, password=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.password = password

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"