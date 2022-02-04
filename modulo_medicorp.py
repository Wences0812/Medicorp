import os; clear = lambda: os.system('cls'); clear()
import sys
import random


class edad_min_invalid(Exception):
    pass


def login(lista_usuarios,lista_contrasenias):
    """
    IN: lista de usuarios y lista de contraseñas.
    OUT: acceso permitido o denegado True/False + usuario + contraseña.
    """
    error = 2
    usuario=input("Ingrese su usuario: ")
    while usuario not in lista_usuarios:    #Si no aparece en la lista vuelve a pedir el usuario.
        error=error-1
        print("Datos incorrectos, por favor vuelva a ingresar sus datos")
        usuario=input("Ingrese su usuario: ")
        if error==0:
            print("Limite de intentos alcanzados, acceso dengado")
            return False,usuario
    contrasenia=input("Ingrese su contraseña: ")
    pos_usuario=lista_usuarios.index(usuario)   #Si aparece busca la posicion
    while contrasenia!=lista_contrasenias[pos_usuario]:
        error=error-1
        if error==0:
            print("Limite de intentos alcanzados, acceso denegado")
            return False, usuario
        print("Datos incorrectos, por favor vuelva a ingresar sus datos")
        contrasenia=input("Ingrese su contraseña: ")
    return True, usuario

def menu():
    print("""
    ****** Bienvenid@ al menu de Medicorp ******
    Ingrese a una de las siguientes opciones con el número asignado:
    1 para alta de paciente,
    2 para alta de turno,
    3 para modificar datos del paciente,
    4 para baja de paciente,
    5 para baja de turno,
    6 para listar turnos según dia y mes,
    7 para listar pacientes,
    8 para buscar turno según DNI,
    9 para cargar datos de prueba,
    10 para buscar paciente,
    11 para listar pacientes segun edad ingresada,
    12 para modificar  el turno de un paciente,
    0 para salir del programa.
    ******************************************************************
    """)
    while True:
        try:
            menu_selection = input()
            assert (menu_selection.isnumeric() == True) ,"Debe ingresar un número"
            menu_selection = int(menu_selection)
            assert (menu_selection>= 0 and menu_selection <=14), "Opción ingresada incorrecta"
        except AssertionError as error:
            clear()
            print(error)
        else:
            break
    return menu_selection

def pacientes_a_listas():
    """
    Leemos el archivo y pasamos los datos de los pacientes a listas.
    """
    try:
        arch=open("datos_pacientes.txt",'r')
    except IOError:
        print("No se pudo leer el archivo")
    except:
        print("Ocurrió un error inesperado")
    else:
        lista_dni=[]
        lista_nombre=[]
        lista_apellido=[]
        lista_edad=[]
        linea=arch.readline()
        linea=linea.rstrip()
        while linea != "":
            pacientes=linea.split(";")
            lista_dni.append(pacientes[0])
            lista_apellido.append(pacientes[1])
            lista_nombre.append(pacientes[2])
            lista_edad.append(pacientes[3])
            linea=arch.readline()
            linea=linea.rstrip()
    return lista_dni,lista_apellido,lista_nombre,lista_edad

def ordenar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad,i=1):
    """
    Se ordena las listas de la pacientes según los apellidos.
    Se utiliza el metodo de incersión con recursividad.
    """
    try:
        assert lista_dni != [] and lista_apellido != [], "Base de datos vacía" 
        assert lista_nombre != [] and lista_edad != [], "No hay datos ingresados."
        if i==len(lista_apellido):
            return lista_dni,lista_apellido,lista_nombre,lista_edad
        else:
            apellido_aux=lista_apellido[i]
            nombre_aux=lista_nombre[i]
            dni_aux=lista_dni[i]
            edad_aux=lista_edad[i]
            j=i
            while j>0 and lista_apellido[j-1]>apellido_aux:
                lista_apellido[j]=lista_apellido[j-1]
                lista_nombre[j]=lista_nombre[j-1]
                lista_dni[j]=lista_dni[j-1]
                lista_edad[j]=lista_edad[j-1]
                j=j-1
            lista_apellido[j]=apellido_aux
            lista_nombre[j]=nombre_aux
            lista_dni[j]=dni_aux
            lista_edad[j]=edad_aux
            return ordenar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad,i+1)
    except AssertionError as error:
            clear()
            print(error)

