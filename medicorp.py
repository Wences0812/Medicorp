import os; clear = lambda: os.system('cls'); clear()
import sys
from modulo_medicorp import *


def run():
    print("MEDICORP SOFTWARE SOLUTIONS")
    lista_usuarios=("medicorp","admin") # Tupla
    lista_contrasenias=("1234","4321abc") # Tupla
    permitido,user=login(lista_usuarios,lista_contrasenias)
    clear()
    if permitido == True:
        print(f'El usuario {user} ha ingresado correctamente.')
    else:
        return print("Los datos de login son incorrectos")
    while True:
        clear()
        menu_selection = menu()
        # Se ejecutan las distintas funciones selecionadas.
        if menu_selection == 1: #Dar de alta un paciente.
            alta_paciente()
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 2:
            print("Ha selecionado dar de alta un turno.")
            dni = input("Ingrese el DNI del paciente: ")
            alta_turno(dni)
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 3: # Modificar los datos de un paciente.
            clear()
            d,a,n,e = pacientes_a_listas()
            modificar_paciente(d, a, n, e)
            ordenar_pacientes(d,a,n,e)
            grabar_pacientes(d,a,n,e)

            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 4: # Dar de baja un paciente.
            d,a,n,e = pacientes_a_listas()
            baja_paciente(d,a,n,e)
            grabar_pacientes(d,a,n,e)
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 5:
            dni = input("Ingrese el DNI a dar de baja el turno: ")
            borrar_turno(dni)
            exit = input("Presione enter para continuar al menu principal")
            
        if menu_selection == 6:
            d,a,n,e = pacientes_a_listas()
            lista_turnos_2(n, a, d)
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 7: # Listar en pantalla todos los pacientes dados de alta.
            clear()
            d,a,n,e = pacientes_a_listas()
            ordenar_pacientes(d,a,n,e)
            grabar_pacientes(d,a,n,e)
            listar_pacientes()
            print()
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 8:
            print("Ha elegido buscar turno según DNI.")
            buscar_turno()
            exit = input("Presione enter para continuar al menu principal")
            
        if menu_selection == 9: # Para cargar datos de prueba.
            test()
            print("Datos de prueba cargados satisfactoriamente.")
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 10:
            buscar_pacientes()
            exit = input("Presione enter para continuar al menu principal")

        if menu_selection == 11:
            print("Ha elegido listar pacientes según edad selecionada.")
            d,a,n,e = pacientes_a_listas()
            listadoMayores(d,a,n,e)
            exit = input("Presione enter para continuar al menu principal")
            
        if menu_selection == 12:
            dni = input("Ingrese el DNI del paciente para modificar el turno: ")
            dni = validar_dni(dni)
            modificar_turno(dni)
            exit = input("Presione enter para continuar al menu principal")
        if menu_selection == 0:
            break
            
    clear()

if __name__ == '__main__':
    run()
    print("Gracias por utilizar MEDICORP SOFTWARE SOLUTIONS")