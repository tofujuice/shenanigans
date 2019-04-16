from datetime import datetime
import requests, json, psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",database="psi_telegram_db", user="postgres", password="password")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

def storePSI(response):
    psi_24 = response['items'][0]['readings']['psi_twenty_four_hourly']
    north = int(psi_24['north'])
    south = int(psi_24['south'])
    east = int(psi_24['east'])
    west =  int(psi_24['west'])
    central = int(psi_24['central'])
    update_timestamp = response['items'][0]['update_timestamp']
    update_timestamp = update_timestamp[0:-6]
    update_timestamp  = datetime.strptime(update_timestamp, '%Y-%m-%dT%H:%M:%S')
    status = str(response['api_info']['status'])
    
    sql = "INSERT INTO psi_readings (north24, south24, east24, west24, central24, status, lastupdated) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    data = (north,south,east,west,central,status,update_timestamp)

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM psi_readings;")
        row = cur.fetchone()
        old_status = row[5]

        if old_status != status:
            initiatePanic()

        cur.execute('DELETE FROM psi_readings;', (None,))
        cur.execute(sql,data)
        conn.commit()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def storeUser(userid,region):
    sql = "INSERT INTO tele_subs (id,region) VALUES(%s,%s)"
    data = (userid,region)
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def removeUser(userid):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('DELETE FROM tele_subs where id= %s;', (userid,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# def initiatePanic():
    