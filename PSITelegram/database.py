import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",database="psi_telegram_db", user="postgres", password="password")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn
