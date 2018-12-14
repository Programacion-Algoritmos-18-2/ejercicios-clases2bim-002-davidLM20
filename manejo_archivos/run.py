from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
suma_n1 = 0
suma_n2 = 0 
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
    # print(d)
    #suma_n1 = suma_n1 + int(d[4])
    p = Persona(d[1], d[2], d[3], d[0], d[4],d[5])
    suma_n1 = suma_n1 + p.obtener_nota1()
    suma_n2 = suma_n2 + p.obtener_nota2()
    if p.obtener_nota1() < 15 or p.obtener_nota2() < 15:
    	print(p.obtener_nombre())

resultado = suma_n1 /len(lista)
resultado2 = suma_n2/len(lista)
print(resultado)
print(resultado2)