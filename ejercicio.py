from medicamento import Medicamento








paracetamol = Medicamento()


print(paracetamol.descuento) # entrega el valor de descuento
print(paracetamol.iva)# entrega el valor de iva

precio =int(input("ingresa un valor"))

print(paracetamol.validar_mayor_a_0(precio))

