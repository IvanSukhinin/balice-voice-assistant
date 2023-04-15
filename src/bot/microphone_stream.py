import sys
import queue
import sounddevice as sd

class MicrophoneStream():
    def __init__(self, device, samplerate, blocksize, channels, dtype='int16'):
        self.__device = device
        self.__samplerate = samplerate
        self.__blocksize = blocksize
        self.__channels = channels
        self.__dtype = dtype
        self.__q = queue.Queue()

    def __q_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.__q.put(bytes(indata))

    def open_stream(self):
        return sd.RawInputStream(samplerate=self.__samplerate, blocksize=self.__blocksize, device=self.__device, dtype=self.__dtype,
                               channels=self.__channels, callback=self.__q_callback)

    def listen(self):
        return self.__q.get()
