# Como caso de estudio tomaremos una tienda de discos ficticia espacializada en vinilos, llamada "VERTIGO". 

# El siguiente código emula un programa con el que los empleados podrán realizar las tareas planteadas en
# el caso práctico final. Las mismas guardan la siguiente correspondencia con el menu principal:

#       1. Agregar una nueva tarea (Opción 1 del menu principal)
#       2. Marcar una tarea como completada (Opción 2 del menu principal)
#       3. Mostrar todas las tareas (Opción 3 del menu principal)
#       4. Eliminar una tarea (Opción 4 del menu principal)

# Como funcionalidad extra, se ha automatizado la lista de tareas para que sus elementos se ordenen por fecha límite.

# Autor: Leandro Oscar Aragon Alonso. Mayo de 2024, Curso IBM de Python Full Stack.


# -----------------------------------

# DEFINICIÓN DE CLASES

# -----------------------------------


# Creamos una clase que contiene los menus, destinados a facilitar la navegación del usuario

from datetime import datetime


# Creamos una clase para agrupar los menus, destinados a facilitar la navegación del usuario

class Menu:


    def bienvenida ():

        print ("\n------------------------------")
        print ("   VERTIGO - MENU PRINCIPAL")
        print ("------------------------------")
        Menu.principal()
    
    # Menu principal (empleado al inicio del programa)

    def principal ():

        print ("\n1. Crear una nueva tarea")
        print ("2. Modificar el estado de una tarea")
        print ("3. Mostrar todas las tareas")
        print ("4. Eliminar una tarea")
        print ("5. Salir del programa")
        
        # Prevenimos un error asociado al uso de strings en el input

        input_1 = input("\n> Selecciona una opción de la lista: ")


        # Creamos un bucle activo hasta que el usuario selecciona una opción válida

        while input_1 not in ("1", "2", "3", "4", "5"):

            input_1 = input("\n> Por favor, selecciona una opción válida (1-5): ")


        if input_1 == "1":

            Menu.crear_tareas()

        elif input_1 == "2":

            Menu.modificar_tareas()
        
        elif input_1 == "3": 

            Menu.lista_tareas()

        elif input_1 == "4": 

            Menu.eliminar_tareas()
        
        elif input_1 == "5": 

            Menu.salir()


    # Creación de tareas

    def crear_tareas ():
        
        print ("\n------------------------------")
        print ("        CREAR TAREAS")
        print ("------------------------------\n")

        return Operaciones.crear ()


    # Modificación del estado de una tarea: 

    def modificar_tareas ():

        print ("\n------------------------------")
        print ("       MODIFICAR ESTADO")
        print ("------------------------------\n")

        return Operaciones.actualizar ()
    

    # Listado de tareas

    def lista_tareas ():

        print ("\n------------------------------")
        print ("        LISTA DE TAREAS")
        print ("------------------------------\n")

        return Operaciones.listar()


    # Eliminación de tareas

    def eliminar_tareas ():

        print ("\n------------------------------")
        print ("       ELIMINAR TAREAS")
        print ("------------------------------\n")

        return Operaciones.eliminar()
        
    # Salida del programa

    def salir ():

        print ("\n------------------------------")
        print ("     PROGRAMA FINALIZADO")
        print ("------------------------------\n")

        return
    

# Creamos una clase para agrupar las tareas de la tienda (listadas más abajo)

class Tareas:

    # Definimos el constructor de la clase
    
    def __init__(self, nombre, estado, prioridad, fecha_fin, responsable, observaciones):

        self.nombre = nombre
        self.estado = estado
        self.prioridad = prioridad
        self.fecha_fin = fecha_fin
        self.responsable = responsable
        self.observaciones = observaciones
    


    # Definimos la representación del objeto (para listados)
    
    def __repr__(self):

        if self.estado == True:
        
            self.estado = "COMPLETADO"
        
        else:
        
            self.estado = "PENDIENTE"

        return f"{self.nombre} ({self.estado})"
    
   

    # Definimos la representación exhaustiva del objeto

    def repr_completa(self):

        if self.estado == True:
        
            self.estado = "COMPLETADO"
        
        else:
        
            self.estado = "PENDIENTE"

        return f"TAREA: {self.nombre}\n\n   • Estado: {self.estado}\n   • Prioridad: {self.prioridad}\n   • Encargado: {self.responsable}\n   • Fecha límite: {self.fecha_fin}\n   • Observaciones: {self.observaciones}"
    

    # Definimos un método para imprimir la lista (ya ordenada por fecha límite)

    def imprimir (i):
    
        for indice, item in enumerate(i):
        
            print(f"{indice}. {item}")
    
        pass


    def ordernar_fecha ():

        tareas_por_fecha = sorted(lista_tareas, key=lambda Tareas: Tareas.fecha_fin)

        return tareas_por_fecha
    

    def imprimir_fecha (i):
    
        for indice, item in enumerate(i):
        
            print(f"{indice}. {item}")
    
        pass
    