def grabar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad):
    """
    Se graban las listas de los datos de los pacientes en el archivo.
    """
    try:
        arch=open("datos_pacientes.txt","w")
    except IOError:
        print("No se pudo leer el archivo")
    except:
        print("Ocurrió un error inesperado")
    else:
        for i in range(len(lista_dni)):
            paciente=[lista_dni[i],lista_apellido[i],lista_nombre[i],lista_edad[i]]
            paciente=";".join(paciente)
            arch.write(paciente+"\n")

def listar_pacientes():
    """
    Imprime en pantalla el archivo de pacientes dados de alta.
    """
    try:
        pacientes = open('datos_pacientes.txt','r')
    except IOError:
        print("No se pudo leer el archivo")
    else:
        try:
            linea = pacientes.readline()
            print("Listado de pacientes en el sistema: ")
            while linea != '':	
                linea = linea.rstrip()
                paciente = linea.split(';')
                dni = int(paciente[0])
                apellido = paciente[1]
                nombre = paciente[2]
                edad = int(paciente[3])
                print(f'DNI:{dni:08d}   APELLIDO: {apellido:<15s}' + 
                f'NOMBRE: {nombre:<15s} EDAD: {edad:02d}')
                linea = pacientes.readline()
        except IndexError:
            print("La base de datos se encuentra vacía.")
        except:
            print("Error inesperado.")
      
def cargar_pacientes_dni():
    """
    Se leen el archivo que contiene todos los pacientes dados de alta.
    Se carga en una lista los DNI de los pacientes.
    Se retorna la lista.
    """
    try:
        pacientes = open('datos_pacientes.txt','r')
    except FileNotFoundError:
        print("El archivo de paciente no se encuentra.")
    except:
        print("Error inesperado")
    else:
        lista_dni = []
        linea = pacientes.readline()
        while linea != '':	
            linea = linea.rstrip()
            paciente = linea.split(';')
            dni = paciente[0]
            lista_dni.append(dni)
            linea = pacientes.readline()
    return lista_dni

def validar_dni(dni):
    while dni.isnumeric() == False or int(dni)>99999999 or int(dni)<1000000:
        print("DNI ingresado es inválido.")
        dni = input('Ingrese el DNI del paciente: ')
    return dni

def alta_paciente():
    lista_dni = cargar_pacientes_dni()
    try:
        pacientes = open('datos_pacientes.txt','a')
    except FileNotFoundError:
        print("El archivo de paciente no se encuentra.")
    except:
        print("Error inesperado")
    else:
        while True:
            try:
                dni = input('Ingrese el DNI del paciente: ')
                dni = validar_dni(dni)
                while int(dni) in lista_dni:
                    dni = input('ERROR: el dni ingresado ya existe. Ingrese el DNI del paciente: ')
                    dni = validar_dni(dni)
            except TypeError:
                print ('Error de tipo')
            except:
                print ('Error inesperado')
            else:
                apellido = input('Ingrese el apellido del paciente: ')
                while apellido.replace(" ", "").isalpha()==False:
                    print("El apellido del paciente es inválido.")
                    apellido = input('Ingrese el apellido del paciente: ')
                nombre = input('Ingrese el nombre del paciente: ')
                while nombre.replace(" ", "").isalpha()==False:
                    print("El nombre del paciente es inválido.")
                    nombre = input('Ingrese el nombre del paciente: ')
                edad = input('Ingrese edad del paciente: ')
                while edad.isnumeric()!=True or int(edad)<18:
                    if edad.isnumeric()!=True:
                        print("Se permiten solo numeros.")
                    else:
                        print("Debe ser mayor de edad.")
                    edad =input('Ingrese edad del paciente: ')
                paciente= [str(dni),apellido.capitalize(), nombre.capitalize(), edad]
                paciente = ';'.join(paciente)
                pacientes.write(paciente + '\n')
                print("Los datos del nuevo paciente se agregaron existosamente.")
                break

def baja_paciente(lista_dni,lista_apellido,lista_nombre,lista_edad):
    dni=input("""Has elegido dar de baja un paciente. 
    Ingrese el DNI del paciente a dar de baja: """)
    veces=lista_dni.count(dni)
    if veces==0:
        print("El paciente no fue dado de alta.")
    else:
        borrar_turno(dni)
        pos=lista_dni.index(dni)
        lista_dni.pop(pos)
        lista_apellido.pop(pos)
        lista_nombre.pop(pos)
        lista_edad.pop(pos)
        print("Paciente dado de baja correctamente.")

