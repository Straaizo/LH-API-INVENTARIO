"""
Test de conexión DB — verifica que todas las tablas respondan con PK = id
Ejecutar: python test_db_pks.py
"""
import mysql.connector

DB = dict(
    host="127.0.0.1",
    port=3306,
    user="UserApp",
    password="&8y7c()tu9t/+,6`",
    database="lahornilla_base_normalizada",
    connection_timeout=10,
)

TABLAS = [
    "inventario_dim_categoria",
    "inventario_dim_destino",
    "inventario_dim_producto",
    "inventario_tipo_movimiento",
    "inventario_fact_movimientos",
    "inventario_dim_equipos",
    "inventario_dim_celulares",
    "inventario_dim_tablets",
    "inventario_dim_impresoras",
    "general_dim_usuario",
]

def run():
    try:
        conn = mysql.connector.connect(**DB)
        print("OK  Conexion establecida")
    except Exception as e:
        print(f"FAIL  No se pudo conectar: {e}")
        return

    cursor = conn.cursor()
    ok = 0
    fail = 0

    for tabla in TABLAS:
        pk = "id"
        # general_dim_usuario ya usaba PK = id (uuid)
        try:
            cursor.execute(f"SELECT {pk} FROM {tabla} LIMIT 1")
            cursor.fetchone()
            print(f"OK  {tabla}.{pk}")
            ok += 1
        except Exception as e:
            print(f"FAIL  {tabla}.{pk} -> {e}")
            fail += 1

    cursor.close()
    conn.close()
    print(f"\n{ok} OK / {fail} FAIL")

if __name__ == "__main__":
    run()
