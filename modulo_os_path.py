#**********pasar varios argumentos y varios argumentos de diccionario**************
# def calculadora_numeros(*numeros):#*args
#     resultado = 1
#     for numero in numeros:
#         resultado *= numero
#     return resultado
# Podemos pasarle cualquier cantidad de números:
#----print(calculadora_numeros(2, 3, 4))  # Salida: 24

# def registrar_producto(**detalles):#**kargs
#     for clave, valor in detalles.items():
#         print(f"{clave} = {valor}")
# Pasamos argumentos con nombre libremente:
#----registrar_producto(nombre="Laptop", precio=800, ram="16GB")
# Salida:
# nombre = Laptop
# ram = 16GB
# precio = 800

# def hacer_pedido(ingrediente_principal, *otros_ingredientes):
#     print(f"Preparando pizza de: {ingrediente_principal}")
    
#     if otros_ingredientes:
#         print("Ingredientes adicionales:")
#         for ingrediente in otros_ingredientes:
#             print(f"- {ingrediente}")
# Ejemplo de uso:
#---hacer_pedido("queso", "peperoni", "champiñones", "aceitunas")

# def registrar_viaje(destino, *lugares_visita, **detalles_adicionales):#*args y *kargs en una funcion
#     print(f"✈️ Destino principal: {destino}")
    
#     # *args agrupa los lugares adicionales en una tupla
#     if lugares_visita:
#         print("📍 Lugares planeados para visitar:")
#         for lugar in lugares_visita:
#             print(f"  - {lugar}")
            
#     # **kwargs agrupa los detalles en un diccionario
#     if detalles_adicionales:
#         print("detalles adicionales")
#         for clave, valor in detalles_adicionales.items():
#             print(f"  - {clave.capitalize()}: {valor}")

# Llamando a la función combinando todo:
#---- registrar_viaje(
#con este for ya no se llama al error solo se itera sobre el valor de la funcion#     "Asturias",                           # Argumento obligatorio (destino)
#     "Oviedo", "Gijón", "Ibias",            # *args (lugares_visita)
#     hotel="Parador Nacional", costo=500   # **kwargs (detalles_adicionales)
# )

#*****************listas con .append y yeil para no saturar la memoria ram**************
# def obtener_numeros_lista():
#     resultado = []
#     for i in range(3):
#         resultado.append(i)
#     return resultado  # Devuelve la lista completa con todos los datos cargados
#---numeros = obtener_numeros_lista()
#---print(numeros)  # [0, 1, 2]

# def obtener_numeros_generador():
#     for i in range(3):
#         yield i  # Pausa la ejecución y entrega el número "al vuelo" [4]

#--- gen = obtener_numeros_generador()
# # Podemos obtener los valores usando la función next() [11]:
#--- print(next(gen))  # Salida: 0 [11]
#--- print(next(gen))  # Salida: 1 [11]
#--- print(next(gen))  # Salida: 2 [11]
# Si llamamos next() otra vez, dará el error StopIteration porque ya terminó [11, 12].
#Si usas un bucle for, Python se encarga de llamar a next() y de capturar el error StopIteration de forma automática por ti, por lo que nunca lo verás fallar
#---for numero in obtener_numeros_generador():
    #---print(numero)
#con este for ya no se llama al error solo se itera sobre el valor de la funcion

#***********decoradores para agregar funcionalidad al otra funcion*****************
from functools import wraps
# def registrar_ejecucion(funcion_original):
#     # Usamos @wraps para conservar los metadatos de la función original [10, 11]
#     @wraps(funcion_original)
#     def envoltura(*args, **kwargs):
#         print(f"⚡ Iniciando la envoltura: {funcion_original.__name__}")
#         resultado = funcion_original(*args, **kwargs)
#         print(f"✅ Finalizó la envoltura: {funcion_original.__name__}")
#         return resultado
#     return envoltura

# # Aplicamos el decorador usando la elegante sintaxis del '@' [9, 12]
# @registrar_ejecucion
# def cocinar_plato(plato):
#     print(f"🍳 Cocinando {plato}...")

# Llamada a la función decorada:
#---cocinar_plato("Pasta")
# Salida del código:
# ⚡ Iniciando la función: cocinar_plato
# 🍳 Cocinando Pasta...
# ✅ Finalizó la función: cocinar_plato

import time
# def func_decorador(FuncionOriginal):
#     def func_modificada(n):
#         inicio = time.time()
#         FuncionOriginal(n)
#         fin = time.time()
#         duracion = fin - inicio
#         print(f'duracion: {duracion}')
#     return func_modificada