def alta_turno(dni):
    lista_dni = cargar_pacientes_dni()
    lista_turnos, lista_turnos_dni = cargar_turnos_lista()
    if dni in lista_dni: # Se chequea que el dni esta dado de alta.
        if dni not in lista_turnos_dni: # Se chequea que el dni no tenga un turno asignado.
            try:
                turnos = open('turnos.txt','a')
            except FileNotFoundError:
                print("El archivo de paciente no se encuentra.")
            except:
                print("Error inesperado")
            else:
                print("Ingrese fecha del turno")
                year = input("Ingrese el año: ")
                year = year.rstrip()
                while year.isnumeric()!=True or int(year)<2021:
                    if year.isnumeric()!=True:
                        print("Se permiten solo 4 numeros para indicar el año.")
                    else:
                        print("Debe ser mayor o igual al año 2021.")
                    year = input("Ingrese el año: ")
                    year = year.rstrip()
                month = input("Ingrese el mes: ")
                month = month.rstrip()
                while month.isnumeric()!=True or int(month)<1 or int(month) >12:
                    if month.isnumeric()!=True:
                        print("Se permiten solo 2 numeros para indicar el mes (Febrero => 02).")
                    else:
                        print("Debe serentre 1 y 12.")
                    month = input("Ingrese el mes: ")
                    month = month.rstrip()
                day = input("Ingrese el dia del turno (1, 8, 15 y 22 de no hay turnos): ")
                day = day.rstrip()
                while True:
                    if int(day)<1 or int(day) >31:
                        print("Valor ingresado inválido.")
                    elif day.isnumeric()!=True:
                        print("Se permiten solo 2 numeros para indicar del dia.")
                    elif int(day) == 1 or int(day) == 8 or int(day) == 15 or int(day) == 22:
                        print("Esa fecha no se atienden pacientes.")
                    else:                       
                        break
                    day = input("Ingrese el dia del turno (1, 8, 15 y 22 de no hay turnos): ")
                    day = day.rstrip()
                hour = input("Ingrese la hora: ")
                hour = hour.rstrip()
                while hour.isnumeric()!=True or int(hour)<10 or int(hour) >14:
                    if hour.isnumeric()!=True:
                        print("El horario de atención es de 10 a 14Hs.")
                    else:
                        print("Debe ser entre 10 y 14.")
                    hour = input("Ingrese la hora: ")
                    hour = hour.rstrip()
                fecha = [year, month.zfill(2), day.zfill(2), hour]
                turno = "".join(fecha)
                if turno not in lista_turnos: # Se chequea que el turno no este tomado.
                    turno = turno + ";" + dni
                    turnos.write(turno + '\n')
                    print("El turno ha sido agendado, recuerde llegar 10 minutos antes.")
                else:
                    print("El turno ya está tomado.")
        else:
            position = lista_turnos_dni.index(dni)
            turno=lista_turnos[position]
            anio=turno[0:4]
            mes=turno[4:6]
            dia=turno[6:8]
            hora=turno[8:]
            print("El paciente ya tiene un turno para el DÍA:",dia,"MES:",mes,"AÑO:",anio, "A las:",hora,"Hs.")

    else:
        print("El DNI no esta dado de alta.")

def cargar_turnos_lista():
    """
    Lee el archivo de turnos y lo pasa a una lista para mejor manipulación.
    """
    try:
        pacientes = open('turnos.txt','r')
    except FileNotFoundError:
        print("El archivo de paciente no se encuentra.")
    except:
        print("Error inesperado")
    else:
        lista_turnos = []
        lista_turnos_dni = []
        linea = pacientes.readline()
        linea = linea.rstrip()
        while linea != '':	
            turno = linea.split(';')
            fecha = turno[0]
            lista_turnos.append(fecha)
            dni = turno[1]
            lista_turnos_dni.append(dni)
            linea = pacientes.readline()
            linea = linea.rstrip()
    return lista_turnos, lista_turnos_dni

def buscar_turno(dni=0):
    lista_dni = cargar_pacientes_dni()
    lista_turnos, lista_turnos_dni = cargar_turnos_lista()
    if dni == 0:
        dni = input("Ingrese el DNI para buscar turno: ")
        dni = validar_dni(dni)
    if dni in lista_dni:
        if dni not in lista_turnos_dni:
            print(f'El paciente con DNI: {dni} no tiene turno asignado.')
        else:
            position = lista_turnos_dni.index(dni)
            turno=lista_turnos[position]
            anio=turno[0:4]
            mes=turno[4:6]
            dia=turno[6:8]
            hora=turno[8:]
            print("El paciente ya tiene un turno para el DÍA:",dia,"MES:",mes,"AÑO:",anio, "A las:",hora,"Hs.")
    else:
        print("El DNI no esta dado de alta.")