# Creamos una clase para agrupar las operaciones requeridas por el ejercicio práctico

class Operaciones():

    def __init__(self):
        
        self.lista_tareas = []
        

    # Definimos un método para crear tareas

    def crear ():


        # El usuario ingresa uno por uno los atributos

        nombre = input ("> Introduce el nombre de la tarea: ")


        # Nos aseguramos de que el estado sea completado o pendiente. Empleamos claves para facilitar el input

        estado = input ("> Indica su estado, completado o pendiente (C/P): ")

        while estado not in ("C", "P"):
                
            estado = input ("Incorrecto, por favor utiliza los valores (C/P): ")

        if estado == "C":
            
            estado = True

        elif estado == "P":
              
            estado = False


        # Nos aseguramos de que la prioridad sea alta, media o baja. Empleamos claves para facilitar el input

        prioridad = input ("> Indica si la prioridad es alta, media o baja (A/M/B): ")
        
        while prioridad not in ("A", "M", "B"):
                
            prioridad = input ("Incorrecto, por favor utiliza los valores (A/M/B): ")

        if prioridad == "A":
            
            prioridad = "ALTA"

        elif prioridad == "M":
              
            prioridad = "MEDIA"
        
        elif prioridad == "B":
              
            prioridad = "BAJA"


        fecha_fin = input("> Introduce la fecha límite (AAAA, MM, DD): ")
       
        try:
        
            fecha_fin = datetime.strptime(fecha_fin, "%Y, %m, %d")

        except ValueError:
        
            print("Formato inválido. Utiliza (YYYY, MM, DD): ")

        
        responsable = input("> Introduce el responsable: ")
        
        observaciones =input("> Introduce tus observaciones: ")


        # Una vez recopilados los datos se pide confirmación
        
        crear_conf = input(f"\n> Se va a añadir una tarea a la lista, desea continuar? (Y/N): ")

        while crear_conf not in ("Y", "N"):

            crear_conf = input("> Introduce un valor correcto (Y/N): ")
        
        if crear_conf == "N": 

            input (f"\n> Operación cancelada (PRESIONA ENTER PARA CONTINUAR)")
            Menu.bienvenida()

        
        # Al obtener confirmación,se crea una nueva tarea
        
        elif crear_conf == "Y":

            nueva_tarea = Tareas(nombre, estado, prioridad, fecha_fin, responsable, observaciones)

            lista_tareas.append(nueva_tarea)


            # Se actualiza la variable de lista ordenada para asegurarnos de que la nueva tarea aparece en la misma

            lista_ordenada2 = sorted(lista_tareas, key=lambda Tareas: Tareas.fecha_fin)

            lista_ordenada = lista_ordenada2
            
            
            # Se imprimen los detalles de la nueva tarea
            
            print(" ") 
            print(nueva_tarea.repr_completa())

        
            input (f"> Tarea creada con éxito (PRESIONA ENTER PARA CONTINUAR)")
            

        return Menu.bienvenida ()
    


    # Definimos un método para eliminar tareas

    def eliminar():

        # Imprimimos el listado de tareas con su correspondiente índice y estado actual

        for indice, item in enumerate(lista_tareas):

            print(f"{indice}. {item}")

    
        # Permitimos al usuario elegir una tarea de la lista para ver todos sus detalles
        
        posicion_input = input("\n> Indica la tarea que deseas eliminar: ")

        try:
            
            usuario_input_3 = int(posicion_input)

            posicion = lista_tareas[usuario_input_3]


        # Prevenimos un error asociado al uso de strings en el input

        except ValueError:


            print ("\n------------------------------")
            print("ERROR: solo puedes utilizar caracteres numéricos")
            print ("------------------------------\n")
            Menu.principal()


        # Prevenimos un error asociado a un índice fuera de rango

        except IndexError:
            
            print ("\n------------------------------")
            print("ERROR: la tarea no se encuentra en el listado")
            print ("------------------------------\n")
            Menu.principal()


        # Mostramos los detalles la tarea que vamos a borrar y pedimos confirmación

        print(f"\n{lista_tareas[usuario_input_3].repr_completa()}")


        user_conf = input("\n> Seguro que deseas borrar esta tarea? (Y/N): ")

        while user_conf not in ("Y", "N"):

            user_conf = input("> Introduce un valor correcto (Y/N): ")
        
        if user_conf == "N": 

            input (f"\n> Operación cancelada (PRESIONA ENTER PARA CONTINUAR)")

            Menu.bienvenida()

        
        # Al obtener confirmación procedemos a borrar la tarea seleccionada
        
        elif user_conf == "Y":

            del lista_tareas[int(usuario_input_3)]

            input(
                f"\n> Tarea borrada con éxito (PRESIONA ENTER PARA CONTINUAR)")

        return Menu.bienvenida()
        

        
    # Definimos un método para cambiar el estado

    def actualizar ():

        Tareas.imprimir_fecha(Tareas.ordernar_fecha())


        # Creamos una nueva variable con la lista ya ordenada por fecha

        lista_tareas_fecha = Tareas.ordernar_fecha()

        
        # Permitimos al usuario elegir una de la lista para ver todos sus detalles
        
        
        posicion_input = input("\n> Indica la tarea cuyo estado quieres modificar: ")

        try:
            
            usuario_input_2 = int(posicion_input)

            posicion = lista_tareas_fecha[usuario_input_2]


        # Prevenimos un error asociado al uso de strings en el input

        except ValueError:


            print ("\n------------------------------")
            print("ERROR: solo puedes utilizar caracteres numéricos")
            print ("------------------------------\n")
            Menu.principal()


        # El usuario pasa a indicar si la tarea está completada o pendiente

        print (f"\nVas a actualizar la tarea: {lista_tareas_fecha[usuario_input_2].nombre} ")

        
        nuevo_estado = input ("\n> Indica su estado, completado o pendiente (C/P): ")

        while nuevo_estado not in ("C", "P"):
                
            nuevo_estado = input ("\nIncorrecto, por favor utiliza los valores (C/P): ")

        if nuevo_estado == "C":
            
            estado = True

        elif nuevo_estado == "P":
              
            estado = False
            

        # Se actualiza el estado de la tarea

        lista_tareas[usuario_input_2].estado


        # Se imprimen los detalles actualizados de la tarea

        print(f"\n{lista_ordenada[usuario_input_2].repr_completa()}")

        input (f"> Tarea actualizada con éxito (PRESIONA ENTER PARA CONTINUAR)")
        
        return Menu.bienvenida()



    # Definimos un método para mostrar el listado de tareas y revisarlas individualmente

    def listar ():

        Tareas.imprimir_fecha(Tareas.ordernar_fecha())


        # Creamos una nueva variable con la lista ya ordenada por fecha

        lista_tareas_fecha = Tareas.ordernar_fecha()

        
        # Permitimos al usuario elegir una de la lista para ver todos sus detalles
        
        
        posicion_input = input("\n> Indica la tarea que deseas inspeccionar: ")

        try:
            
            usuario_input_4 = int(posicion_input)

            posicion = lista_tareas_fecha[usuario_input_4]


        # Prevenimos un error asociado al uso de strings en el input

        except ValueError:


            print ("\n------------------------------")
            print("ERROR: solo puedes utilizar caracteres numéricos")
            print ("------------------------------\n")
            Menu.principal()


        # Prevenimos un error asociado a un índice fuera de rango

        except IndexError:
            
            print ("\n------------------------------")
            print("ERROR: la tarea no se encuentra en el listado")
            print ("------------------------------\n")
            Menu.principal()
        

        # Se muestran los detalles de la tarea actualizada

        print(f"\n{lista_tareas_fecha[usuario_input_4].repr_completa()}")

        input (f"> Volver al menu principal (PRESIONA ENTER PARA CONTINUAR)")
        
        return Menu.bienvenida()
    
    
