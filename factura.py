# 1. Base de datos con tus 15 productos e IVA actualizados
productos = [
    "Jugo", "Chocolate", "Agua", "Galletas", "Pan", 
    "Leche", "Café", "Arroz", "Azúcar", "Sal", 
    "Azucar", "Huevos", "Papas", "Pasta", "Carne"
]
precios = [
    2500, 1800, 1000, 1200, 4000, 
    1500, 3000, 2000, 1100, 1500, 
    1700, 600, 1500, 3000, 5000
]

IVA = 0.19

# Listas vacías para el carrito del usuario
carrito_nombres = []
carrito_precios = []

print("--- MENÚ DE PRODUCTOS DISPONIBLES ---")
# Cambiamos a range(15) porque ahora tienes 15 elementos (del 0 al 14)
for i in range(15):
    # Formateamos el precio con {precios[i]:,} para que ponga puntos de miles (ej: 2,500 o 2.500)
    print(f"[{i}] {productos[i]} - ${precios[i]:,}")

print("\n" + "="*40)

# 2. Ciclo de compras
comprando = True

while comprando:
    opcion = int(input("Ingresa el número del producto (o -1 para pagar): "))
    
    if opcion == -1:
        comprando = False
    # Cambiamos la validación: ahora el número válido debe estar entre 0 y 14
    elif 0 <= opcion <= 14:
        carrito_nombres.append(productos[opcion])
        carrito_precios.append(precios[opcion])
        print(f"¡Agregado! -> {productos[opcion]} (${precios[opcion]:,})")
    else:
        print("Número inválido. Intenta de nuevo (0 al 14).")
        
    print("-" * 40)

# 3. Factura Final
print("\n" + "="*40)
print("         FACTURA DE COMPRA         ")
print("="*40)

if len(carrito_precios) == 0:
    print("No compraste ningún producto.")
else:
    # Imprime los productos comprados
    for i in range(len(carrito_nombres)):
        print(f"{carrito_nombres[i]} - ${carrito_precios[i]:,}")
    
    print("-" * 40)
    
    # Cálculos
    subtotal = sum(carrito_precios)
    valor_iva = subtotal * IVA
    total_pagar = subtotal + valor_iva

    # Mostramos los resultados con formato de miles sin decimales
    print(f"Subtotal ({len(carrito_precios)} prod):   ${subtotal:,.0f}")
    print(f"IVA ({IVA * 100}%):             ${valor_iva:,.0f}")
    print(f"TOTAL A PAGAR:          ${total_pagar:,.0f}")

print("="*40)

