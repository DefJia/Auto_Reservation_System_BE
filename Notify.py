from wxpy import *
from configparser import ConfigParser
from General import General
from tkinter import Tk
from tkinter.messagebox import showinfo
import threading
import pyaudio
import wave

cfg = General.get_config()[0]

def continuous_output(text):
    print(text)

def final_output(text):
    from_ = cfg.get('Notify', 'Mail_from')
    pwd = cfg.get('Notify', 'Password')
    to = cfg.get('Notify', 'Mail_to')
    mail = Mail(from_, pwd, to)

def play_audio(filename):
    CHUNK = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

def play_audio_async(filename):
    do_therad = threading.Thread(target=play_audio, args=[filename])
    do_therad.start()

def show_messagebox(text):
    root = Tk()
    root.withdraw()
    showinfo(message = text)
    root.destroy()

def show_messagebox_async(text):
    do_therad = threading.Thread(target=show_messagebox, args=[text])
    do_therad.start()

class Robot:
    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('.config.ini', encoding='utf8')
        try:
            self.bot = Bot(cache_path=True, console_qr=2)
        except:
            print('此账号已被列入黑名单，无法登陆！')

    # @self.bot.register(my_friend)
    def reply_my_friend(msg):
        return 'received: {} ({})'.format(msg.text, msg.type)


class Mail:
    def __init__(self, from_, psw, to):
        pass


if __name__ == '__main__':
    a = Robot()
