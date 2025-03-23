def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (int, optional): El porcentaje de descuento a aplicar. Defaults to 10.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Ejemplo de como se utiliza la funcion.
monto1 = 100
monto2 = 200
descuento_porcentaje = 20

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, descuento_porcentaje)

monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

print(f"Para un monto de ${monto1}, el descuento es de ${descuento1} y el monto final es de ${monto_final1}")
print(f"Para un monto de ${monto2}, el descuento es de ${descuento2} y el monto final es de ${monto_final2}")