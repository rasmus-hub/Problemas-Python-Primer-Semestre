# Diseña un programa que lea el precio de un producto y calcule el precio con IVA (19%)

precio_producto = int(input('Ingrese el precio del producto: '))
print(f'El precio del producto ${precio_producto} con IVA aplicado son ${(precio_producto * 0.19) + precio_producto:.0f}')