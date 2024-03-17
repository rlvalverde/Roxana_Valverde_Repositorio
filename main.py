def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Función para calcular el descuento aplicando un porcentaje al monto total de la compra.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def main():
    """
    Función principal del programa.
    """
    # Llamada a la función con solo el monto total de la compra
    monto_compra1 = 1000
    descuento1 = calcular_descuento(monto_compra1)
    monto_final1 = monto_compra1 - descuento1
    print(f"Monto del descuento: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}")

    # Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
    monto_compra2 = 2000
    porcentaje_descuento2 = 15
    descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
    monto_final2 = monto_compra2 - descuento2
    print(f"\nMonto del descuento con {porcentaje_descuento2}% de descuento: ${descuento2:.2f}")
    print(f"Monto final a pagar con {porcentaje_descuento2}% de descuento: ${monto_final2:.2f}")

if __name__ == "__main__":
    main()