def buscar_pacientes():
    try:
        input_dni = int(input("Ingrese el DNI del paciente: "))
        lista_dni = cargar_pacientes_dni()
        if input_dni in lista_dni:
            try:
                archivo = open("datos_pacientes.txt",'r')
                pacientes = archivo.readlines()
                for paciente in pacientes:
                    if paciente.startswith(str(input_dni)):
                        paciente_lista = paciente.split(";") 
                        print(f"DNI: {paciente_lista[0]}")
                        print(f"Apellido: {paciente_lista[1]}")
                        print(f"Nombre: {paciente_lista[2]}")
                        print(f"Edad: {paciente_lista[3]}")
            except FileNotFoundError:
                print('Archivo no disponible.')
        else:
            print('No hay registros con ese DNI.')
    except ValueError:
        print('DNI no valido.')
    except:
        print("Error inesperado.")

def borrar_turno(dni):
    """
    Se cargan los turnos en una lista y los DNI en otra lista. 
    Cada lista está indexada con su respectiva posición.
    Se elimina el DNI que ingresa por teclado si existe.
    luego se vuelve a escribir en el archivo los restantes turnos.
    """
    lista_turnos, lista_turnos_dni = cargar_turnos_lista()
    if dni in lista_turnos_dni: # Se chequea que el dni esta dado de alta.
        pos=lista_turnos_dni.index(dni)
        lista_turnos_dni.pop(pos)
        lista_turnos.pop(pos)
        try:
            turnos = open('turnos.txt','w')
        except FileNotFoundError:
                print("El archivo de paciente no se encuentra.")
        except:
                print("Error inesperado")
        else:
            for turno in lista_turnos:
                for dni in lista_turnos_dni:
                    turno = turno + ";" + dni
                    turnos.write(turno + '\n')

def listadoMayores(lista_DNI, lista_apellido,lista_nombres, lista_edades ):
    '''
    Función que lista los pacientes según una determinada edad ingresada por teclado.
    '''
    try:
        edadMin=int(input("Ingrese la edad mínima del listado de pacientes: "))
        assert edadMin >17, 'La edad mínima es 18 años'
    except ValueError:
        print('Edad no valida.')
    except AssertionError as error:
        print(error)
    except:
        print("Error inesperado.")
    else:
        dicc= {'listaEdadesMayores':[], 'listaDNI':[], 'listaApellidos':[], 'listaNombres':[]}
        for i in range(len(lista_edades)):
            if int(lista_edades[i])>=edadMin: 
                dicc['listaEdadesMayores'].append(lista_edades[i])
                dicc['listaDNI'].append(lista_DNI[i])
                dicc['listaApellidos'].append(lista_apellido[i])
                dicc['listaNombres'].append(lista_nombres[i])
        for i in range(len(dicc['listaNombres'])):
            dni=int(dicc['listaDNI'][i])
            apellido=dicc['listaApellidos'][i]
            nombre=dicc['listaNombres'][i]
            edad=int(dicc['listaEdadesMayores'][i])
            print(f'DNI:{dni:08d}   APELLIDO: {apellido:<15s}' + 
                f'NOMBRE: {nombre:<15s} EDAD: {edad:02d}')

def modificar_paciente(lista_dni, lista_apellido, lista_nombre, lista_edad):
    dni= input("ingrese el dni del paciente a modificar:")
    dni= validar_dni(dni)
    lista_dni= cargar_pacientes_dni()
    lista_dnicont= lista_dni.count(dni)
    if lista_dnicont != 0:
        pos= lista_dni.index(dni)
        nombre= input("ingrese el nombre del paciente:")
        nombre= validar_nombre(nombre)
        lista_nombre[pos]= nombre.title() 
        apellido= input("ingrese el apellido del paciente:")
        apellido= validar_apellido(apellido)
        lista_apellido[pos]= apellido.title()
        edad= int(input("ingrese la edad del paciente:"))
        edad= validar_edad(int(edad))
        lista_edad[pos]= str(edad)
        print(f'Paciente con DNI {dni} modificado con exito.')
    else:
        print(f'El DNI {dni} no esta dado de alta.')

def validar_apellido(apellido):
    while apellido.isalpha() == False:
        print("error, el apellido ingresado es invalido")
        apellido= input("ingrese un nombre valido:")
    return apellido

