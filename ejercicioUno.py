class Coctel:
    def __init__(self, nombre, precio, grados_alcohol):
        self.nombre = nombre
        self.precio = precio
        self.grados_alcohol = grados_alcohol


class CoctelConFruta(Coctel):
    def __init__(self, nombre, precio, grados_alcohol, frescura):
        super().__init__(nombre, precio, grados_alcohol)
        self.frescura = frescura

    def calcular_costo_venta(self, cantidad, dias_anejamiento):
        if dias_anejamiento <= 0:
            return cantidad * self.precio
        elif dias_anejamiento == 1:
            return cantidad * self.precio
        elif dias_anejamiento == 2:
            return (cantidad * self.precio) - (0.2 * cantidad * self.precio)
        elif dias_anejamiento == 3:
            return (cantidad * self.precio) - (0.5 * cantidad * self.precio)
        else:
            print("Pasados tres dias de añejamiento no se venden el coctel")


class ShotAlcohol(Coctel):
    def __init__(self, nombre, precio, grados_alcohol, temperatura):
        super().__init__(nombre, precio, grados_alcohol)
        self.temperatura = temperatura

    def calcular_costo_venta(self, cantidad):
        return cantidad * self.precio


cocteles = [
    CoctelConFruta("Coctel con fruta -  Margarita de sandia - Precio: 20.000", 20000, 5, "Fresco"),
    CoctelConFruta("Coctel con fruta - Coco Tropical - Precio: 25.000", 25000, 8, "Medio fresco"),
    ShotAlcohol("Shot Ron - Precio: 7.000", 7000, 4, "Frío"),
    ShotAlcohol("Shot Aguardiente - Precio: 5.000", 5000, 3, "Templado"),
]


for i, coctel in enumerate(cocteles):
    print(f"{i + 1}. {coctel.nombre}")


opcion = int(input("Selecciona el número del coctel que deseas comprar: "))


if opcion <= 2:
    cantidad = int(input("Ingresa la cantidad que deseas comprar: "))
    dias_anejamiento = int(input("Ingresa los días de añejamiento (0 si es fresco maximo 3): "))
    coctel_seleccionado = cocteles[opcion - 1]
    costo_venta = coctel_seleccionado.calcular_costo_venta(cantidad, dias_anejamiento)
    if dias_anejamiento <= 3:
     print(f"El costo total de la venta es: {costo_venta}")
else:
    cantidad = int(input("Ingresa la cantidad que deseas comprar: "))
    coctel_seleccionado = cocteles[opcion - 1]
    costo_venta = coctel_seleccionado.calcular_costo_venta(cantidad)
    print(f"El costo total de la venta es: {costo_venta}")







