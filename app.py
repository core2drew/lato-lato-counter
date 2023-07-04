import wave
import sys

import pyaudio
import numpy

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = 20000

def listen():
    latoCounter = 0
    p = pyaudio.PyAudio();
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK,input_device_index=2)
    print('Listening to lato-lato noise...')
    while True:
        data = numpy.frombuffer(stream.read(CHUNK), dtype=numpy.int16)
        amplitude = numpy.max(numpy.abs(data))
        if amplitude > THRESHOLD:
            latoCounter += 1
            print(latoCounter)

    stream.close()
    p.terminate()

def get_available_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


if __name__ == "__main__":
    # get_available_devices()
    listen()