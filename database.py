import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

def init_db():
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
    conn = get_connection()
    cur = conn.cursor()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M')
    cur.execute(
        'INSERT INTO mediciones (peso, altura, edad, sexo, imc, categoria, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        (peso, altura, edad, sexo, imc, categoria, fecha)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_all_measurements():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM mediciones ORDER BY id DESC LIMIT 50')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]

def get_stats():
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
