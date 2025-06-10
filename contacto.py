import os


class Contacto:
    """
    Nombre , e mail, telefono, 
    
    """
    def __init__(self, nombre:str,email:str,telefono:str)-> None:
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def email(self):
        return self.__email
    @property
    def telefono(self):
        return self.__telefono
    
    #mostrar todo
   # def mostrar_obj(self):
    #    return f"nombre :{self.nombre}, email :{self.email}, telefono :{self.telefono}"

    def __repr__(self):
        return repr(f"nombre :{self.nombre}, email :{self.email}, telefono :{self.telefono}")


class ContactoTrabajo(Contacto):
    #constructor del contacto trabajo
    def __init__(self, nombre, email, telefono, empresa, oficio):
        #constructor de contacto()
        super().__init__(nombre, email, telefono)
        self.__empresa = empresa
        self.__oficio = oficio

    @property
    def empresa(self):
        return self.__empresa

    @property
    def oficio(self):
        return self.__oficio

     #mostrar todo
    def __repr__(self):
        
        return repr(f"{self.nombre},empresa:{self.email},oficio:{self.telefono} {self.oficio} {self.empresa}")

"""
cliente = ContactoTrabajo("juan","correo@ghg","26276246","claro","jardinero")
print(cliente.mostrar_obj())
 """   

"""    
contacto = contacto("luis", "hola@email","hola")

print(contacto.email)
"""        
        
class Manejador:
    def __init__(self):
        self.contactos:list[Contacto] =[]

    def agregar_contacto(self,contacto:Contacto):
        self.contactos.append(Contacto)

    def listar_contactos(self)-> list[Contacto]:
        return self.contactos
    

    def buscar_contacto(self, nombre):
        nombre_minuscula = nombre.lower()
        for i in self.contactos:
            if i.nombre.lower() == nombre_minuscula:
                return i
        return None


    
    def borrar_contacto(self):
        contacto = self.buscar_contacto(nombre) # type: ignore
        if contacto is not None:
            self.contactos
    

class Consola_menu:
    # 1.- limpiar la cionsola
    # 2.- mostrar menu

    @staticmethod
    def limpiar_consola():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def mostar_menu():
        print("""

===Menu Contactos ===
              
1.- Agregar contacto
2.- Agregar contacto trabajo
3.- Listar contactos
4.- Buscar usuario
5.- Actualizar usuario
6.- Eliminar usuario
8.- salir
        """)

class Pedir_datos:

    @staticmethod
    def contcto_normal():
        nombre = input("nombre :")
        email = input("email :")
        telefono = input("telefono :")
        return Contacto(nombre, telefono, email)


    @staticmethod
    def contacto_empresa():
        nombre = input("nombre :")
        email = input("email :")
        telefono = input("telefono :")
        empresa = input("empresa :")
        oficio = input(" oficio")
        
        return ContactoTrabajo(nombre, telefono, email, empresa, oficio)


class App:
    def __init__(self):
        self.manejador = Manejador()


    def run(self):
        while True:
            Consola_menu.limpiar_consola()
            Consola_menu.mostar_menu()

            opcion = input("Elige una opcion : ")
            if opcion == "1":
                c = Pedir_datos.contcto_normal() # type: ignore
                self.manejador.agregar_contacto(c)
                print("contacto agregado !! ")
                input ("enter para contunuar")

            elif opcion == "2":
                ct = Pedir_datos.contacto_empresa()
                self.manejador.agregar_contacto(ct)
                print("contacto agregado !")
                input(" enter para continuar")

            elif opcion == "3":
                contactos = self.manejador.listar_contactos()
                if contactos:     # si hay contactos esto lo toma como un sí
                    for i in contactos:
                        print(i)
                else:
                    print("sin contactos")












"""  
contacto_manejador = Manejador()

contacto1 = contacto("juan","correo electronico", "3675346")
contacto2 = contacto("juan","correo electronico", "4345")
contacto3 = contacto("juan","correo electronico", "56456")

contacto4 = ContactoTrabajo("juan","correo electronico", "456456", "trrf,"kjhg")
contacto5 = ContactoTrabajo("juan","correo electronico", "567","ytfytf","jfgytf")
contacto6 = ContactoTrabajo("juan","correo electronico", "856","hgfr","hgfytf")



contacto_manejador.agregar_contacto(contacto1) 
contacto_manejador.agregar_contacto(contacto2)
contacto_manejador.agregar_contacto(contacto3)
contacto_manejador.agregar_contacto(contacto4)
contacto_manejador.agregar_contacto(contacto5)
contacto_manejador.agregar_contacto(contacto6)


nombre = input()
dato = contacto_manejador.agregar_contacto()





print(contacto_manejador.listar_contactos())
print(dato)

"""
