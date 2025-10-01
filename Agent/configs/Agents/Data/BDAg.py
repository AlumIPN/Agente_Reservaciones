import sqlite3

def consultar_hoteles(ciudad):
    conn = sqlite3.connect('Turismo_Agente.db')
    cursor = conn.cursor()
    query = """
        SELECT h.nombre, h.direccion, h.estrellas, h.servicios
        FROM hoteles h
        JOIN ciudades c ON h.ciudad_id = c.id
        WHERE c.nombre LIKE ?
    """
    patron = f"%{ciudad}%"
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

def consultar_restaurantes(ciudad):
    conn = sqlite3.connect('Turismo_Agente.db')
    cursor = conn.cursor()
    query = """
        SELECT r.nombre, r.direccion, r.tipo_comida, r.descripcion
        FROM restaurantes r
        JOIN ciudades c ON r.ciudad_id = c.id
        WHERE c.nombre LIKE ?
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados



def consultar_atracciones(ciudad):
    conn = sqlite3.connect('Turismo_Agente.db')
    cursor = conn.cursor()
    query = """
        SELECT a.nombre, a.descripcion, a.tipo
        FROM atracciones a
        JOIN ciudades c ON a.ciudad_id = c.id
        WHERE c.nombre LIKE ?
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados




def consultar_transportes(ciudad):
    conn = sqlite3.connect('Turismo_Agente.db')
    cursor = conn.cursor()
    query = """
        SELECT t.empresa, t.tipo, t.contacto
        FROM transportes t
        JOIN ciudades c ON t.ciudad_id = c.id
        WHERE c.nombre LIKE ?
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


def consultar_autos(ciudad):
    conn = sqlite3.connect('Turismo_Agente.db')
    cursor = conn.cursor()
    query = """
        SELECT v.nombre, v.direccion, v.telefono
        FROM agencias_autos v
        JOIN ciudades c ON v.ciudad_id = c.id
        WHERE c.nombre LIKE ?
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


