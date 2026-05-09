"""
Módulo de acceso y gestión de bases de datos.

Este archivo centraliza todas las operaciones relacionadas con:
- Conexión a bases de datos.
- Gestión de reservaciones.
- Administración de itinerarios.
- Consultas de vuelos y autobuses.
- Actualización y cancelación de reservas.
- Carga de contexto del usuario.

Bases de datos utilizadas:
- Turismo_Agente
- Autobus
- TArero

El módulo actúa como capa de persistencia dentro de la arquitectura
multiagente, permitiendo a los agentes interactuar con información
estructurada de manera segura y organizada.

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

import mysql.connector
import datetime
import json
import os

from configs.Agents.Data.context_variables import context_variables
from dotenv import load_dotenv


# ============================================================================
# Carga de variables de entorno
# ============================================================================

"""
Carga las credenciales y variables sensibles desde el archivo `.env`.
"""
load_dotenv()

User = os.getenv("user")
Pass = os.getenv("password")
Host = os.getenv("host")


# ============================================================================
# Funciones de conexión
# ============================================================================

def conectar_mysql():
    """
    Establece conexión con la base de datos principal del sistema.

    Returns
    -------
    mysql.connector.connection.MySQLConnection
        Conexión activa a la base de datos `Turismo_Agente`.
    """

    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="Turismo_Agente"
    )


def conectar_mysql2():
    """
    Establece conexión con la base de datos de transporte terrestre.

    Returns
    -------
    mysql.connector.connection.MySQLConnection
        Conexión activa a la base de datos `Autobus`.
    """

    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="Autobus"
    )


def conectar_mysql3():
    """
    Establece conexión con la base de datos de vuelos.

    Returns
    -------
    mysql.connector.connection.MySQLConnection
        Conexión activa a la base de datos `TArero`.
    """

    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Pass,
        database="TArero"
    )


# ============================================================================
# Gestión de contexto del usuario
# ============================================================================

def cargar_contexto(usuario_id):
    """
    Carga la información del usuario desde la base de datos y actualiza
    el contexto global utilizado por los agentes.

    Parameters
    ----------
    usuario_id : int
        Identificador único del usuario.

    Returns
    -------
    dict
        Diccionario actualizado de variables de contexto.
    """

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

        context_variables["customer_context"]["NAME"] = (
            f"{usuario[1]} {usuario[2]}"
        )

        context_variables["customer_context"]["AGE"] = usuario[3]

        context_variables["customer_context"]["EMAIL"] = usuario[4]

        context_variables["customer_context"]["PHONE"] = usuario[5]

    cursor.close()
    conn.close()

    return context_variables


# Inicialización del contexto por defecto
cargar_contexto(1)


# ============================================================================
# Gestión de reservaciones
# ============================================================================

def reservar(
    folio,
    usuario_id,
    fecha_inicio,
    fecha_fin,
    num_viajeros,
    estado="confirmada"
):
    """
    Registra una nueva reservación en la base de datos.

    Parameters
    ----------
    folio : str
        Identificador único de la reservación.

    usuario_id : int
        Identificador del usuario.

    fecha_inicio : str
        Fecha inicial de la reservación.

    fecha_fin : str
        Fecha final de la reservación.

    num_viajeros : int
        Número total de viajeros.

    estado : str, optional
        Estado de la reservación.

    Returns
    -------
    str
        Mensaje de confirmación.
    """

    conn = conectar_mysql()
    cursor = conn.cursor()

    query = """
        INSERT INTO reservas (
            folio,
            usuario_id,
            fecha_inicio,
            fecha_fin,
            num_viajeros,
            estado
        )
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
    conn.commit()

    cursor.close()
    conn.close()

    print(query)

    return f"Reserva {folio} almacenada correctamente."


# ============================================================================
# Gestión de itinerarios
# ============================================================================

