import skills
import playsound
from speech import silero_tts
from multiprocessing import Process
import random

class BotSkills():
	def __init__(self, default_notification, answers):
		# text to speach
		self.__default_notification = default_notification
		self.__answers = answers
		self.__stts = silero_tts.SileroTTS()
		# skills
		self.__w = skills.weather.Weather()
		self.__chat_gpt = skills.chat_gpt.ChatGPT()
		self.__process = Process()

	def playWelcomeSound(self):
		playsound.playsound(self.__default_notification, True)

	def terminate_process(self):
		if self.__process.is_alive():
			self.__process.terminate()

	def say_weather(self):
		data = self.__w.current_weather()
		result = self.__w.beautify_weather(data)
		text = result if result else 'Я не знаю. С а+пи погоды что-то не то...'
		self.__process = Process(target=self.__stts.tts, args=(text,))
		self.__process.start()

	def say_unrecognized_command(self):
		unrecognized_cmd_index = random.randint(0, len(self.__answers['unrecognized']) - 1)
		text = self.__answers['unrecognized'][unrecognized_cmd_index]
		self.__process = Process(target=self.__stts.tts, args=(text,))
		self.__process.start()
		self.__process.join()

	def say_chat_gpt(self, text):
		# TODO
		# text = text[6:]
		self.__process = Process(target=self.execute_command_chat_gpt, args=(text,))
		self.__process.start()

	def execute_command_chat_gpt(self, text):
		answer = self.__chat_gpt.generate_answer(text)
		self.__stts.tts(answer)

	def is_in_process(self):
		return self.__process.is_alive()

	def say_help(self):
		text = self.__answers['help']
		self.__process = Process(target=self.__stts.tts, args=(text,))
		self.__process.start()
		self.__process.join()
