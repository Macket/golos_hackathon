import text_messages
import os
from backend import login, User

def start_callback_body(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=text_messages.start_message_initial.format(update.message.from_user.first_name))

def upload_file(bot, update):
	file_id = update.message.video.file_id
	if file_id:
		try:
			pure_file = bot.get_file(file_id)
		except Exception as e:
			print(e)
			return False
		else:
			try:
				filepath = os.path.join(os.getcwd(), 'hackathon.mp4')
				pure_file.download(custom_path=filepath)
				try:
					#hardcode
					usename = 'poster'
					password = 'qwerty12345'
					user_ = login(usename, password)
					user_.add_video('VideoPotest', filepath)
					return True
				except Exception as e:
					print('Upload fail!')
					print(e)
					return False
				return True
			except ValueError as e:
				print(e)
				return False
	else:
		return False

def video_callback_body(bot, update):
	if upload_file(bot, update):
		bot.send_message(chat_id=update.message.chat_id, text=text_messages.upload_file.format(update.message.from_user.first_name))
	else:
		bot.send_message(chat_id=update.message.chat_id, text=text_messages.problem_msg.format(update.message.from_user.first_name))