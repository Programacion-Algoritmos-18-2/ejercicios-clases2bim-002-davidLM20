"""
    creación de clases
"""

class Persona(object):
    """
    """
    # declaracion de atributos de la clase
    def __init__(self, n, ape, ed, cod, n1, n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)#se transforma la variable a entero
        self.codigo = int(cod)#se transforma la variable a entero
        self.apellido = ape
        self.nota1 = int(n1)#se transforma la variable a entero
        self.nota2 = int(n2)#se transforma la variable a entero

    # metodos para obtener y agregar cada uno de la informacion
    def agregar_nombre(self, n):# agregar y obtener nombre
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):# agregar y obtener edad
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):# agregar y obtener codigo
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo

    def agregar_apellido(self, ape):# agregar y obtener apellido
        """
        """
        self.apellido = ape

    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self, n1):# agregar y obtener nota 1
        """
        """
        self.nota1 = n1

    def obtener_nota1(self):
        """
        """
        return self.nota1

    def agregar_nota1(self, n2): # agregar y obtener nota 2
        """
        """
        self.nota2 = n2

    def obtener_nota2(self):
        """
        """
        return self.nota2

    # metodo str para retornar la informaciotoda la informacion    
    def __str__(self): 
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.obtener_nombre(), self.obtener_apellido(),\
                self.obtener_edad(), self.obtener_codigo(), self.obtener_nota1(), self.obtener_nota2())


class OperacionesPersona(object):
    """
    """
    # declaracion de atributo lista
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado

    # metodo para obtener el promedio de las primeras notas
    def obtener_promedio_nota1(self):
        """
        """
        suma = 0 # se crea variable para la suma de las notas
        for n in self.listado_personas: # se recorre el listado 
            suma = suma + n.obtener_nota1() # se sumalas notas
        promedio = suma / len(self.listado_personas) # se divide la suma para tama;o de listado

        return promedio# se retorna el promedio

     # metodo para obtener el promedio de las segundas notas
    def obtener_promedio_nota2(self):
        """
        """
        suma = 0 # se crea variable para la suma de las notas
        for n in self.listado_personas: # se recorre el listado 
            suma = suma + n.obtener_nota2()# se sumalas notas
        promedio = suma / len(self.listado_personas) # se divide la suma para tama;o de listado

        return promedio# se retorna el promedio  
    
    #metodo para devolver el nombre de las personas scon nota 1 menor a 15
    def obtener_nombres_promedios_n1(self):
        """
        """
        cadena = "Estudiantes con la primera nota menor a 15\n" # se realiza un encabezado
        for n in self.listado_personas:# se recorre la lista
            if n.obtener_nota1() < 15: # se genera el condicional para verificar que nota es menor a 15
                cadena = "%s %s %s" % (cadena, n.obtener_nombre(),n.obtener_apellido()) # se da la informacion a cadena 
        return cadena  # se retorna cadena

    #metodo para devolver el nombre de las personas scon nota 2 menor a 15
    def obtener_nombres_promedios_n2(self):
        """
        """
        cadena = "Estudiantes con la segundo nota menor a 15\n"# se realiza un encabezado
        for n in self.listado_personas:# se recorre la lista
            if n.obtener_nota2() < 15:# se genera el condicional para verificar que nota es menor a 15
                cadena = "%s %s %s" % (cadena, n.obtener_nombre(),n.obtener_apellido()) # se da la informacion a cadena
        return cadena# se retorna cadena

    # metodo para obtner un listado de personas que su nombre inicie con R o J
    def obtener_listado_personas(self, nom1, nom2):
        cadena = "Estudiantes con nombre que inicia con R o J" # se realiza un encabezado
        lista = [] # se crea una lista para guardar 
        for n in self.listado_personas:# se recorre la lista 
            if (nom1 == n.obtener_nombre()[0] or nom2 == n.obtener_nombre()[0]): # condicional para verificar con que Letra empieza
                cadena = "%s %s %s\n" % (cadena, n.obtener_nombre(),n.obtener_apellido())# se da la informacion a cadena
                lista = cadena # guarda cadena en la lista
        return lista # se retorna lista

    # metodo str
    def __str__(self):
        """
        """
        cadena = ""
        for n in self.listado_personas:
            cadena = "%s %s %s \n" % (cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena    