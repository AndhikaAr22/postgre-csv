import psycopg2
import json


def param_config(config):
    with open("config.json","rb") as file:
        conf = json.load(file)

        try:
            conf = conf[config]
            return conf
        except:
            print("check config")
            
            
def con_postgres(conf):
    while True:
        try:
            conn = psycopg2.connect(
                host = conf["host"],
                user = conf["user"],
                password = conf["password"],
                database = conf["database"],
                port = conf["port"])
            break
        except:
            print("config wrong")
            #time.sleep(1)
    return conn
