from flask import Flask
from flask import request
from flask import jsonify
import time
import requests
import json
from pprint import pprint
import Logic_C19

import requests

class C19_Telegram():
	def __init__(self):
		self.app = Flask(__name__)

	def set_logic(self, logic_class):
		self.logic = logic_class

	def send_message(self, chat_id, button, text):
		token = "1355290045:AAFD96LRCoEbYXbwYgowpVCNnssE3M5ptnw"
		url = "https://api.telegram.org/bot" + token + "/sendMessage"

		if button == True:
			keyboard = {
				"keyboard": [
					["Кнопка #1"], 
					["Кнопка #2"], 
					["Exit"],
				],
				"resize_keyboard": True,
				"one_time_keyboard": True,

			}

			message = {
				"chat_id": chat_id,
				"text": text,
				"reply_markup": json.dumps(keyboard),
			}
		else:
			keyboard = {}

			message = {
				"chat_id": chat_id,
				"text": text,
			}

		response = requests.post(url, json = message)

		print(response.status_code)
		print(response.text)

	def start(self):
		@self.app.route("/", methods = ["POST"])
		def proceed_request():
			updates = request.get_json()
			chat_id = updates["message"]["chat"]["id"]
			text = updates["message"]["text"]
			print(text, chat_id)
			self.logic.main(text, chat_id)
			return jsonify(updates)
		self.app.run()



if __name__ == "__main__":
	logic = Logic_C19.C19_Logic()

	telegram = C19_Telegram()
	telegram.set_logic(logic)

	logic.set_telegram(telegram)

	telegram.start()