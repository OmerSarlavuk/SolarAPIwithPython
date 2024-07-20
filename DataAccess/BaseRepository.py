import pymssql
import json
from Utils import Messages
from Utils.EncodedDataAlgorithms import EncodedDataAlgorithms

#Docker Container _ SQL Server Information 
with open('appsettings.json', 'r') as f:
    settings = json.load(f)

algo = EncodedDataAlgorithms()
key  = settings['encoded_data_algorithms_key']['key']

server = algo.decrypt_text(settings['database']['server'], key)
port = algo.decrypt_text(settings['database']['port'], key)
database = algo.decrypt_text(settings['database']['name'], key)
username = algo.decrypt_text(settings['database']['username'], key)
password = algo.decrypt_text(settings['database']['password'], key)

messages = Messages


#Bağlantı var mı yok mu tek bu fonksiyon ile kontrol edilebilir. mainde de çağrılabilir tek başına.
def try_connection():
    try:
        conn = pymssql.connect(server=server, user=username, password=password, database=database, port=port)
        return conn
    except Exception as e:
        return None


#sorgular ile herhangi bir tabloya ait veriler okunabilir.
def read_data(query: str):

    conn = try_connection()

    if conn:

        cursor = conn.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        conn.close()

        size = len(rows)

        if size >= 1:
            return rows, messages.success_data
        else :
            return None, messages.database_table_exception

    else :
        return None, messages.data_base_exception


#Buradda yeni kayıt işlemi gerçekleşiyor veri tabanına
def create_data(query: str):

    conn = try_connection()

    if conn:
        
        cursor = conn.cursor()
        cursor.execute(query)
    
        conn.commit()
        conn.close()

        return True, messages.create_data_success
    else:
        return False, messages.data_base_exception


#Veri tabanındaki ilgili tablodaki ilgili satırı girilen id değerine göre günceller.
def update_data(query):

    conn = try_connection()

    if conn:

        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()

        return True, messages.update_data_success
    else:
        return False, messages.data_base_exception

#Veri tabanında ilgili tablodaki ilgili satırı siler verilen id değerine göre
def delete_data(query: str):

    conn = try_connection()

    if conn:

        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()

        return True, messages.delete_data_success
    else:
        return False, messages.data_base_exception
