


class contacto:
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


class ContactoTrabajo(contacto):
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
        self.contactos:list[contacto] =[]

    def agregar_contacto(self,contacto:contacto):
        self.contactos.append(contacto)

    def listar_contactos(self)-> list[contacto]:
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


