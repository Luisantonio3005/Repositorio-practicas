# Crear una clase llamada celular con atributos como marca, modelo, color, almacenamiento y cámara
class celular():
    def __init__(self, marca, modelo, color, almacenamiento, camara):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento
        self.camara = camara

# Definir métodos para llamar y cortar la llamada
    def llamar(self):
        print(f'Estas llmando desde un: {self.modelo}')

    def cortar(self):
        print(f'Colgando la llamada desde un {self.modelo}')
  
# Crear objetos de la clase celular con diferentes atributos para cada uno
celular1 = celular("Samsung", "Galaxy S", "blue", "128GB", "12MP")
celular2 = celular("Apple", "iPhone 13", "black", "256GB", "12MP")
celular3 = celular("Xiaomi", "Redmi Note 10", "white", "64GB", "48MP")
celular4 = celular("Huawei", "P40", "green", "128GB", "50MP")
celular5 = celular("Nokia", "3310", "gray", "16MB", "2MP")

# Imprimir los atributos de cada objeto

celular1.llamar()

print (f"los datos del celular son:")
print(celular1.marca)
print(celular1.modelo)
print(celular1.color)
print(celular1.almacenamiento)
print(celular1.camara)

celular2.cortar()

print (f"los datos del celular son:")
print(celular2.marca)
print(celular2.modelo)
print(celular2.color)
print(celular2.almacenamiento)
print(celular2.camara)