from General import General
import wxpy
from configparser import ConfigParser
from tkinter import Tk
from tkinter.messagebox import showinfo
import threading
import pyaudio
import wave
import smtplib
from email.mime.text import MIMEText
from email.header import Header

cfg_main = General.get_config()[0]


class Output:
    @staticmethod
    def continuous_output(text):
        print(text)

    @staticmethod
    def final_output(text, type):
        type = cfg_main.get('Notify', 'Type') if type == '' else type
        if '1' in type:
            mail = Mail(text, text)
            mail.send()
        elif '4' in type:
            music = Music()
            music.play_audio_async()
        elif '5' in type:
            message_box = Massage_box(text)
            message_box.show_messagebox_async()


class Music:
    def __init__(self):
        self.filepath = cfg_main.get('Notify', 'Music_path')

    def play_audio(self):
        CHUNK = 1024
        wf = wave.open(self.filepath, 'rb')
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

    def play_audio_async(self):
        do_therad = threading.Thread(target=self.play_audio)
        do_therad.start()


class Massage_box:
    def __init__(self, text=''):
        self.text = text
        
    def show_messagebox(self):
        root = Tk()
        root.withdraw()
        showinfo(message = self.text)
        root.destroy()

    def show_messagebox_async(self):
        do_therad = threading.Thread(target=self.show_messagebox)
        do_therad.start()


class Wechat:
    def __init__(self):
        try:
            self.bot = wxpy.Bot(cache_path=True, console_qr=2)
        except:
            print('此账号已被列入黑名单，无法登陆！')

    # @self.bot.register(my_friend)
    # def reply_my_friend(self):
        # return 'received: {} ({})'.format(msg.text, msg.type)


class Mail:
    def __init__(self, subject, context):
        self.from_ = cfg_main.get('Notify', 'Sender')
        self.pwd = cfg_main.get('Notify', 'Password')
        self.to = cfg_main.get('Notify', 'Reciever').split(',')
        self.subject = subject
        self.context = context
    
    def send(self):
        message = MIMEText(self.context, 'plain', 'utf-8')
        message['From'] = self.from_
        message['To'] =  self.to[0]
        message['Subject'] = self.subject
        try:
            smtpObj = smtplib.SMTP()
            smtp_server = 'smtp.' + self.from_.split('@')[1]
            smtpObj.connect(smtp_server)
            smtpObj.login(self.from_, self.pwd)
            smtpObj.sendmail(self.from_, self.to, message.as_string())
            smtpObj.quit() 
            print('邮件发送成功！')
        except smtplib.SMTPException as e:
            print('邮件发送失败！',e) 
        
    
if __name__ == '__main__':
    a = Music()
    a.play_audio_async()
