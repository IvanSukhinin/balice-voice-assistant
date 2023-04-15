from num2words import num2words
from transliterate import translit

class TextFormatter():
	def __init__(self, lang='ru'):
		self.__lang = lang

	def digits_to_words(self, s):
		l = len(s)
		format_string = ''
		i = 0
		while i < l:
			s_int = ''
			char = s[i]
			while '0' <= char <= '9':
				s_int += char
				i += 1
				if i < l:
					char = s[i]
				else:
					break
			if s_int != '':
				format_string += ' ' + num2words(s_int, lang=self.__lang) + ' '
			format_string += char
			i += 1
		return format_string

	def format_text(self, s):
		return self.digits_to_words(translit(s, self.__lang))
