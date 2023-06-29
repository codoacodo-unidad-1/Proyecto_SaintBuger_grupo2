import sqlite3
# Configurar la conexión a la base de datos SQLite
DATABASE = 'saint_burguer.db'

def conectar():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


#----------------------------------------------
# Esta funcion crea la tabla "productos" en la
# base de datos, en caso de que no exista.
#----------------------------------------------
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS burguers (
                    codigo INT PRIMARY KEY,
                    descripcion VARCHAR(255),
                    stock INT,
                    precio FLOAT)
            """)
    conn.commit()
    cursor.close()
    conn.close()


#----------------------------------------------
# Esta funcion da de alta un producto en la
# base de datos.
#----------------------------------------------
def alta_producto(cod, desc, stock, valor):
    print()
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO burguers(codigo, descripcion, stock, precio)
                    VALUES(?,?,?,?) """,(cod, desc, stock, valor))
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error: Producto no creado.")
    else:
        print ("Producto creado correctamente.")
    print("-"*30)

#----------------------------------------------
# Muestra en la pantalla los datos de un  
# producto a partir de su código.
#----------------------------------------------
def consultar_producto(cod):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM burguers 
                            WHERE codigo=?""", (cod,))
        producto = cursor.fetchone()
        print()
        print(f"Código     : {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Stock      : {producto['stock']}")
        print(f"Precio     : {producto['precio']}")
        print("-"*30)
        conn.commit()
        cursor.close()
        conn.close()
        return producto
    except:
        print("Error posible: registro no encontrado")
        print("-"*30)
        return False


#----------------------------------------------
# Modifica los datos de un producto a partir
# de su código.
#----------------------------------------------
def modificar_producto(cod, nueva_desc, nuevo_stock, nuevo_precio):
    producto = consultar_producto(cod)
    if producto:
        print("\nNuevos datos del producto:")
        print(f"Descripción: {nueva_desc}")
        print(f"Stock      : {nuevo_stock}")
        print(f"Precio     : {nuevo_precio}")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""UPDATE burguers SET descripcion=?, stock=?, precio=?
                            WHERE codigo=?""", (nueva_desc, nuevo_stock, nuevo_precio, cod))
        conn.commit()
        
        print("El producto ha sido modificado correctamente.")
    else:
        print("El producto no se encuentra en la base de datos.")
    
    cursor.close()
    conn.close()
    print("-"*30)
    
    
def eliminar_producto(cod):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM burguers WHERE codigo= ?", (cod,))
        producto = cursor.fetchone()
        print()
        print("Producto eliminado.")
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error posible: registro no encontrado")
        print("-"*30)
        return False    


#----------------------------------------------
# Lista todos los productos en la base de datos.
#----------------------------------------------
def listar_productos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM burguers")
        productos = cursor.fetchall()
        print("\nListado de productos:")
        print("-" * 30)
        for producto in productos:
            print(f"Código     : {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Stock      : {producto['stock']}")
            print(f"Precio     : {producto['precio']}")
            print("-" * 30)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error al listar los productos.")
        print("-" * 30)


#----------------------------------------------
# Ejemplos de uso de las funciones implementadas
#----------------------------------------------
#crear_tabla()

#alta_producto(1, "Genesis", 30, 1600)
#lta_producto(2, "Adam", 30, 1900)

consultar_producto(1)
consultar_producto(2)

#alta_producto(3, "Moises", 30, 1900)
#modificar_producto(3, "Goliath", 30, 2000)
#consultar_producto(3)
#eliminar_producto(3)

listar_productos()
