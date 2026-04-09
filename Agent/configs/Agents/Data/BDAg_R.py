#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[2]:


import datetime


# In[3]:


from configs.Agents.Data.context_variables import context_variables


# In[3]:
from dotenv import load_dotenv


# In[5]:


import os

load_dotenv()

User = os.getenv("user")
Pass = os.getenv("password")
Host = os.getenv("host")



# In[6]:


def conectar_mysql():
    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="Turismo_Agente"
    )


# In[5]:


def cargar_contexto(usuario_id):
    conn = conectar_mysql()
    cursor = conn.cursor()
    
    query = """
        SELECT id, nombre, apellidos, edad, correo, telefono
        FROM usuarios
        WHERE id = %s
    """
    cursor.execute(query, (usuario_id,))
    usuario = cursor.fetchone()
    
    if usuario:
        context_variables["customer_context"]["CUSTOMER_ID"] = usuario[0]
        context_variables["customer_context"]["NAME"] = f"{usuario[1]} {usuario[2]}"
        context_variables["customer_context"]["AGE"] = usuario[3]
        context_variables["customer_context"]["EMAIL"] = usuario[4]
        context_variables["customer_context"]["PHONE"] = usuario[5]
        
        #context_variables["general_context"]["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.close()
    conn.close()
    return context_variables

# Ejemplo de uso
cargar_contexto(1)  # usuario con id=1
#print(contexto)



# In[22]:


def consultar_hoteles(ciudad):
    conn = conectar_mysql()
    cursor = conn.cursor()
    query = """
        SELECT h.nombre, h.direccion, h.estrellas, h.servicios
        FROM hoteles h
        JOIN ciudades c ON h.ciudad_id = c.id
        WHERE c.nombre LIKE %s
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


# In[27]:


def consultar_restaurantes(ciudad):
    conn = conectar_mysql()
    cursor = conn.cursor()
    query = """
        SELECT r.nombre, r.direccion, r.tipo_comida, r.descripcion
        FROM restaurantes r
        JOIN ciudades c ON r.ciudad_id = c.id
        WHERE c.nombre LIKE %s
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


# In[31]:


def consultar_atracciones(ciudad):
    conn = conectar_mysql()
    cursor = conn.cursor()
    query = """
        SELECT a.nombre, a.descripcion, a.tipo
        FROM atracciones a
        JOIN ciudades c ON a.ciudad_id = c.id
        WHERE c.nombre LIKE %s
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


# In[33]:


def consultar_transportes(ciudad):
    conn = conectar_mysql()
    cursor = conn.cursor()
    query = """
        SELECT t.empresa, t.tipo, t.contacto
        FROM transportes t
        JOIN ciudades c ON t.ciudad_id = c.id
        WHERE c.nombre LIKE %s
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


# In[36]:


def consultar_autos(ciudad):
    conn = conectar_mysql()
    cursor = conn.cursor()
    query = """
        SELECT v.nombre, v.direccion, v.telefono
        FROM agencias_autos v
        JOIN ciudades c ON v.ciudad_id = c.id
        WHERE c.nombre LIKE %s
    """
    patron = f"%{ciudad}%" 
    cursor.execute(query, (patron,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


# In[2]:


def reservar(folio, usuario_id, fecha_inicio, fecha_fin, num_viajeros, estado="confirmada"):
    conn = conectar_mysql()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO reservas (folio, usuario_id, fecha_inicio, fecha_fin, num_viajeros, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    valores = (
        folio,
        usuario_id,
        fecha_inicio,
        fecha_fin,
        num_viajeros,
        estado
    )
    
    cursor.execute(query, valores)
    conn.commit()  # importante para guardar cambios
    
    cursor.close()
    conn.close()

    print(query)
    
    return f"Reserva {folio} almacenada correctamente."


# In[3]:


def itinerario(folio, tipo, nombre, ciudad, fecha, detalles=None):
    """
    Almacena un registro en la tabla itinerario vinculado a un folio de reserva.
    
    Parámetros:
    - folio: identificador único de la reserva
    - tipo: tipo de actividad (hotel, restaurante, atracción, vuelo, renta_auto)
    - nombre: nombre del lugar o servicio
    - ciudad: ciudad o destino
    - fecha: fecha específica de la actividad (ej. check-in, vuelo de ida)
    - detalles: información adicional (dirección, notas)
    """
    if not detalles:
        detalles = "Ninguno"
        
    conn = conectar_mysql()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO itinerario (folio, tipo, nombre, ciudad, fecha, detalles)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    valores = (
        folio,
        tipo,
        nombre,
        ciudad,
        fecha,
        detalles,

    )
    
    cursor.execute(query, valores)
    conn.commit() 
    
    cursor.close()
    conn.close()
    print(query)
    return f"Itinerario agregado para folio {folio}."


# In[4]:


def actualizar(folio, cambios):
    """
    Actualiza registros en las tablas reservas e itinerario según los campos enviados.
    
    Parámetros:
        folio   : folio de la reserva/itinerario a actualizar
        cambios : diccionario con los campos a actualizar y sus nuevos valores
                  Ejemplo: {"num_viajeros": 4, "fecha_fin": "2026-04-10", "nombre": "Hotel Quinta Real"}
    """
    conn = conectar_mysql()
    cursor = conn.cursor()

    # Definir qué campos pertenecen a cada tabla
    campos_reservas = {"num_viajeros", "fecha_inicio", "fecha_fin"}
    campos_itinerario = {"nombre", "ciudad", "fecha", "detalles"}

    # Actualizar tabla reservas si hay cambios
    set_reservas = []
    valores_reservas = []
    for campo in campos_reservas & cambios.keys():
        set_reservas.append(f"{campo} = %s")
        valores_reservas.append(cambios[campo])
    if set_reservas:
        sql_reservas = f"UPDATE reservas SET {', '.join(set_reservas)} WHERE folio = %s"
        cursor.execute(sql_reservas, valores_reservas + [folio])

    # Actualizar tabla itinerario si hay cambios
    set_itinerario = []
    valores_itinerario = []
    for campo in campos_itinerario & cambios.keys():
        set_itinerario.append(f"{campo} = %s")
        valores_itinerario.append(cambios[campo])
    if set_itinerario:
        sql_itinerario = f"UPDATE itinerario SET {', '.join(set_itinerario)} WHERE folio = %s"
        cursor.execute(sql_itinerario, valores_itinerario + [folio])

    conn.commit()
    cursor.close()
    conn.close()

    return f"Reserva/Itinerario {folio} actualizado correctamente."


# In[9]:


def cancelar_reserva(folio):
    """
    Cancela una reserva cambiando el estado a 'Cancelado' en la tabla reservas.
    
    Parámetros:
        folio : folio de la reserva a cancelar
    """
    conn = conectar_mysql()
    cursor = conn.cursor()

    query = "UPDATE reservas SET estado = %s WHERE folio = %s"
    valores = ("Cancelado", folio)

    cursor.execute(query, valores)
    conn.commit()

    cursor.close()
    conn.close()

    return f"Reserva {folio} cancelada correctamente."


# In[8]:


def consultar_hoteles2(ciudad):
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






