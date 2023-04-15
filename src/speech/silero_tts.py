import torch
import sounddevice as sd
from speech.text_formatter import TextFormatter

class SileroTTS:
	def __init__(self, language='ru', model_id='v3_1_ru', device='cpu', samplerate=48000, speaker='baya'):
		# speakers - baya, kseniya, xenia
		self.__model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
		                                     model='silero_tts',
		                                     language=language,
		                                     speaker=model_id)
		device = torch.device(device)
		self.__model.to(device)
		self.__samplerate = samplerate
		self.__speaker = speaker
		self.__text_formatter = TextFormatter()

	def tts(self, text):
		text = self.__text_formatter.format_text(text)
		put_accent = True
		put_yo = True
		audio = self.__model.apply_tts(text=text,
		                        speaker=self.__speaker,
		                        sample_rate=self.__samplerate,
		                        put_accent=put_accent,
		                        put_yo=put_yo)
		self.__speak(audio)

	def __speak(self, audio):
		sd.play(audio, self.__samplerate, blocking=True)
		sd.stop()
