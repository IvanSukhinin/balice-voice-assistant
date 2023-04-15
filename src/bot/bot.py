from speech.vosk_stt import VoskSTT
from bot.microphone_stream import MicrophoneStream
from bot.bot_command_mapping import BotCommandMapping

class Bot():
	def __init__(self, micro_config, bot_config, model_folder):
		self.bot_command_mapping = BotCommandMapping(bot_config)
		# speech recognition
		self.vstt = VoskSTT(model_folder, micro_config['samplerate'])
		# microphone stream
		self.microphone = MicrophoneStream(device=micro_config['device'], samplerate=micro_config['samplerate'], blocksize=micro_config['blocksize'], channels=micro_config['channels'])
		self.microphone_stream = self.microphone.open_stream()

	def run(self):
		with self.microphone_stream:
			while True:
				data = self.microphone.listen()
				if not data:
					continue
				text = self.vstt.stt(data)
				self.microphone_stream.stop()
				self.bot_command_mapping.map_command(text)
				self.microphone_stream.start()
