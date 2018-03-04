import config
from telegram.ext import Updater, Dispatcher
from telegram.ext import CommandHandler, MessageHandler, Filters
import callbacks as clb

def config_dispather(dispatcher):
	dispatcher.add_handler(CommandHandler("start", clb.start_callback))
	dispatcher.add_handler(MessageHandler(Filters.video, clb.video_callback))

def init_bot():
	updater = Updater(token=config.API_TOKEN)
	config_dispather(updater.dispatcher)
	return updater

def start_bot():
	updater = init_bot()
	updater.start_polling()
	return updater

def stop_bot(updater):
	updater.stop()

if __name__ == '__main__':
	updater = None
	try:
		updater = start_bot()
	except KeyboardInterrupt:
		stop_bot(updater)