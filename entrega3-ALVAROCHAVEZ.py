inventario = []
stock = {
    'FICCION' : 15,
    'NO_FICCION' : 19,
    'CIENCIA' : 23
}
generoTexto = ('FICCION','NO FICCION','CIENCIA')
ventas = []

def registroInventario():
    tituloLibro = input("INGRESE TÍTULO LIBRO: ").upper()
    while tituloLibro == "":
        print("NO HA INGRESADO NINGÚN TÍTULO. INTENTE NUEVAMENTE.")
        tituloLibro = input("INGRESE TÍTULO LIBRO: ")
    print("REGISTRO CON ÉXITO.")
    print("********************")

    autorLibro = input("INGRESE AUTOR LIBRO: ").upper()
    while autorLibro == "":
        print("NO HA INGRESADO NINGÚN AUTOR. INTENTE NUEVAMENTE.")
        autorLibro = input("INGRESE AUTOR LIBRO: ")
    print("REGISTRO CON ÉXITO.")
    print("********************")
    
    generoLibro = input("INGRESE GÉNERO LIBRO: ").upper()
    while generoLibro == "":
        print("NO HA INGRESADO NINGÚN GÉNERO. INTENTE NUEVAMENTE.")
        generoLibro = input("INGRESE GÉNERO LIBRO: ")
    print("REGISTRO CON ÉXITO.")
    print("********************")

    precioLibro = int(input("INGRESE VALOR LIBRO: "))
    while precioLibro == "":
        print("NO HA INGRESADO VALOR LIBRO. INTENTE NUEVAMENTE.")
        precioLibro = int(input("INGRESE VALOR LIBRO: "))
    print("REGISTRO CON ÉXITO.")
    print("********************")

    inventario.append({
        'titulo' : tituloLibro,
        'autor' : autorLibro,
        'genero' : generoLibro,
        'precio' : precioLibro
    })


def listarInventario():
    print("*****LISTADO REGISTRO INVENTARIO*****")
    for producto in inventario:
        print(producto)

def registrarVentas():
    tituloVenta = input("INGRESE TÍTULO LIBRO VENDIDO: ").upper
    if tituloVenta in inventario:
        print("LIBRO EN INVENTARIO")
    elif tituloVenta not in inventario:
        print("LIBRO NO REGISTRADO")
    else:
        print("VUELVA A INTENTARLO")
    
    

def imprimirReporte():
    print()


while True:
    try:
        print("*****MENÚ PRINCIPAL LIBRERÍA 'VIÑA DEL MAR'*****")
        print("""[1] REGISTRO INVENTARIO
[2] LISTAR INVENTARIO
[3] REGISTRO VENTAS
[4] IMPRESIÓN REPORTE DE VENTAS
[5] SALIR MENÚ PRINCIPAL""")
        opMenu = int(input("INGRESE OPCIÓN A REALIZAR: "))
        print("********************")

        if opMenu == 1:
            registroInventario()

        elif opMenu == 2:
            listarInventario()

        elif opMenu == 3:
            registrarVentas()

        elif opMenu == 4:
            imprimirReporte()

        elif opMenu == 5:
            break
        else:
            print("OPCIÓN NO EXISTE. INTENTE NUEVAMENTE.")


        
    
    except ValueError:
        print("OPCIÓN INVÁLIDA. INTENTE NUEVAMENTE.")

