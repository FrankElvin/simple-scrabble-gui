# -*- coding: utf-8 -*-
import sqlite3
import codecs

from db_connection import create_connection

database = "word_database.db"
conn = create_connection(database)

data_file = "slovar.txt"
infile = codecs.open(data_file, 'r', 'utf_8')

def insert_word(cursor, word):
	sql = 'INSERT INTO WORDS (word) VALUES (?)'
	cursor.execute(sql, word)
	return cursor.lastrowid

if conn is not None:
	try:
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS WORDS (word TEXT)")
		c.execute('DELETE FROM WORDS')
	except Error as e:
		print(e)

print("Inserting data")

for row in infile.readlines():
	insert_word(c, [row.rstrip()] )

conn.commit()
conn.close()
print("Done")

