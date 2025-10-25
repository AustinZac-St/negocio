class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def stock(self, stock, cantidad_producto, nombre):
        self.cantidad_producto = stock

class Productos:
    def __init__(self) -> None:
        self.inventario = []

    def agregar_producto(self,producto):
        self.inventario.append(producto)

    def encontrar_producto(self,nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                print("Se encontro el ",producto.stock)

productos = Productos()

mandarina = Producto("Mandarina",200,10)

productos.agregar_producto(mandarina)

print(productos.encontrar_producto("Mandarina"))