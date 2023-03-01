import psycopg2

host = 'localhost'
user = 'postgres'
password = 'admin'
database = 'eCommerce'
port = 5432


def con_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = database,
                port = port)
            break
        except:
            print("config wrong")
            #time.sleep(1)
    return conn