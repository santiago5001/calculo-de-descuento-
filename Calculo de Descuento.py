"""
Crea una función llamada calcular_descuento que tome dos parámetros:
el monto total de la compra y un valor predeterminado para el porcentaje de descuento
 (por ejemplo, 25% por defecto).
La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
La función debe devolver el monto del descuento calculado.

Llamada a la Función:

Llama a la función: calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y, en la otra, proporciona
tanto el monto total de la compra como el porcentaje de descuento.
Salida de Resultados:

Muestra los resultados de las llamadas a la función, incluyendo el monto del descuento y el monto final a pagar después del descuento.
Subida del Código:"""

def calcular_descuento(monto_total, porcentaje_descuento= 25):
    descuento = monto_total * (porcentaje_descuento/100)
    return descuento
if __name__=="__main__":
    monto1 = 5000
    monto2 = 7000
    ## llamada
    descuento1 = calcular_descuento (monto1)
    print(f"Monto de la compra es {monto1}, el descuento es {descuento1}")

    # llamada 2
    descuento2 = calcular_descuento(monto2,20)
    print(f"Monto de la compra es {monto2}, el descuento es {descuento2}")

