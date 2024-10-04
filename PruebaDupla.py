inventario = [
    {"nombre": "Chupetín Sable de Luz", "cantidad": 50, "precio": 200},
    {"nombre": "Agua La Fuerza", "cantidad": 35, "precio": 3200},
    {"nombre": "Gomitas Holocubo", "cantidad": 25, "precio": 990},
    {"nombre": "Barrita de Cereal Wookie", "cantidad": 48, "precio": 2500},
    {"nombre": "Galletitas R2D2", "cantidad": 20, "precio": 15800}
]

def validar_numero(mensaje, tipo):
    while True:
        try:          #Creo que no vimos el comando try, pero creo qu es la mejor forma, ya que sino tendria que hacer el doble de if, elif, else y return
            valor = tipo(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Debes ingresar un número válido. Intenta de nuevo.")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = validar_numero("Precio del producto: ", float)
    cantidad = validar_numero("Cantidad del producto: ", int)
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print(f'Producto "{nombre}" agregado al inventario.')

def realizar_venta():
    mostrar_productos()
    nombre = input("Nombre del producto a vender: ")
    cantidad = validar_numero("Cantidad a vender: ", int)
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                total = producto["precio"] * cantidad
                print(f'Venta realizada: {cantidad} de "{nombre}" - Total a pagar: ${total:.2f}')
                return
            else:
                print('No hay suficiente stock para realizar la venta.')
                return
    print(f'Producto "{nombre}" no encontrado en el inventario.')

def mostrar_productos():
    if not inventario:
        print('No hay productos disponibles.')
    else:
        print("\nProductos disponibles:")
        for producto in inventario:
            print(f'{producto["nombre"]}: ${producto["precio"]:.2f} - Cantidad: {producto["cantidad"]}')

def mostrar_inventario():
    print("\nEstructura del inventario:")
    for producto in inventario:
        print(producto)

def menu_principal():
    while True:
        print("\n$--Menu Principal--$ :")
        print("1. Agregar producto al inventario")
        print("2. Realizar una venta")
        print("3. Mostrar productos disponibles")
        print("4. Ver estructura del inventario")
        print("5. Salir del sistema")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            realizar_venta()
        elif opcion == '3':
            mostrar_productos()
        elif opcion == '4':
            mostrar_inventario()
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

menu_principal()