def itinerario(folio, tipo, nombre, ciudad, fecha, detalles=None):
    """
    Registra un elemento dentro del itinerario asociado a una reservación.

    Parameters
    ----------
    folio : str
        Identificador de la reservación.

    tipo : str
        Tipo de actividad o servicio.

    nombre : str
        Nombre del servicio o establecimiento.

    ciudad : str
        Ciudad asociada al itinerario.

    fecha : str
        Fecha de ejecución de la actividad.

    detalles : str, optional
        Información adicional relacionada.

    Returns
    -------
    str
        Mensaje de confirmación.
    """

    if not detalles:
        detalles = "Ninguno"

    conn = conectar_mysql()
    cursor = conn.cursor()

    query = """
        INSERT INTO itinerario (
            folio,
            tipo,
            nombre,
            ciudad,
            fecha,
            detalles
        )
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


# ============================================================================
# Actualización de reservaciones e itinerarios
# ============================================================================

def actualizar(folio, cambios):
    """
    Actualiza información de reservaciones e itinerarios.

    La función permite:
    - Actualizar fechas.
    - Modificar cantidad de viajeros.
    - Actualizar elementos del itinerario.
    - Realizar actualizaciones dinámicas según cambios detectados.

    Parameters
    ----------
    folio : str
        Identificador de la reservación.

    cambios : dict or str
        Diccionario o cadena JSON con los cambios a aplicar.

    Returns
    -------
    str
        Mensaje de confirmación.
    """

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

    fecha_inicio_actual, fecha_fin_actual = (
        result if result else (None, None)
    )

    nueva_fecha_inicio = fecha_inicio_actual
    nueva_fecha_fin = fecha_fin_actual

    # ------------------------------------------------------------------------
    # Detección automática de cambios en fechas
    # ------------------------------------------------------------------------

    if "itinerario" in cambios:

        for item in cambios["itinerario"]:

            fecha_original = item.get("fecha_original")
            fecha_nueva = item.get("fecha_nueva")

            if not fecha_original or not fecha_nueva:
                continue

            if fecha_original == str(fecha_inicio_actual):
                nueva_fecha_inicio = fecha_nueva

            if fecha_original == str(fecha_fin_actual):
                nueva_fecha_fin = fecha_nueva

    # ------------------------------------------------------------------------
    # Actualización de información principal
    # ------------------------------------------------------------------------

    set_reservas = []
    valores_reservas = []

    for campo in {"num_viajeros"} & cambios.keys():
        set_reservas.append(f"{campo} = %s")
        valores_reservas.append(cambios[campo])

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

    # ------------------------------------------------------------------------
    # Actualización del itinerario
    # ------------------------------------------------------------------------

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
                WHERE folio = %s
                AND tipo = %s
                AND fecha = %s
            """

            valores_main = valores + [
                folio,
                tipo,
                fecha_original
            ]

            cursor.execute(query, valores_main)

            # ----------------------------------------------------------------
            # Actualización alternativa si no existe coincidencia exacta
            # ----------------------------------------------------------------

            if cursor.rowcount == 0 and fecha_nueva is not None:

                query_fallback = """
                    UPDATE itinerario
                    SET fecha = %s
                    WHERE folio = %s
                    AND fecha = %s
                """

                cursor.execute(
                    query_fallback,
                    [fecha_nueva, folio, fecha_original]
                )

                if cursor.rowcount == 0:

                    print(
                        f"[WARN] No se actualizó registro: "
                        f"folio={folio}, "
                        f"tipo={tipo}, "
                        f"fecha={fecha_original}"
                    )

    conn.commit()

    cursor.close()
    conn.close()

    return f"Reserva/Itinerario {folio} actualizado correctamente."


# ============================================================================
# Cancelación de reservaciones
# ============================================================================

def cancelar_reserva(folio, tipo=None, nombre=None):
    """
    Gestiona cancelaciones de reservaciones e itinerarios.

    Casos soportados:
    - Cancelación completa de reservación.
    - Eliminación por tipo.
    - Eliminación por nombre.
    - Eliminación específica por tipo y nombre.

    Parameters
    ----------
    folio : str
        Identificador de la reservación.

    tipo : str, optional
        Tipo de elemento a cancelar.

    nombre : str, optional
        Nombre del elemento a cancelar.

    Returns
    -------
    str
        Resultado de la operación.
    """

    if tipo in ["NONE", "", "null", None]:
        tipo = None
    else:
        tipo = tipo.lower()

    if nombre in ["NONE", "", "null", None]:
        nombre = None

    conn = conectar_mysql()
    cursor = conn.cursor()

    # ------------------------------------------------------------------------
    # Cancelación completa
    # ------------------------------------------------------------------------

    if not tipo and not nombre:

        query = """
            UPDATE reservas
            SET estado = %s
            WHERE folio = %s
        """

        valores = ("Cancelado", folio)

    # ------------------------------------------------------------------------
    # Cancelación por tipo
    # ------------------------------------------------------------------------

    elif tipo and not nombre:

        query = """
            DELETE FROM itinerario
            WHERE folio = %s
            AND tipo = %s
        """

        valores = (folio, tipo)

    # ------------------------------------------------------------------------
    # Cancelación por nombre
    # ------------------------------------------------------------------------

    elif nombre and not tipo:

        query = """
            DELETE FROM itinerario
            WHERE folio = %s
            AND nombre LIKE %s
        """

        valores = (folio, f"%{nombre}%")

    # ------------------------------------------------------------------------
    # Cancelación específica
    # ------------------------------------------------------------------------

    else:

        query = """
            DELETE FROM itinerario
            WHERE folio = %s
            AND tipo = %s
            AND nombre LIKE %s
        """

        valores = (folio, tipo, f"%{nombre}%")

    cursor.execute(query, valores)
    conn.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conn.close()

    if filas_afectadas == 0:
        return (
            "No se encontró ninguna reserva "
            "con los criterios proporcionados."
        )

    return f"{filas_afectadas} registro(s) afectados correctamente."


# ============================================================================
# Consulta de autobuses
# ============================================================================

def consultar_bus(origen, destino, fecha):
    """
    Consulta salidas de autobuses disponibles.

    Parameters
    ----------
    origen : str
        Ciudad o terminal de origen.

    destino : str
        Ciudad o terminal de destino.

    fecha : str
        Fecha de salida.

    Returns
    -------
    list
        Resultados encontrados.
    """

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

        cursor.execute(
            query,
            (f"%{origen}%", f"%{destino}%", fecha)
        )

        resultados = cursor.fetchall()

    finally:

        cursor.close()
        conn.close()

    return resultados


# ============================================================================
# Consulta de vuelos
# ============================================================================

def buscar_vuelo(origen, destino, fecha):
    """
    Consulta vuelos disponibles entre aeropuertos.

    Parameters
    ----------
    origen : str
        Código IATA de origen.

    destino : str
        Código IATA de destino.

    fecha : str
        Fecha de salida.

    Returns
    -------
    list
        Resultados encontrados.
    """

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


# ============================================================================
# Consulta de itinerarios por folio
# ============================================================================

def consultar_folio(folio):
    """
    Obtiene el itinerario asociado a un folio de reservación.

    Parameters
    ----------
    folio : str
        Identificador único de la reservación.

    Returns
    -------
    dict
        Información estructurada del itinerario.
    """

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



