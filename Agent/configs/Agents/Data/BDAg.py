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


# In[4]:

import json
import os

load_dotenv()

User = os.getenv("user")
Pass = os.getenv("password")
Host = os.getenv("host")



# In[5]:


def conectar_mysql():
    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="Turismo_Agente"
    )

def conectar_mysql2():
    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="Autobus"
    )

def conectar_mysql3():
    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="TArero"
    )


# In[7]:


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

cargar_contexto(1)  # usuario con id=1



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

    return f"Itinerario agregado para folio {folio}."


# In[4]:


def actualizar(folio, cambios):

    conn = conectar_mysql()
    cursor = conn.cursor()
    
    if isinstance(cambios, str):
        cambios = json.loads(cambios)

    cursor.execute("""
        SELECT fecha_inicio, fecha_fin 
        FROM reservas 
        WHERE folio = %s
    """, (folio,))
    
    result = cursor.fetchone()
    fecha_inicio_actual, fecha_fin_actual = result if result else (None, None)

    nueva_fecha_inicio = fecha_inicio_actual
    nueva_fecha_fin = fecha_fin_actual


    # 1. Detectar cambios desde itinerario
    
    if "itinerario" in cambios:
        for item in cambios["itinerario"]:
            fecha_original = item.get("fecha_original")
            fecha_nueva = item.get("fecha_nueva")

            if not fecha_original or not fecha_nueva:
                continue

            # Si coincide con inicio
            if fecha_original == str(fecha_inicio_actual):
                nueva_fecha_inicio = fecha_nueva

            # Si coincide con fin
            if fecha_original == str(fecha_fin_actual):
                nueva_fecha_fin = fecha_nueva

    # 2. Actualizar reservas

    campos_reservas = {"num_viajeros", "fecha_inicio", "fecha_fin"}
    set_reservas = []
    valores_reservas = []

    # Campos directos
    for campo in {"num_viajeros"} & cambios.keys():
        set_reservas.append(f"{campo} = %s")
        valores_reservas.append(cambios[campo])

    # Fechas detectadas dinámicamente
    if nueva_fecha_inicio != fecha_inicio_actual:
        set_reservas.append("fecha_inicio = %s")
        valores_reservas.append(nueva_fecha_inicio)

    if nueva_fecha_fin != fecha_fin_actual:
        set_reservas.append("fecha_fin = %s")
        valores_reservas.append(nueva_fecha_fin)

    if set_reservas:
        sql_reservas = f"""
            UPDATE reservas 
            SET {', '.join(set_reservas)} 
            WHERE folio = %s
        """
        cursor.execute(sql_reservas, valores_reservas + [folio])

    # 3. Actualizar itinerario

    if "itinerario" in cambios:
        for item in cambios["itinerario"]:
            tipo = item.get("tipo")
            fecha_original = item.get("fecha_original")

            nombre = item.get("nombre")
            fecha_nueva = item.get("fecha_nueva")
            detalles = item.get("detalles")

            if not tipo or not fecha_original:
                continue

            set_clauses = []
            valores = []

            if nombre is not None:
                set_clauses.append("nombre = %s")
                valores.append(nombre)

            if fecha_nueva is not None:
                set_clauses.append("fecha = %s")
                valores.append(fecha_nueva)

            if detalles is not None:
                set_clauses.append("detalles = %s")
                valores.append(detalles)

            if not set_clauses:
                continue

            query = f"""
                UPDATE itinerario
                SET {', '.join(set_clauses)}
                WHERE folio = %s AND tipo = %s AND fecha = %s
            """

            valores_main = valores + [folio, tipo, fecha_original]
            cursor.execute(query, valores_main)

            # Fallback
            if cursor.rowcount == 0 and fecha_nueva is not None:
                query_fallback = """
                    UPDATE itinerario
                    SET fecha = %s
                    WHERE folio = %s AND fecha = %s
                """
                cursor.execute(query_fallback, [fecha_nueva, folio, fecha_original])

                if cursor.rowcount == 0:
                    print(f"[WARN] No se actualizó registro: folio={folio}, tipo={tipo}, fecha={fecha_original}")

    conn.commit()
    cursor.close()
    conn.close()

    return f"Reserva/Itinerario {folio} actualizado correctamente."


# In[15]:


