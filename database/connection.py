"""
Capa de acceso a datos. Toda la lógica SQL vive aquí, aislada del resto
de la aplicación (rutas y servicios no conocen detalles de PostgreSQL).
"""
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

from config import Config


def get_connection():
    """Abre una nueva conexión a PostgreSQL usando DATABASE_URL."""
    return psycopg2.connect(Config.DATABASE_URL, cursor_factory=RealDictCursor)


def init_db():
    """Crea la tabla de mediciones si todavía no existe."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS mediciones (
            id SERIAL PRIMARY KEY,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            edad INTEGER NOT NULL,
            sexo TEXT NOT NULL,
            imc REAL NOT NULL,
            categoria TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()


def save_measurement(peso, altura, edad, sexo, imc, categoria):
    """Guarda una nueva medición en la base de datos."""
    conn = get_connection()
    cur = conn.cursor()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M')
    cur.execute(
        '''INSERT INTO mediciones (peso, altura, edad, sexo, imc, categoria, fecha)
           VALUES (%s, %s, %s, %s, %s, %s, %s)''',
        (peso, altura, edad, sexo, imc, categoria, fecha)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_all_measurements(limit=50):
    """Devuelve las últimas `limit` mediciones, más recientes primero."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM mediciones ORDER BY id DESC LIMIT %s', (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]


def get_stats():
    """Calcula estadísticas agregadas: total, promedio, min, max y distribución."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT
            COUNT(*) as total,
            ROUND(AVG(imc)::numeric, 2) as promedio_imc,
            ROUND(MIN(imc)::numeric, 2) as min_imc,
            ROUND(MAX(imc)::numeric, 2) as max_imc
        FROM mediciones
    ''')
    row = cur.fetchone()

    cur.execute('''
        SELECT categoria, COUNT(*) as cantidad
        FROM mediciones
        GROUP BY categoria
    ''')
    categorias = cur.fetchall()

    cur.close()
    conn.close()

    stats = dict(row) if row else {}
    stats['categorias'] = [dict(c) for c in categorias]
    return stats


def delete_all_measurements():
    """Borra todo el historial. Útil para pruebas o reiniciar el demo."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM mediciones')
    conn.commit()
    cur.close()
    conn.close()
