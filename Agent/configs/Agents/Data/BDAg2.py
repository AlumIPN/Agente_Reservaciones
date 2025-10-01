#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[5]:


def conectar_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Imag35ql",
        database="Turismo_Agente"
    )


# In[3]:


def consultar_usuario(nombre, apellidos):
    conn = conectar_mysql()
    cursor = conn.cursor()
    query = """
        SELECT nombre, apellidos, edad, correo, telefono
        FROM usuarios
        WHERE nombre = %s AND apellidos = %s
    """
    cursor.execute(query, (nombre, apellidos))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados


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


# In[ ]:




