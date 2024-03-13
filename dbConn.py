import psycopg2
from dbConfig import load_config

def queryDatabase(query):
    try:
        print(query)
        conn = psycopg2.connect(**load_config())
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)
