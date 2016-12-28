import notify2
import datetime
import random
import time
import pygame
from os import path

def hey_notify(sleep_fact = 0, *args):
    n = notify2.Notification(*args)
    n.show()
    pygame.mixer.music.play()
    time.sleep(sleep_fact * mul_fact)


notify2.init('foo')
pygame.mixer.init()
pygame.mixer.music.load(path.abspath(path.dirname(__file__))+ "/monotone.mp3")
mul_fact = 60 * 60
hours = 0
things_to_do = {'Advanced algorithims and Datastructures': 1,
                'Research on new trends in AI': 1,
                'Mathematics is the foundation of science': 1,
                'CS graduation': 1,
                'Call your friend': 0.25
                }
while things_to_do:
    random_hour = random.choice([1, 2, 1.5, 2.5])
    hey_notify(random_hour, 'Get Back To Work!!!!')
    current_time = datetime.datetime.now()
    right_now_item = random.choice(list(things_to_do.keys()))
    hours = things_to_do[right_now_item]
    end_time = current_time + datetime.timedelta(hours=hours)
    hey_notify(hours, right_now_item, 'Do it till ' + end_time.strftime('%r'))
    del things_to_do[right_now_item]

hey_notify('Take breaks in between and work the shit until you die')
