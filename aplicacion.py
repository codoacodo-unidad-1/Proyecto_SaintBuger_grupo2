import sqlite3
# Configurar la conexión a la base de datos SQLite
DATABASE = 'saint_burguer.db'

def get_db_connection(): 
    conn = sqlite3.connect(DATABASE) 
    conn.row_factory = sqlite3.Row 
    return conn

# Crear la tabla 'burguers' si no existe

conn = get_db_connection() 
cursor = conn.cursor() 
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS burguers ( 
            codigo INTEGER PRIMARY KEY, 
            descripcion TEXT NOT NULL, 
            cantidad INTEGER NOT NULL, 
            precio REAL NOT NULL ) ''') 
conn.commit() 
cursor.close() 
conn.close()



# Limpiamos la pantalla    
print("\033[H\033[J")       
    

# -------------------------------------------------------------------
# Definimos la clase "Inventario"
# -------------------------------------------------------------------
class Inventario: 
    def __init__(self): 
        self.conexion = get_db_connection() 
        self.cursor = self.conexion.cursor()     
        
class Producto:
    def __init__(self, codigo, descripcion, cantidad, precio):
        self.codigo=codigo
        self.descripcion=descripcion    
        self.cantidad=cantidad
        self.precio=precio

def Modificar (self, nueva_descripcion, nueva_cantidad, nuevo_precio):
    self.descripcion = nueva_descripcion
    self.cantidad = nueva_cantidad
    self.precio = nuevo_precio

def agregar_producto(self, codigo, descripcion, cantidad, precio):
    producto_existente =self.consultar_producto(codigo)
    if producto_existente:
        print("Ya existe un producto con este código.")
        return False
    
    nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
    self.curso.execute("INSERT INTO burguers VALUES (?,?,?,?)" , (codigo,descripcion,cantidad,precio))
    self.conexion.commit()
    return True

def consultar_producto(self,codigo):
    self.cursor.execute ("SELECT * FROM burguers WHERE codigo= ?" ,  (codigo,))
    row = self.cursor.fetchone()
    if row:
        codigo, descripcion, cantidad, precio = row
        return Producto(codigo, descripcion,cantidad,precio)
    return False
    
            
def modificar_producto(self, codigo,nueva_descripcion,nueva_cantidad,nuevo_precio):
    producto = self.consultar(codigo)
    if producto:
        producto.modificar(nueva_descripcion,nueva_cantidad,nuevo_precio)
        self.cursor.execute("UPDATE  burguers SET descripcion = ?, cantidad= ?, precio = ? where codigo=?",(nueva_descripcion,nueva_cantidad, nuevo_precio, codigo))
        self.conexion.commit()
        