def cancelar_reserva(folio, tipo=None, nombre=None):
    """
    Cancela reservas de forma flexible:
    
    Casos:
    - folio: cancela todo (UPDATE estado = 'Cancelado')
    - folio + tipo: elimina por tipo (DELETE)
    - folio + nombre: elimina por nombre (LIKE)
    - folio + tipo + nombre: elimina específico (LIKE)

    Parámetros:
        folio  : obligatorio
        tipo   : opcional
        nombre : opcional
    """

    # Normalización segura
    if tipo in ["NONE", "", "null", None]:
        tipo = None
    else:
        tipo = tipo.lower()

    if nombre in ["NONE", "", "null", None]:
        nombre = None

    conn = conectar_mysql()
    cursor = conn.cursor()

    # Caso 1: cancelar TODO
    if not tipo and not nombre:
        query = "UPDATE reservas SET estado = %s WHERE folio = %s"
        valores = ("Cancelado", folio)

    # Caso 2: folio + tipo
    elif tipo and not nombre:

        query = """
            DELETE FROM itinerario
            WHERE folio = %s AND tipo = %s
        """
        valores = (folio, tipo)

    # Caso 3: folio + nombre (LIKE)
    elif nombre and not tipo:

        query = """
            DELETE FROM itinerario
            WHERE folio = %s AND nombre LIKE %s
        """
        valores = (folio, f"%{nombre}%")

    # Caso 4: folio + tipo + nombre (LIKE)
    else:
 
        query = """
            DELETE FROM itinerario
            WHERE folio = %s AND tipo = %s AND nombre LIKE %s
        """
        valores = (folio, tipo, f"%{nombre}%")

    cursor.execute(query, valores)
    conn.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conn.close()

    if filas_afectadas == 0:
        return "No se encontró ninguna reserva con los criterios proporcionados."

    return f"{filas_afectadas} registro(s) afectados correctamente."




# In[11]:


def consultar_bus(origen, destino, fecha):
    conn = conectar_mysql2()
    try:
        cursor = conn.cursor()
        query = """
            SELECT 
                c.fecha_salida, 
                c.hora_salida, 
                c.fecha_llegada, 
                c.hora_llegada,
                c.precio,
                p.duracion, 
                t_origen.nombre AS origen, 
                t_destino.nombre AS destino, 
                a.marca
            FROM Salidas c
            INNER JOIN Autobuses a 
                ON c.id_autobus = a.id_autobus
            INNER JOIN Rutas p 
                ON c.id_ruta = p.id_ruta
            INNER JOIN Terminales t_origen 
                ON p.origen = t_origen.id_terminal
            INNER JOIN Terminales t_destino 
                ON p.destino = t_destino.id_terminal
            WHERE t_origen.ubicacion LIKE %s
              AND t_destino.ubicacion LIKE %s
              AND c.fecha_salida = %s;
        """

        cursor.execute(query, (f"%{origen}%", f"%{destino}%", fecha))
        resultados = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return resultados




# In[13]:


def buscar_vuelo(origen, destino, fecha):
    conn = conectar_mysql3()
    try:
        cursor = conn.cursor()
        query = """
            SELECT 
                c.hora_salida, 
                c.hora_llegada, 
                c.fecha_salida, 
                t_origen.codigo AS origen, 
                t_destino.codigo AS destino, 
                a.nombre AS aerolinea
            FROM vuelos c
            INNER JOIN aeropuertos t_origen 
                ON c.origen_codigo = t_origen.codigo
            INNER JOIN aeropuertos t_destino 
                ON c.destino_codigo = t_destino.codigo
            INNER JOIN aerolineas a 
                ON c.aerolinea_id = a.id
            WHERE t_origen.codigo = %s
              AND t_destino.codigo = %s
              AND c.fecha_salida = %s;
        """

        cursor.execute(query, (origen, destino, fecha))
        resultados = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return resultados



# In[6]:


def consultar_folio(folio):
    conn = conectar_mysql()
    cursor = conn.cursor(dictionary=True)  
    
    query = """
        SELECT tipo, nombre, ciudad, fecha, detalles
        FROM itinerario
        WHERE folio = %s
        ORDER BY fecha ASC
    """
    
    cursor.execute(query, (folio,))
    resultados = cursor.fetchall() 
    
    cursor.close()
    conn.close()
    
    respuesta = {
        "folio": folio,
        "itinerario": resultados
    }
 
    return respuesta


# In[ ]:




