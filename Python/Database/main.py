import sqlite3

def insertaAlumno(cursor ,id, nombre, apellido):
    cursor.execute(f'INSERT INTO Alumnos (id, Nombre, Apellido) VALUES ({id}, "{nombre}", "{apellido}");')
def main():
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    # Elimina la tabla si existe (para crearla de nuevo)
    cursor.execute('DROP TABLE IF EXISTS Alumnos;')

    cursor.execute('CREATE TABLE Alumnos (id INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT);')
    insertaAlumno(cursor, 1, 'Pepe', 'Sánchez')
    insertaAlumno(cursor, 2, 'Marta', 'Gómez')
    insertaAlumno(cursor, 3, 'Laura', 'García')
    insertaAlumno(cursor, 4, 'Francisco', 'Aliaga')
    insertaAlumno(cursor, 5, 'Roberto', 'Martínez')
    insertaAlumno(cursor, 6, 'Alberto', 'Colomer')
    insertaAlumno(cursor, 7, 'María', 'González')
    insertaAlumno(cursor, 8, 'Teresa', 'Ramírez')
    connection.commit()

    cursor.execute('SELECT * FROM Alumnos WHERE Nombre="Francisco"')

    data = cursor.fetchall()
    print(data)

    cursor.close()
    connection.close()
if __name__ == '__main__':
    main()
