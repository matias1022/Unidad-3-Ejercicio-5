from zope.interface import implementer
from ClaseInterfaz import interface
@implementer(interface)

class Coleccion:
    __listaColeccion=[]
    def __init__(self):
        self.__listaColeccion=[]

    def insertarElemento(self,objeto,lugar):
        try:
            self.__listaColeccion.insert(lugar,objeto)
        except:
            print("\nError")
  
    def agregarElemento(self,elemento):
        self.__listaColeccion.append(elemento)

    def mostrarElemento(self,lugar):
        try:
            print(self.__listaColeccion[lugar-1])

        except IndexError:
            print("\nError")