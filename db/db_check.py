import sqlite3
import codecs

from db_connection import create_connection

database = "word_database.db"
conn = create_connection(database)

if conn is not None:
	try:
		c = conn.cursor()
		c.execute('SELECT COUNT(*) FROM WORDS')
	except Error as e:
		print(e)

print(c.fetchone())

