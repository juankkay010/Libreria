import sys
from Libreria.mundo.libreria import Biblioteca


class Consola:

    def __init__(self):
        self.libreria = Biblioteca()
        self.opciones = {
            "1": self.registrar_usuario,
            "2": self.registrar_prestamo,
            "3": self.buscar_libro
        }

    def mostar_menu(self):
        print("""
        \n
        BIENVENIDO A LA BIBLIOTECA POOSITIVA
        ===================================
        Menú de opciones:\n
        1. Registrar usuario
        2. Registrar prestamo
        3. Buscar Libro
        4. Salir
        ===================================
        """)

    def ejecutar(self):
        while True:
            self.mostar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"ERROR: {opcion} no es una opción válida")

    def registrar_usuario(self):
        print("\n>>> REGISTRAR USUARIO")
        cedula = input("Ingrese la cédula: ")
        nombre = input("Ingrese el nombre: ")
        if self.libreria.registrar_usuario(cedula, nombre):
            print("INFO: El usuario se registró exitosamente")
        else:
            print(f"ERROR: Ya existe un usuario con la cédula {cedula}")

    def registrar_prestamo(self):
        print("\n>>> LISTADO DE PRODUCTOS")
        for producto in self.libreria.libros.values():
            print(producto)

    def buscar_libro(self):
        print("BUSQUEDA DE LIBRO")
        scib = input("Ingrese el codigo del libro: ")
        if self.libreria.buscar_libro(scib):
            print(f"LIBRO: {self.libreria.libros[scib]}")
        else:
            print("No se encuentra el libro")



    def salir(self):
        print("\nMUCHAS GRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)
