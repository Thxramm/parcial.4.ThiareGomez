compradores = {}

def validar_codigo(codigo):
    if len(codigo) < 6:
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if ' ' in codigo:
        return False
    return True

def comprar_entrada():
    nombre = input("Ingrese nombre de comprador: ")
    if nombre in compradores:
        print("El nombre ya existe. Intente nuevamente.")
        return
    
    tipo = input("Ingrese tipo de etrada (G/V): ")
    if tipo not in ['G', 'V', 'g', 'v']:
        print("Tipo de entrada no valido. Debe ser 'G' o 'V'.")

    while True:
        codigo = input("Ingrese el codigo de confirmacion: ")
        if validar_codigo(codigo):
            break
        else:
            print("Codigo no valido. Intente nuevamente.")
            
    compradores[nombre] = {"tipo": tipo, "codigo": codigo}
    print("Codigo valido. Entrada registrada con exito :D")

def consultar_comprador():
    nombre = input("Ingrese nombre de comprador a buscar: ")
    if nombre in compradores:
        datos = compradores[nombre]
        print(f"Tipo de entrada: {datos['tipo']}")
        print(f"Codigo de confirmación: {datos['codigo']}")
    else:
        print("El comprador no se encuentra.")

def cancelar_compra():
    nombre = input("Ingree nombre de comprador a cancelar: ")
    if nombre in compradores:
        del compradores[nombre]
        print("Compra cancelada con exito.")
    else:
        print("No se pudo cancelar la compra")

def menu():
    while True:
        print("\n~~~ MENÚ PRINCIPAL ~~~")
        print("1.~ Comprar entrada.")
        print("2.~ Consultar comprador.")
        print("3.~ Cancelar compra.")
        print("4.~ Salir.")
        opcion = input("Ingrese opcion: ")

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            consultar_comprador()
        elif opcion == "3":
            cancelar_compra()
        elif opcion == "4":
            print("Programa terminado.")
            break
        else:
            print("Opción invalida. Intente nuevamente.")

menu()
