import sqlite3
from datetime import datetime

DB_PATH = 'imc.db'

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# database.py

def init_db():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS mediciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    conn.close()

def save_measurement(peso, altura, edad, sexo, imc, categoria):
    conn = get_connection()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M')
    conn.execute(
        '''INSERT INTO mediciones 
           (peso, altura, edad, sexo, imc, categoria, fecha) 
           VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (peso, altura, edad, sexo, imc, categoria, fecha)
    )
    conn.commit()
    conn.close()

def get_all_measurements():
    conn = get_connection()
    rows = conn.execute('SELECT * FROM mediciones ORDER BY id DESC LIMIT 50').fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_stats():
    conn = get_connection()
    row = conn.execute('''
        SELECT 
            COUNT(*) as total,
            ROUND(AVG(imc), 2) as promedio_imc,
            ROUND(MIN(imc), 2) as min_imc,
            ROUND(MAX(imc), 2) as max_imc
        FROM mediciones
    ''').fetchone()

    categorias = conn.execute('''
        SELECT categoria, COUNT(*) as cantidad
        FROM mediciones
        GROUP BY categoria
    ''').fetchall()

    conn.close()

    stats = dict(row) if row else {}
    stats['categorias'] = [dict(c) for c in categorias]
    return stats
