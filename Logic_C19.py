from pprint import pprint
import DataBase_C19
import time
import requests
import json


class C19_Logic():
	def __init__(self):
		self.db = DataBase_C19.C19_Database()

	def set_telegram(self, telegram):
		self.answer = telegram
	def main(self, text, chat_id):
		list1 = self.db.get_list(chat_id)
		print(list1)
		print(2)
		self.check_text(text, list1, chat_id)
	def check_text(self, text, last_action, chat_id):
		if text == "/start":
			self.answer.send_message(chat_id, False,"Hello user!! I'm coronavirus bot which gives you information about your condition according to your statement and also number of people that was infected or died during pandemic.")
			self.answer.send_message(chat_id, False,"All commands: \n \
'stats' - gives you a number of infected and died people during pandemic in your or in another country. \n \
'info' - information about my bot and me \n \
'start examination' - start identifying your diagnosis )")
			self.db.change_or_put("/start", chat_id)
		elif text == "stats" or text == "Stats":
			self.answer.send_message(chat_id, False,"Please write the name of your country, example: 'Russian Federation', 'Japan'. If you want to stop write 'exit'")
			self.answer.send_message(chat_id, False,"Also you need to write the full name of country, example: 'UK'- No, 'United Kingdom' - Yes")
			self.answer.send_message(chat_id, False,"If you want to write 'Korea' please write 'Korea (South)'")
			self.db.change_or_put("stats", chat_id)
		elif text == "info" or text == "Info":
			self.answer.send_message(chat_id, False,"My coronavirus bot gives you information that I tell him, but I'm not doctor and I take this information from articles, so I think you can trust me or you can do all this by yourself ). My Instagram: @ismailzade18 ")
			self.answer.send_message(chat_id, False,"All commands: \n \
'stats' - gives you a number of infected and died people during pandemic in your or in another country. \n \
'info' - information about my bot and me \n \
'start examination' - start identifying your diagnosis )")
			self.db.change_or_put("info", chat_id)
		elif text == "start examination" or last_action == "exam":
			if text == "Exit":
				self.db.change_or_put("/start", chat_id)
				self.answer.send_message(chat_id, False,"All commands: \n \
'stats' - gives you a number of infected and died people during pandemic in your or in another country. \n \
'info' - information about my bot and me \n \
'start examination' - start identifying your diagnosis )")
			else:
				self.answer.send_message(chat_id, True,"Let's start examination: \n \
	\n \
	???")
			self.db.change_or_put("exam", chat_id)
		elif last_action == "/start":
			self.answer.send_message(chat_id, False,"Hello user!! I'm coronavirus bot which gives you information about your condition according to your statement and also number of people that was infected or died during pandemic.")
			self.answer.send_message(chat_id, False,"All commands: \n \
'stats' - gives you a number of infected and died people during pandemic in your or in another country. \n \
'info' - information about my bot and me \n \
'start examination' - start identifying your diagnosis )")
			self.db.change_or_put("/start", chat_id)
		else:
			if text == "exit" or text == "Exit":
				self.answer.send_message(chat_id, False,"All commands: \n \
'stats' - gives you a number of infected and died people during pandemic in your or in another country. \n \
'info' - information about my bot and me \n \
'start examination' - start identifying your diagnosis )")
				self.db.change_or_put("/start", chat_id)
			elif last_action == "stats":
				self.send_stats(chat_id, text)
				self.db.change_or_put("stats", chat_id)
			else:
				self.answer.send_message(chat_id, False,"No such command")
		# else:
		# 	self.answer.send_message(chat_id, False,"Sorry, but bot is not available now")

	# def get_and_put(self):
	# 	comm = "https://api.covid19api.com/countries"
	# 	get_countr = requests.get(comm)
	# 	data = json.loads(get_countr.text)
	# 	self.db.put_list(data)
	def get_data(self):
		get_stat = requests.get("https://api.covid19api.com/summary")
		data = json.loads(get_stat.text)

		return data

	def send_stats(self, chat_id, text):
		info = self.get_data()
		print(info)

		ok = False
		if info["Message"] == "Caching in progress":
			self.answer.send_message(chat_id, False,"Sorry, but bot is not available now")
		for i in range(len(info["Countries"])):
			if text == info["Countries"][i]["Country"]:
				ok =True
				self.answer.send_message(chat_id, False,"Confirmed: "+str(info["Countries"][i]["TotalConfirmed"])+", Deaths: "+str(info["Countries"][i]["TotalDeaths"])+", Recovered: "+str(info["Countries"][i]["TotalRecovered"]))
				break
		if ok == False:
			self.answer.send_message(chat_id, False,"There is no such country")

	def get_and_put(self):
		pass