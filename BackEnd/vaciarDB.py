import mysql.connector

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host="localhost",  # Cambia esto si la base de datos no está en el mismo servidor
    user="machinez",
    password="1234",
    database="storedb"
)

# Crear un objeto cursor
cursor = conn.cursor()

# Obtener la lista de tablas en la base de datos
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Eliminar todas las tablas una por una
for table in tables:
    table_name = table[0]
    cursor.execute(f"DROP TABLE {table_name}")

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Todas las tablas de 'storedb' han sido eliminadas.")
