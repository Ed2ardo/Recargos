nuevoEmpleado = input('¿Agregar empleado? \n 1: Si, 2:No ')
empleado = 1
empleados = []

while nuevoEmpleado == '1':
    id = input ('Identificación: ')
    nombre = input ('Nombres y apellidos: ')
    cargo = input ('Ingrese cargo: ')
    salario = int(input('Ingrese Salario: '))
    fechaIngreso = input ('Ingrese fecha de ingreso: "dd/mm/aaaa": ')

    empleados.append([id, nombre, salario, fechaIngreso])
    nuevoEmpleado = input('¿Agregar empleado? \n 1: Si, 2:No ')