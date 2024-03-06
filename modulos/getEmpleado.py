from MySQLdb import create_engine, MetaData, Table, select

def obtener_jefe(nombre_base_datos):
    
    engine = create_engine(f'mysql://localhost/{nombre_base_datos}')
    connection = engine.connect()

 
    metadata = MetaData()

    
    empleados = Table('empleados', metadata, autoload=True, autoload_with=engine)

    
    consulta = select([empleados.c.nombre_puesto,
                       empleados.c.nombre,
                       empleados.c.apellidos,
                       empleados.c.email]).where(empleados.c.nombre_puesto == 'Jefe')

    resultado = connection.execute(consulta)

    
    resultados = []
    for fila in resultado:
        resultados.append({
            'Puesto': fila['nombre_puesto'],
            'Nombre': fila['nombre'],
            'Apellidos': fila['apellidos'],
            'Email': fila['email']
        })

   
    connection.close()

    return resultados


nombre_base_datos = 'nombre_base_de_datos'

resultados = obtener_jefe(nombre_base_datos)
for resultado in resultados:
    print(resultado)





