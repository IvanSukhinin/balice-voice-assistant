import openai
from api_tokens import CHAT_GPT_TOKEN

class ChatGPT():
	def __init__(self):
		self.__openai = openai
		self.__openai.api_key = CHAT_GPT_TOKEN

	def generate_answer(self, text):
		if not text:
			return ''

		print('generating')
		response = self.__openai.ChatCompletion.create(
		    model="gpt-3.5-turbo",
			messages=[
				{"role": "user", "content": text}
			],
			max_tokens=800
		)

		return response.choices[0].message.content
