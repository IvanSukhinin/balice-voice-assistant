from definitions import ROOT_DIR

bot = {
	'names': ['братан', 'балиса', 'алиcа'],
	'commands': {
		'weather': ['какая сейчас погода', 'подскажи погоду', 'что за окном'],
		'chat_gpt': 'чат бот',
		'terminate': ['заверши', 'стоп', 'хватит', 'прекрати', 'стоямба'],
		'help': ['справка', 'что ты умеешь', 'расскажи о себе']
	},
	'answers': {
		'unrecognized': ['я не умею такого', 'не понимаю, что ты хочешь', 'че? че? че?'],
		'help': 'Сейчас я умею делать все, что умеет чат гэпэтэ'
	},
	'command_map_accuracy': 80,
	'default_notification' : ROOT_DIR + '/assets/music/notification.mp3'
}

microphone = {
	'device': 0,
	'samplerate': 44100,
	'channels': 1,
	'blocksize': 4000,
}