def validar_nombre(nombre):
    while nombre.isalpha() == False:
        print("error, el nombre ingresado es invalido")
        nombre= input("ingrese un nombre valido:")
    return nombre

def validar_edad(edad):
    while str(edad).isnumeric() == False or int(edad) >100 or int(edad) < 18:
        print("error, la edad ingresada no es valida")
        edad= int(input("ingrese una edad valida:"))
    return edad

def modificar_turno(dni):
    """
    Modifica el turno del DNI si este existe.
    """
    lista_dni = cargar_pacientes_dni()
    lista_turnos, lista_turnos_dni = cargar_turnos_lista()
    if dni in lista_dni and dni in lista_turnos_dni:
        """
        Mientras el formulario no sea valido se mantendra en bucle.
        La variable first es para evaluar si es la primera iteracion del programa,
        no van a haber errores si es la primera vez que se corre.
        La lista errors es la que almacena todos los mensajes de los campos ingresados
        que no son validos
        """
        buscar_turno(dni)
        valid = False
        first = True
        errors = []
        while valid == False:
            if not first and len(errors) > 0:
                print('-----------------------------------------')
                print("Por favor corrige los siguientes errores: ")
                print('\n'.join(errors))
                print('-----------------------------------------')
                errors = []
            year = input("Ingrese el nuevo año: ").rstrip()
            month = input("Ingrese el nuevo mes: ").rstrip()
            day = input("Ingrese el nuevo dia: ").rstrip()
            hour = input("Ingrese la nueva hora: ").rstrip()
            if not year.isnumeric() or int(year) < 2021:
                errors.append("* El año no es valido.")
            if not year.isnumeric() or int(month) < 1 or int(month) > 12:
                errors.append("* El mes no es valido.")
            if not day.isnumeric() or int(day) < 1 or int(day) > 31:
                errors.append("* El dia no es valido.")
            if not hour.isnumeric() or int(hour) < 10 or int(hour) > 14:
                errors.append("* La hora debe estar entre las 10 y las 12.")
            first = False
            valid = len(errors) == 0
            # Si la lista de errores esta vacia se asume que es valido todo.
            if valid:
                exists = False
                turnosFile = open('turnos.txt','r')
                turnos = turnosFile.readlines()
                turnosModificados = []
                for turno in turnos:
                    turno = turno.replace('\n', '')
                    if turno.endswith(str(dni)):
                        fecha = "".join([year, month.zfill(2), day.zfill(2), hour])
                        turno = f"{fecha};{dni}"
                        # valida si el turno existe y si es asi el if de abajo va a reiniciar el while
                        exists = fecha in lista_turnos
                    turnosModificados.append(f"{turno}\n")
                turnosFile.close()
                if exists:
                    print("El turno existe, por favor intente de nuevo.")
                    # con este parametro reiniciamos el while para que el usuario ingrese nuevos datos
                    valid = False
                else:
                    turnosFile = open('turnos.txt','w+')
                    turnosFile.writelines(turnosModificados)
                    turnosFile.close()
                    print("Turno modificado con exito.")
    else:
        print("El DNI ingresado no existe como usuario registrado o no posee un turno activo.")