# @func_decorador
# def imprimir_numero(n):
#     for i in range(n):
#         print(i)
#---imprimir_numero(50)


# Código problemático:
# def agrega(num, target=[]):
#     target.append(num)
#     return target

#---print(agrega(1)) # Salida: [1]
#---print(agrega(2)) # Salida: [1, 2]  (¡Reutilizó la lista anterior!)
#---print(agrega(3)) # Salida: [1-2-3]

# La Solución Idiomática: Usar None
# Para evitar que la lista se acumule entre llamadas, el estándar en Python,
#  es utilizar None como valor por defecto e inicializar,
#  la lista limpia dentro de la función
# Código correcto:
# def agrega(element, target=None):
#     if target is None:
#         target = []
#     target.append(element)
#     return target

#---print(agrega(1)) # Salida: [1]
#---print(agrega(2)) # Salida: [2]
#---print(agrega(3)) # Salida: [3]
#De esta forma, cada vez que llamas a la función sin pasar el segundo parámetro,
#  se creará una lista totalmente nueva

import math, random

#numeros = [1,4,9,16,25]
# raices = []
# for n in numeros:
#     raices.append(int(math.sqrt(n)))
#---print(raices)
# comprencion de listas
#raices = [int(math.sqrt(x)) for x in numeros]
#---print(raices)
#ejemplo 2
#numeros2 = [1,4,9,16,25]
#v = [x if (x>10) else '*' for x in numeros2]
#---print(v)
#up = [u.upper() for u in 'javier']
#---print(up)
#ejemplo3
#a = [l if l in 'aeiou' else '*' for l in 'murcielago']
#---print(a)
#lista = [l for l in range(10)]
#---print(lista)
#lista_1 = [random.randint(1,100) for _ in range(10)]
#---print(lista_1)
#comprencion de diccionarios
# "i" es la clave y el valor es el "random" de numeros aleatorios
#diccionario = {i:random.randint(1,100) for i in range(10)}
#---print(diccionario)
#crear dies listas con dos clave, valor el diccionario x comperencion
#diccionario_1= [{i:random.randint(1,100) for i in range(2)} for _ in range(10)]
#---print(diccionario_1)
#puedes meter listas dentro de diccionarios
#lista_2 = [{i:['javier' for _ in range(2)] for i in range(2)} for _ in range(10)]
#---print(lista_2)
#comprencion de generadores
#multiplos_gen = (i for i in range(30) if i % 3 == 0)
# #---print(multiplos_gen)
#  Mediante una Clase con __enter__ y __exit__
# Para que una clase actúe como gestor de contexto, debe definir
#  los métodos mágicos __enter__ y __exit__
# __enter__: Abre o prepara el recurso y devuelve el objeto con el que trabajaremos
# __exit__: Se invoca automáticamente al salir del bloque with para cerrar o liberar el recurso,
#  además de poder manejar excepciones si retorna True
# class MiGestorArchivo:
#     def __init__(self, nombre, modo):
#         self.archivo = open(nombre, modo)

#     def __enter__(self):
#         return self.archivo  # Se asigna a la variable 'as'

#     def __exit__(self, tipo_error, valor, traza):
#         self.archivo.close()  # Se asegura de cerrar el archivo siempre

# Uso con la sentencia 'with':
#---with MiGestorArchivo('demo.txt', 'w') as d:
#---    d.write('¡Hola Mundo!')
#Al terminar el bloque with, Python ejecuta automáticamente el método __exit__,
#  garantizando que el archivo no quede abierto

#Mediante contextlib y Generadores
#Python incluye el módulo contextlib con el decorador @contextmanager,
#  el cual permite definir un gestor de contexto usando una simple función y la palabra clave yield

# from contextlib import contextmanager
# @contextmanager
# def abrir_archivo(nombre):
#     f = open(nombre, 'w')
#     try:
#         yield f  # Entrega el recurso al bloque 'with'
#     finally:
#         f.close()  # Se ejecuta al salir del bloque 'with'
# Uso:
#---with abrir_archivo('demo.txt') as f:
    #---f.write('*argumentos y **argumentos de diccionario\n')
    #---f.write('funcion crear archivo txt\n')
    #---f.write('modulo mas decorador dentro del modulo\n')
#Todo el código antes del yield equivale a la fase de entrada (__enter__),
#  y el bloque finally actúa como la salida (__exit__)


#modulos os y pathlib en python
import os, pathlib
#obtener la direccion actual
#print(os.getcwd())

#cambiara otra carpeta 
# carpeta = pathlib.Path(__file__).resolve().parent / 'Documentos'
# if carpeta.is_dir():
#     os.chdir(carpeta)
#     print(f'Carpeta actual: {os.getcwd()}')
# else:
#     print(f'No se encontró la carpeta: {carpeta}')

#leer el contenido de un archivo
#archivo = open('demo.txt', 'r')
# for linea in archivo:
#     print(linea)
#archivo.close()

#leer la primera linea
#archivo = open('demo.txt', 'r')
#linea = archivo.readline()
#print(linea)

#lista los elementos del directorio actual
#elementos = os.listdir('.')
#os.mkdir("imagenes"): #Crea un único directorio
#os.remove('')
#print(elementos)

#Crear, renombrar y eliminar:
#os.makedirs("a/b/c", exist_ok=True): #Crea carpetas anidadas de forma recursiva. 
#El parámetro exist_ok=True evita que falle si la carpeta ya existe
#os.remove("archivo.txt"): #Elimina un archivo
#os.rmdir("carpeta"): #Elimina un directorio vacío
#os.rename("viejo.txt", "nuevo.txt"): #Renombra o mueve archivos y directorios

#Recorrer estructuras de carpetas con os.walk(): 
# Permite navegar de forma recursiva por un árbol de directorios 
# generando tuplas de la forma (ruta_actual, subcarpetas, archivos)

#for root, dirs, files in os.walk('.'):
#    print(f"Carpeta: {root} | Archivos: {files}")# [24, 25]

#Variables de entorno: Accede a las variables del sistema 
# usando os.environ.get("CLAVE", "valor_por_defecto") 
# sin riesgo de lanzar excepciones

#2. Manejo de Rutas: os.path vs. pathlib
#Construir rutas concatenando texto manualmente causa errores 
# debido a las diferencias de separadores entre sistemas operativos 
# (\ en Windows frente a / en Unix)
#Enfoque Tradicional (os.path — basado en cadenas)
#os.path.join("carpeta", "archivo.txt")#: Une partes de rutas insertando 
# el separador correcto
#os.path.exists("ruta"), os.path.isfile("ruta"), os.path.isdir("ruta")
#: Comprueban la existencia y tipo de elemento
#os.path.splitext("documento.pdf")
# : Separa el nombre base de la extensión (retorna ('documento', '.pdf'))

# import os
# ruta = os.path.join("nueva_carpeta_python", "modulo_os_path.py")# [29, 36]
# if os.path.exists(ruta):# [32, 33]
#     print(f"Archivo encontrado en: {ruta}")

#Enfoque Moderno (pathlib — orientado a objetos, Python 3.4+)
#El módulo pathlib representa las rutas mediante objetos Path 
# y utiliza el operador / para combinarlas de forma intuitiva

# from pathlib import Path
# base_dir = Path("Desktop")
# archivo = base_dir / "nueva_carpeta_python" / "modulo_os_path" #[5, 6, 37]

# if archivo.exists():# [5, 38, 39]
#     print(f"Nombre: {archivo.name}, Extensión: {archivo.suffix}")# [5, 39, 40]
#    contenido = archivo.read_text()# [38, 39]

# try y except ejemplos como usarlos
# numero = int(input('ingrese un numero: '))
# division = 10/numero
# print(division)
# #que pasa si ingreso un string en lugar de un numero
#------salta un error----------
# File "c:\Users\javier\Desktop\nueva_carpeta-python\modulo_os_path.py", line 301, in <module>
#     numero = int(input('ingrese un numero: '))
# ValueError: invalid literal for int() with base 10: 'javier'
# try:
#     numero = int(input('ingrese un numero: '))
#     division = 10/numero
#     print(division)
# except:
#     print('tienes que ingresar un numero entero')
#para eso se usa el try y except para validar fragmentos de codigo
#-----------clases y objetos------------------
class Perrro:
    especie = 'canis lupus familiaris'
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print('se ejecuto el constructor')
    def ladrar(self):
        print('el perro esta ladrando')
#se crea el objeto de la clase para que se ejecuter el constructor
mi_perro = Perrro('firulais', 30)
#acceder a los atributos y metodos de la clase
#para ejecutar un metodo ai que llamarlo para que se ejecute
print(mi_perro.nombre)
print(mi_perro.edad)
#llamar al metodo para que ejecute su proceso de operacion
mi_perro.ladrar()
#eliminar un objeto con "del" se usa en la creacion de videojuegos
#para que un objeto ya no ocupe memoria al ser eliminado
try:
    del mi_perro
    print(mi_perro.nombre)
except:
    print('el objeto ya no existe')
#aqui se uso el try,except para llamar al error

        


























































