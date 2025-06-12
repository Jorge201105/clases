



class Medicamento:
    descuento = 0.05
    iva = 0.19




    @staticmethod
    def validar_mayor_a_0(numero):
        return numero > 0


m1 = Medicamento()
m2 = Medicamento()

if m1.iva == m2.iva and m1.descuento == m2.descuento:
    print("todas las instancias son iguales")
    print(f"el iva es {Medicamento.iva}")
    print(f"el descuento es {Medicamento.descuento}")


