import psycopg2
from psycopg2 import pool

hostname = "152.1.26.116"
dbname = "team1"
dbuser = "team1"
dbpass = "Faido9ke"
dbport = "5432"
db = pool.SimpleConnectionPool(1, 10, host=hostname, database=dbname, user=dbuser, password = dbpass, port = dbport)

def querydb(query):
	conn = db.getconn()
	cur = conn.cursor()
	cur.execute(query)
	results = cur.fetchall()
	db.putconn(conn)
	return results



