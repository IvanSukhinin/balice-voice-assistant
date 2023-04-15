import config
from bot.bot import Bot
from definitions import ROOT_DIR

model_folder = ROOT_DIR + '/models/vosk-model-small-ru-0.22'
bot = Bot(config.microphone, config.bot, model_folder)
bot.run()
