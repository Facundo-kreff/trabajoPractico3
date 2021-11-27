#2019_AED_TP2_Kreff_80791[1k11]

import random

#Creacion De Registro
#El Registro crea los datos automaticamente
class Articulo():
    def __init__(self, busq):
        self.producto = busq
        self.codigo = random.randint(00000,99999)
        self.precio = float(random.randint(100,100000))
        self.ubicacion = random.choice(("Buenos Aires","Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos"
                                        , "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén"
                                        , "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe"
                                        , "Santiago del Estero", "Tierra del Fuego", "Tucumán"))
        self.estado =  random.choice(("Nuevo","Usado"))
        self.cantidad = random.randint(1,500)
        self.puntuacion = random.choice(("1- Mala", "2- Normal", "3- Buena","4- Muy Buena", "5- Exelente"))

#Funcion De Carga De Datos
def carga(v, art):
    for i in range(len(v)):
        v[i] = Articulo(art)

#Funcion para ordenar el arreglo de registrp
def ordenar(v):
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

#Funcion PAra mostrar
def mostrar(v):
    for i in range(len(v)):
        print ("\033[1;34m"+"\n------------------------------")
        print ("Producto: ", v[i].producto)
        print ("Codigo De Publicacion: ", v[i].codigo)
        print ("Precio: $", v[i].precio)
        print ("Ubicacion: ", v[i].ubicacion)
        print ("Estado: ", v[i].estado)
        print ("Cantidad Disponible: ", v[i].cantidad)
        print ("Puntuacion Del Vendedor: ", v[i].puntuacion)
        print ("------------------------------"+'\033[0;m')

#Opcion 1
def ordenar_precio(v):
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            if v[i].precio > v[j].precio:
                v[i], v[j] = v[j], v[i]
    mostrar(v)

def opcion_1(v):
    registro=[]
    for i in range(len(v)):
        if v[i].estado == "Nuevo":
            registro.append(v[i])
    ordenar_precio(registro)

#Opcion 2
def opcion_2(v):
    can1, can2, can3, can4, can5 = 0, 0, 0, 0, 0
    for i in range(len(v)):
        if v[i].puntuacion == "1- Mala":
            can1+=1
        elif v[i].puntuacion == "2- Normal":
            can2+=1
        elif v[i].puntuacion == "3- Buena":
            can3+=1
        elif v[i].puntuacion == "4- Muy Buena":
            can4+=1
        elif v[i].puntuacion == "5- Exelente":
            can5+=1
    print("\033[4;30m"+"\nCantidad de publicaciones en estado usado por cada puntuacion de vendedor"+'\033[0;m')
    print("-",can1,"Publicacion de 1 punto")
    print("-",can2,"Publicacion de 2 puntos")
    print("-",can3,"Publicacion de 3 puntos")
    print("-",can4,"Publicacion de 4 puntos")
    print("-",can5,"Publicacion de 5 puntos")

#opcion 3
def opcion_3(v):
    matriz = [[0] * 23 for i in range(5)]
    


#opcion 4
def opcion_4(v):
    print()

#opcion 5
def opcion_5(v):
    registro=[]
    suma = 0
    for i in range(len(v)):
        suma+=v[i].precio
    promedio = suma / len(v)
    for i in range(len(v)):
        if v[i].estado == "Usado":
            registro.append(v[i])
    print("\n")
    mostrar(registro)

#opcion 6
def menor_precio(v):
    menor=[]
    if len(v) == 0:
        menor="No Se Encuentra Resultado"
        print (menor)
    else:
        for i in range(len(v)):
            for j in range(len(v)):
                if v[i].precio > v[j].precio:
                    menor = v[j]
                else:
                    menor = v[i]
        print ("\033[1;34m"+"\n------------------------------")
        print ("Producto: ", menor.producto)
        print ("Codigo De Publicacion: ", menor.codigo)
        print ("Precio: $", menor.precio)
        print ("Ubicacion: ", menor.ubicacion)
        print ("Estado: ", menor.estado)
        print ("Cantidad Disponible: ", menor.cantidad)
        print ("Puntuacion Del Vendedor: ", menor.puntuacion)
        print ("------------------------------"+'\033[0;m')

def opcion_6(v):
    registro=[]
    for i in range(len(v)):
        if v[i].estado == "Nuevo" and v[i].puntuacion != "1- Mala":
            registro.append(v[i])
    menor_precio(registro)


#opcion 7
def opcion_7(v):
    compra=[]
    x = int(input("Ingrese Codigo: "))
    for i in range(len(v)):
        if v[i].codigo == x :
            compra.append(v[i])
    if lend(compra) == 0:
        print("NO EXISTE")
    else:
        articulos=int(input("Ingrese la cantidad ed articulos que desea comprar: "))
        if compra[0].cantidad < articulos :
            print ("No se pudo realizar la compra. NO HAy suficientes articulos ")
        else:
            print ("Compra Realizada.")


#Funcion Principal

def test():
    print("\033[4;30m"+"MERCADO LIBRE"+'\033[0;m')
    art=input("Ingrese el Nombre Del Articulo Que Decea Buscar: ")
    n =int(input("Ingrese la Cantida De Resultados Que Quiere: "))
    v = [None] * n
    carga(v,art)
    ordenar(v)
    mostrar (v)
    op = 0
    #Menu de opciones
    while op != 8:
        print("\nOpciones:")
        print ("1-Nuevos por precio.")
        print ("2-Usados por calificacion.")
        print ("3-Distribucion geografica.")
        print ("4-Total provincial.")
        print ("5-Precio promedio de usados.")
        print ("6-Compra ideal.")
        print ("7-Comprar.")
        print ("8-Salir.")
        op=int(input("\nIngrese Numero De Opcion: "))
        if op == 1:
            opcion_1(v)
        elif op == 2:
            opcion_2(v)
        elif op == 3:
            opcion_3(v)
        elif op == 4:
            opcion_4(v)
        elif op == 5:
            opcion_5(v)
        elif op == 6:
            opcion_6(v)
        elif op == 7:
            opcion_7(v)
        elif op == 8:
            print ("\nQue Tenga Buen Dia ;)")

test()










