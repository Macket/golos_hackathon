import text_messages
import os
from backend import login, User
from config import username, password
from time import sleep

def start_callback_body(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=text_messages.start_message_initial.format(update.message.from_user.first_name))

def upload_file(bot, update):
	file_id = update.message.video.file_id
	text = update.message.caption
	filename = text.lower().replace(' ', '-') if text else 'hackathon-mipt'
	if file_id:
		try:
			pure_file = bot.get_file(file_id)
		except Exception as e:
			print(e)
			return False
		else:
			try:
				filepath = os.path.join(os.getcwd(), filename)
				pure_file.download(custom_path=filepath)
				try:
					#hardcode
					user_ = login(username, password)
					user_.add_video(filename, filepath)
					os.remove(filepath)
					bot.send_message(chat_id=update.message.chat_id, text=text_messages.success_upload_msg.format(update.message.from_user.first_name, filename))
					return True
				except Exception as e:
					print('Upload fail!')
					print(e)
					return False
			except ValueError as e:
				print(e)
				return False
	else:
		return False

def message_callback_body(bot, update):
	text = update.message.text
	if text:
		#Hardcode
		text = text.lower()
		print(text)
		filepath = os.path.join(os.getcwd(), text)
		user_ = login(username, password)
		user_.get_video(text, filepath)
		while not os.path.isfile(filepath):
			sleep(1)
		bot.send_message(chat_id=update.message.chat_id, text=text_messages.success_download_msg.format(update.message.from_user.first_name, text))
		bot.send_video(chat_id=update.message.chat_id, video=open(filepath, 'rb'))
		os.remove(filepath)
	else:
		bot.send_message(chat_id=update.message.chat_id, text=text_messages.download_error_msg.format(update.message.from_user.first_name))

def video_callback_body(bot, update):
	if not upload_file(bot, update):
		bot.send_message(chat_id=update.message.chat_id, text=text_messages.problem_msg.format(update.message.from_user.first_name))

