import sqlite3

class C19_Database():
	def __init__(self):
		self.conn = None
		self.corsor = None

	def create_db(self, chat_id, last_action):
		print(1)
		self.conn = sqlite3.connect("country_list.db",  check_same_thread=False)

		self.cursor = self.conn.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS action (chat_id text, last_action text)")
		self.conn.commit()
		# except Exception as e:
		# 	file1 = open("Error_db.txt", "a")
		# 	file1.write(str(e)+"\n")
		# 	file1.close()
	def delete(self, chat_id):
		if self.conn == None:
			self.create_db(chat_id, "as")
		# block = [("1114074475", "asas", "cd")]

		# self.cursor.executemany("INSERT INTO act VALUES(?, ?, ?);", block)
		# self.conn.commit()

		self.cursor.execute("DELETE FROM action")
		self.conn.commit()
	def change_or_put(self, last_action, chat_id):
		if self.conn == None:
			self.create_db(chat_id, "as")
		try:
			self.cursor.execute("UPDATE action SET last_action = ? WHERE chat_id = ?;", (last_action, chat_id))
			self.conn.commit()
		except:
			self.cursor.execute("INSERT INTO action VALUES(?, ?);", (chat_id, last_action))
			self.conn.commit()

	def get_list(self, chat_id):
		if self.conn == None:
			self.create_db(chat_id, "as")

		self.cursor.execute("SELECT * FROM action WHERE chat_id=?", (chat_id, ))
		list1 = self.cursor.fetchall()

		if list1 == []:
			return list1
		else:
			return list1[0][1]

			