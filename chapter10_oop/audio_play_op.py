#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("invalid file format")
        self.filename=filename

class Mp3File(AudioFile):
    ext="mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext="wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class WM(AudioFile):
    ext="wm"
    def play(self):
        print("playing {} as wm".format(self.filename))

if __name__=="__main__":
    mp3=Mp3File("sunning.mp3")
    print(mp3.ext)