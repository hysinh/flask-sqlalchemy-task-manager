import psycopg2
try:
    conn = psycopg2.connect("host=localhost dbname=postgres")
    conn.close()
    print("Connection successful")
except psycopg2.OperationalError as ex:
    print("Connection failed: {0}".format(ex))


import socket                                                                                                                                                              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('localhost',5432))
    s.close()
    print("Connection to socket 5432 successful")
except socket.error as ex:
    print("Connection failed with errno {0}: {1}".format(ex.errno, ex.strerror))            