def lista_turnos_2(lista_nombres,lista_apellidos,lista_dni):
    try:
        turnos = open('turnos.txt','r')
    except IOError:
        print("No se pudo leer el archivo")
    else:
        print("Listado de turnos en el sistema: ")
        dia_in=input("Ingrese el dia: ")
        while dia_in.isnumeric()!=True or int(dia_in)<=0 or int(dia_in)>=32:
            print("Ingreso inválido")
            dia_in=input("Ingrese el dia: ")
        if len(dia_in)==1:
            dia_in=dia_in.zfill(2) 
        mes_in=input("Ingrese el mes: ")
        while mes_in.isnumeric()!=True or int(mes_in)<=0 or int(mes_in)>=13:
            print("Ingreso inválido")
            mes_in=input("Ingrese el mes: ")
        if len(mes_in)==1:
            mes_in=mes_in.zfill(2)  #El metodo Zfill agrega ceros a la izquierda
        anio_in=input("Ingrese el año: ")
        while anio_in.isnumeric()!=True or int(anio_in)<=2020 or int(anio_in)>=2030:
            print("Ingreso inválido")
            anio_in=input("Ingrese el año: ")
        lista_dni_turno=[]
        lista_apellidos_turno=[]
        lista_nombres_turno=[]
        lista_hora=[]
        lista_anio=[]
        linea = turnos.readline()
        while linea != '':	
            linea = linea.rstrip()
            lista_turno = linea.split(';')
            turno=lista_turno[0]
            dni=lista_turno[1]
            anio=turno[0:4]
            mes=turno[4:6]
            dia=turno[6:8]
            hora=turno[8:]
            if dia==dia_in and mes==mes_in and anio==anio_in:
                pos=lista_dni.index(dni)
                nombre=lista_nombres[pos]
                apellido=lista_apellidos[pos]
                lista_dni_turno.append(dni)
                lista_apellidos_turno.append(apellido)
                lista_nombres_turno.append(nombre)
                lista_hora.append(hora)
                lista_anio.append(anio)
            linea = turnos.readline()
        if len(lista_dni_turno)!=0:
            ordenar_turnos(lista_dni_turno,lista_apellidos_turno,lista_nombres_turno,lista_hora)
            m=[[0]*7 for i in range(len(lista_dni_turno))]
            filas=len(m)
            columnas=len(m[0])
            for f in range (filas):
                for c in range (columnas):
                    m[f][0]=lista_dni_turno[f]
                    m[f][1]=lista_apellidos_turno[f]
                    m[f][2]=lista_nombres_turno[f]
                    m[f][3]=dia
                    m[f][4]=mes
                    m[f][5]=lista_hora[f]
                    m[f][6]=anio
            for t in range(filas):
                print(f'DNI:{int(m[t][0]):08d} NOMBRE: {m[t][2]:<15s}' + 
                    f' APELLIDO: {m[t][1]:<15s} AÑO: {int(anio):<04d}'+
                    f' MES:{int(mes):<02d} DIA:{int(dia):02d}' +
                    f' HORA:{int(m[t][5]):02d}' )
        else:
            print("No hay turnos ese dia")

def ordenar_turnos(lista_dni,lista_apellido,lista_nombre,lista_hora):
    """
    Se ordena las listas de la pacientes según los apellidos.
    Se utiliza el metodo de incersión.
    """
    for i in range(1,len(lista_apellido)):
        apellido_aux=lista_apellido[i]
        nombre_aux=lista_nombre[i]
        dni_aux=lista_dni[i]
        hora_aux=lista_hora[i]
        j=i
        while j>0 and lista_hora[j-1]>hora_aux:
            lista_apellido[j]=lista_apellido[j-1]
            lista_nombre[j]=lista_nombre[j-1]
            lista_dni[j]=lista_dni[j-1]
            lista_hora[j]=lista_hora[j-1]
            j=j-1
        lista_apellido[j]=apellido_aux
        lista_nombre[j]=nombre_aux
        lista_dni[j]=dni_aux
        lista_hora[j]=hora_aux

# Datos de prueba para realizar tests de funcionamiento.
def test(counter = 3):

    def init_test():
        test={}
        return test

    def add_test(test,data):
        keys = test.keys()
        new_key = len(keys) + 1
        test.update({str(new_key):data})

    def get_test(test):
        if len(test.keys())>0:
            return test.popitem() # Saca el último dato ingresado.
        else:
            raise ValueError

    def check_test(test):
        return len(test)==0

    test = init_test()
    apellidos = ["Aaaaa","Bbbbb","Ccccc","Dddddd","Eeeeee","Ffffff"]
    nombres = ["Rrrrr","Ssssss","Ttttttt","Oooooo","Zzzzzzz"]
    while counter >0:
        dni = str(random.randint(1000000,99999999)) +";" # DNI al azar.
        apellido = str(random.choice(apellidos)) +";" # Elijo un apellido de la lista.
        nombre = str(random.choice(nombres)) +";" # Elijo un nombre de la lista.
        edad = str(random.randint(18,99))
        data = dni + apellido + nombre + edad

        add_test(test,data) # agrego datos de prueba a la pila.
        counter -=1
    lista_dni,lista_apellido,lista_nombre,lista_edad = pacientes_a_listas()
    while check_test(test) == False: # Chequeo que la pila no este vacía.
        dato=list(get_test(test))
        dato = "".join(dato)
        pacient = dato[1:100]
        pacientes=pacient.split(";")
        lista_dni.append(pacientes[0])
        lista_apellido.append(pacientes[1])
        lista_nombre.append(pacientes[2])
        lista_edad.append(pacientes[3])
    ordenar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad)
    grabar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad)

def run():
    pass

if __name__ == '__main__':
    run()