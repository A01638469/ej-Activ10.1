def precio_antes_descuento(tipo_silla, cantidad) :
    # Agrega aquí el código de la funcion
    if tipo_silla == 'B':
        return 700.0 * cantidad
    elif tipo_silla == 'E':
        return 900.0 * cantidad
    elif tipo_silla == 'L':
        return 1500.0 * cantidad

def calcula_descuento(precio, tipo_cl) :
    # Agrega aquí el código de la funcion
    if tipo_cl == 'N':
        if precio >= 10000 and precio < 20000:
            return precio * 0.1
        elif precio >= 20000:
            return precio * 0.15
        else:
            return 0.0
    elif tipo_cl == 'F':
        return precio * 0.2

    

def main() :
    # pido el tipo de silla (B E L)
    tipo_silla = input("Tipo silla: ")
    # pido el tipo de cliente (N F)
    tipo_cl = input("Tipo cliente: ")
    cantidad = int(input("Cantidad de sillas: "))

    subtotal = precio_antes_descuento(tipo_silla, cantidad)
    desc = calcula_descuento(subtotal, tipo_cl)
    total = subtotal - desc

    print(f"Total sin dcto.  ${subtotal:>7}")
    print(f"Descuento        ${desc:>7}")
    print(f"Total a pagar    ${total:>7}")

if __name__=='__main__':
    main()
