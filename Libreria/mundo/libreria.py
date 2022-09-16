class Libro:

    def __str__(self):
        return f"{self.scib}-{self.titulo}-{self.disponibilidad}-{self.precio}"


    def __init__(self, scib:str, titulo: str, disponibilidad: bool, precio: str):
        self.scib= scib
        self.titulo= titulo
        self.disponibilidad= disponibilidad
        self.precio = precio

class Biblioteca:


    def __init__(self):
        self.total_prestados = 0
        self.total_vendidos = 0
        self.total_devueltos= 0
        self.usuarios = {}
        self.libros = {}


    def eliminar_libro(self, scib: str):
        self.libros.pop(scib)

    def cargar_libros(self):
        self.libros["216676"]=Libro("216676",
                                    "código limpio",
                                    True,
                                    "85000")

        self.libros["786534"]=Libro("786534",
                                    "lenguajes II",
                                    True,
                                    "32000")

        self.libros["396784"]=Libro("396784",
                                    "fundamentos de programación",
                                    True,
                                    "56000")

    def buscar_libro(self, scib: str):
       if scib in self.libros.keys():
           return self.libros[scib]
       else:
           return None








    def registrar_usuario(self, dni: int, nombre: str) -> bool:
        if self.buscar_usuario(dni) is None:
            usuario=Usuario(dni, nombre)
            self.usuarios[dni]=usuario
            return True
        else:
            return False

    def buscar_usuario(self, dni: str):
        if dni in self.usuarios.keys():
            return self.usuarios[dni]
        else:
            return None


class Usuario:

    def __init__(self, dni: int, nombre: str):
        self.dni: int = dni
        self.nombre: str = nombre
        self.bolsa= Bolsa()


class Prestado:


    def __init__(self, scib: int, dia: int, mes: str):
        self.scib= scib
        self.dia= dia
        self.mes= mes
        self.prestados={}

    def agregar_a_prestados(self, dni:str, scib: str):
        self.prestados[dni]= Biblioteca
class Bolsa:
    pass
class Ejemplar:
    pass