import sqlite3

database = "word_database.db"
def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	
	return None
	

def check_word_in_db(cursor, word):
	sql = "SELECT 1 FROM WORDS WHERE WORD = '%s'" %word
	cursor.execute(sql)
	return cursor.fetchone()

class DbChecker:

	def __init__(self, database):
		self.conn = create_connection(database)
		self.cursor = self.conn.cursor()
	
	def checkWordInDb(self, word):
		sql = "SELECT 1 FROM WORDS WHERE WORD = '%s'" %word
		self.cursor.execute(sql)
		return self.cursor.fetchone()
	
if __name__ == '__main__':
	conn = create_connection(database)
	c = conn.cursor()

	if conn is not None:
		if check_word_in_db(c, u"АБАЖУР"):
			print("lol")
		if check_word_in_db(c, u"ЛОЛКЕК"):
			print("lol")
		conn.close()
	
