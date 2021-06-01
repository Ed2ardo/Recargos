# from recargos import *
import sqlite3

def menu():
    print('Escoge una opcion')
    seleccion = int(input('''
        1. Agregar nuevo empleado, 
        2. consultar empleado,
        3. Salir.
        Ingrese opción: '''))
    return seleccion
seleccion = menu()
print(seleccion)


# miConexion = sqlite3.connect('Empleados') #Crear BBDD
# miCursor = miConexion.cursor()
# miCursor.execute('''
#     CREATE TABLE EMPLEADOS (
#     ID INTEGER PRIMARY KEY,
#     NOMBRES VARCHAR(50),
#     CARGO VARCHAR(50),
#     SALARIO VARCHAR(20),
#     FECHA INGRESO VARCHAR(20))
#     ''')
# miConexion.commit()
# miConexion.close()



def nuevoEmpleado(id, nombre, cargo, salario, fechaIngreso):
    datos = [(int(id), nombre, cargo, salario, fechaIngreso)]

    miConexion = sqlite3.connect('Empleados')
    miCursor = miConexion.cursor()
    miCursor.executemany("INSERT INTO EMPLEADOS VALUES(?,?,?,?,?)", datos)
    print ('DATOS ALMACENADOS CON EXITO')
    miConexion.commit()
    miConexion.close()


def consultarEmpleados(id):
    # id = id
    miConexion = sqlite3.connect('Empleados')
    miCursor = miConexion.cursor()
    miCursor.execute(f'SELECT * FROM EMPLEADOs WHERE ID={id}')
    empleados = miCursor.fetchall()
    for i in empleados:
        print (i)
    miConexion.commit()
    miConexion.close()


while seleccion == 1:
    id = input('Inserte número de identificación. Sin puntos ni comas: ')
    nombre = input('Inserte nombres completos del empleado: ')
    cargo = input('Cargo del empleado: ')
    salario = int(input('Ingrese salario del empleado. Sin puntos ni comas: '))
    fIngreso = input('Ingrese fecha de ingreso. dd/mm/aaaa: ')
    nuevoEmpleado(id, nombre, cargo, salario, fIngreso)
    menu()
while seleccion == 2:
    id = int(input('Ingrese ID: '))
    consultarEmpleados(id)
    menu()
while seleccion == 3:
    print ('Has salido.')
    seleccion = 0

print (seleccion)
