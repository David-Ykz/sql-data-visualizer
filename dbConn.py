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
            pass
#            print(row)
        cursor.close()
        conn.close()

        return rows
    except Exception as e:
        print("Error:", e)
        return ""
