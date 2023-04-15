from vosk import Model, KaldiRecognizer
import json

class VoskSTT():
    def __init__(self, model_folder, samplerate):
        model = Model(model_folder)
        self.__recognizer = KaldiRecognizer(model, samplerate)

    def stt(self, data):
        if self.__recognizer.AcceptWaveform(data):
            return json.loads(self.__recognizer.Result())['text']
