lista_productos=[]

def validaCodigo(cod):
    try:
        c = int(cod)
        if c > 0:
            return True
        return False
    except:
        return False

def validar_nombre(nom):
    if len(nom.strip())>=3:
        return True
    return False


def validarPrecio(precio):
    try:
        p=int(precio)
        if p>100 and p<=50000:
            return True
        return False
    except:
        return False


def ingresarproducto(lista):
    codigo=input("ingrese codigo del producto: ")
    resp=validaCodigo(cod=codigo)
    if resp == False:
        print("Ingrese codigo numerico entero mayor a cero")
        return False
    nombre=input("Ingrese nombre del producto:")
    resp=validar_nombre(nombre)
    if resp==False:
        print("Nombre sin espacio y minimo 3 letras")
        return False
    precio=input("ingrese precio del producto: ")
    resp=validarPrecio(precio)
    if resp==False:
        print("precio debe ser un numero entre 100 y 50000")
    
    producto={
        "codigo": int(codigo),
        "nombre": nombre,
        "precio": int(precio)
    }
    lista.append(producto)
    return True

def menu():
    print("== menu almacen ==")
    print("1. Ingresar")
    print("2. Listar ")
    print("3. salir")
    
def selecicione():
    try:
        op=int(input("seleccione:"))
        return op
    except:
        print("opcion incorrecta, ingrese solo numero")
        return 0

def rutas (op):
    match op:
        case 1:
            print("== Ingresar ")
        case 2:
            print("== listar ==")
        case 3:
            print("== salir ==")

ciclo=True
while ciclo:
    menu()
    opcion= selecicione()
    rutas(opcion)
    if opcion==3:
        ciclo=False