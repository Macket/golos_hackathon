from telegram.ext.dispatcher import run_async
import functions

@run_async
def start_callback(bot, update):
	functions.start_callback_body(bot, update)

@run_async
def video_callback(bot, update):
	functions.video_callback_body(bot, update)

@run_async
def message_callback(bot, update):
	functions.message_callback_body(bot, update)
