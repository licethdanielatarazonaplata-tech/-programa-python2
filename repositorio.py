
#nombre: Liceth Daniela Tarazona Plata
#grupo: 213022_305
#programa: Fundamentos de programación
#código de fuente: Autoría propia


# Matriz: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    [101, "Teclado", 8, 15],
    [102, "Mouse", 20, 10],
    [103, "Monitor", 5, 8],
    [104, "Memoria USB", 12, 12],
    [105, "Impresora", 2, 6]
]
# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Mostrar lista de pedidos
print("=== LISTA DE REABASTECIMIENTO ===")

for articulo in inventario:
    
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_pedido(stock_actual, stock_minimo)

    print("Artículo:", nombre)
    print("Cantidad a solicitar:", cantidad)
    print("-------------------------")