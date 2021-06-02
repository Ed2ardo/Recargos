# from recargos import *
import sqlite3
seleccion = 0
while seleccion == 0:
    print('Escoge una opcion')
    seleccion = int(input('''
        1. Agregar nuevo empleado, 
        2. consultar empleado,
        3. Salir.
        Ingrese opción: '''))
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



while seleccion == 1:
    id = input('Inserte número de identificación. Sin puntos ni comas: ')
    nombre = input('Inserte nombres completos del empleado: ')
    cargo = input('Cargo del empleado: ')
    salario = int(input('Ingrese salario del empleado. Sin puntos ni comas: '))
    fIngreso = input('Ingrese fecha de ingreso. dd/mm/aaaa: ')
    def nuevoEmpleado(id, nombre, cargo, salario, fechaIngreso):
        datos = [(int(id), nombre, cargo, salario, fechaIngreso)]

        miConexion = sqlite3.connect('Empleados')
        miCursor = miConexion.cursor()
        miCursor.executemany("INSERT INTO EMPLEADOS VALUES(?,?,?,?,?)", datos)
        print ('DATOS ALMACENADOS CON EXITO')
        miConexion.commit()
        miConexion.close()
    nuevoEmpleado(id, nombre, cargo, salario, fIngreso)
    print('Escoge una opcion')
    seleccion = int(input('''
        1. Agregar nuevo empleado, 
        2. consultar empleado,
        3. Salir.
        Ingrese opción: '''))
while seleccion == 2:
    id = int(input('Ingrese ID: '))
    miConexion = sqlite3.connect('Empleados')
    miCursor = miConexion.cursor()
    miCursor.execute(f'SELECT * FROM EMPLEADOS WHERE ID={id}')
    empleados = miCursor.fetchall()
    for i in empleados:
        print (i)
    miConexion.commit()
    miConexion.close()
    print('Escoge una opcion')
    seleccion = int(input('''
        1. Agregar nuevo empleado, 
        2. consultar empleado,
        3. Salir.
        Ingrese opción: '''))

while seleccion == 3:
    print ('Has salido.')
    seleccion = 0

print (seleccion)
