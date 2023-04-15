from fuzzywuzzy import process
from bot.bot_skills import BotSkills

class BotCommandMapping():
	def __init__(self, bot_config):
		self.__bot_skills = BotSkills(bot_config['default_notification'], bot_config['answers'])
		self.__is_gpt_calling = False
		self.__is_calling = False
		self.__is_in_process = False
		self.__bot_names = bot_config['names']
		self.__chat_gpt_names = bot_config['chat_gpt_names']
		self.__bot_commands = bot_config['commands']
		self.__command_accurancy = bot_config['command_map_accuracy']

	def __check_command(self, checked_cmd, cmd_list):
		return (process.extractOne(checked_cmd, cmd_list)[1] >= self.__command_accurancy)

	def map_command(self, cmd):
		""" bot command mapping """
		if not cmd:
			return False

		print(cmd)

		if self.__check_command(cmd, self.__bot_names) and not self.__is_calling:
			self.__is_calling = True
			self.__bot_skills.playWelcomeSound()
			return True
		elif self.__check_command(cmd[:len(max(self.__chat_gpt_names, key=len))], self.__chat_gpt_names) and not self.__is_gpt_calling:
			self.__is_gpt_calling = True
			self.__bot_skills.playWelcomeSound()
			return True

		if self.__is_gpt_calling:
			self.__is_gpt_calling = False
			self.__bot_skills.terminate_process()
			return self.__bot_skills.say_chat_gpt(cmd)

		if not self.__is_calling:
			return False

		self.__is_calling = False
		self.__is_in_process = self.__bot_skills.is_in_process()

		# kill process if need
		if self.__check_command(cmd, self.__bot_commands['terminate']):
			return self.__bot_skills.terminate_process()

		# if bot has an active process, just abort
		if self.__is_in_process:
			return False

		if self.__check_command(cmd, self.__bot_commands['weather']):
			return self.__bot_skills.say_weather()

		if self.__check_command(cmd, self.__bot_commands['help']):
			return self.__bot_skills.say_help()

		return self.__bot_skills.say_unrecognized_command()
