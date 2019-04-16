import psycopg2
import database, psi, time

if __name__ == '__main__':
    while True:
        psi.getPSI()
        time.sleep(3600)