# -----------------------------------

# Pasamos a enumerar las instancias, en este caso tareas: 

lista_tareas = [
Tareas("Devolver el pedido #5059 a EMI Music", True, "ALTA", datetime(2024, 5, 25), "Juan", "Incluír el albarán firmado"),
Tareas("Cambiar los discos del expositor exterior", True, "MEDIA", datetime(2024, 6, 1), "Frank", "Poner el nuevo disco de AC/DC en primera fila"),
Tareas("Hacer un pedido a Totem Cat Records", True, "BAJA", datetime(2025, 1, 12), "Frank", "Solicitar 15 copias de Church of Misery"),
Tareas("Actualizar la base de datos", False, "BAJA", datetime(2024, 8, 13), "Frank", "Añadir los lanzamientos del Record Store Day"),
Tareas("Realizar entrevistas para Social Media Manager", True, "MEDIA", datetime(2024, 5, 28), "Juan", "Revisar los mensajes privados de Facebook para obtener los CV")
]

# -----------------------------------

# Ordenamos la lista de tareas por fecha

lista_ordenada = sorted(lista_tareas, key=lambda Tareas: Tareas.fecha_fin)

# -----------------------------------

# Finalmente, hacemos correr el programa con una sola llamada a la función del menu de bienvenida

Menu.bienvenida()

# NOTA: En caso de seleccionar ("Salir del programa") el mismo finalizará