from paquete_archivos.miarchivo import MiArchivo # se importa toda la informacion de mi archivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona	# se importa la informacion de las clases persona y operacionespersona

m = MiArchivo() # se crea el objeto mi archivo
lista = m.obtener_informacion() # se da la informacion del objeto a la lista
lista = [l.split("|") for l in lista] # se crea nuevas listas ada que encuentre el separador |

# print(lista)

lista = lista[1:]
lista_personas = [] # se crea una lista nueva para a;adir el objeto p
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
print("Listado de estudiantes\n")# se genera un encabezado
for d in lista:# se recorre la lista
    # print(d)
    #suma_n1 = suma_n1 + int(d[4])
    p = Persona(d[1], d[2], d[3], d[0], d[4],d[5]) # se crea un objeto tipo persona y se le envia la informacion
    lista_personas.append(p)# se a;iade a la lista persona
    print(p) # se inmprime el listado de estudiantes

operaciones = OperacionesPersona(lista_personas)# se crea una variable operaciones para imprimir 

print("\nPromedio de la primera nota de los estudiantes ", operaciones.obtener_promedio_nota1()) # se imprime el promedio de la nota 2
print("Promedio de la segunda nota de los estudiantes ", operaciones.obtener_promedio_nota2())# se imprimer el promedio de la nota 2
print("")
print(operaciones.obtener_nombres_promedios_n1()) # se imprime la los nombres de las personas que tienen una note 1 menor a 15
print(operaciones.obtener_nombres_promedios_n2()) #  se imprime la los nombres de las personas que tienen una note 2  menor a 15
print("")
print(operaciones.obtener_listado_personas("R", "J")) # se imprime los nombre que empiezan con R o J