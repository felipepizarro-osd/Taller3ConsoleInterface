
import psycopg2

def juego(username):
    print("Comienza el juego")


print("Inicio de sesion")
print("opciones: 1 --> Login")
print("opciones: 2 --> Registrar")

opcion = input("eliga la opcion: ")

if opcion == '1':  
    print("Menu registro") 
    user_name = input("escriba su nombre de usuario : ")
    user_password = input ("escriba su contraseña : ")
    entry = False 

    conn = psycopg2.connect(
    dbname="taller3",
    user = "postgres",
    password = "root",
    host = "localhost",
    port = "5432"
    ) 

    cursor = conn.cursor()
    query = '''select * from entrenador where password = %s and nombre = %s'''
    cursor.execute(query,(user_password,user_name))
    row = cursor.fetchone()

    if row is not None :
        juego(user_name)
    else :
        print("error")
    conn.commit()
    conn.close()
    
elif opcion == '2':
    print ("registro de usuario nuevo")
    username = input("ingrese su nombre ")
    password = input("ingrese su password ")
    nickname = input("ingrese un apodo de su personaje ")
    fecha = input("ingrese la fecha de nacimiento ")
    age = input("ingrese su edad ")

    connect = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    cur = connect.cursor()
    query = '''INSERT INTO entrenador (nombre, password ,nombre_usuario , fecha_nac , edad) VALUES (%s,%s,%s,%s,%s)'''

    cur.execute(query,(username,password,nickname,fecha,age))
    print("Data Saved")

    connect.commit()
    connect.close()

