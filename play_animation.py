import wiringpi2 as w
import time as t
import urllib.request as u
import json
import Dev as dev
import random

# Setting up wiring pi
w.wiringPiSetup()

# Setting constants of pin modes
READ = 0
WRITE = 1

# Setting constants of pin states
HIGH = 1
LOW = 0

# Setting constants with pin values
DATA = 7
CLOCK = 0
LATCH = 3

# Setting pin modes
w.pinMode(DATA, WRITE)
w.pinMode(CLOCK, WRITE)
w.pinMode(LATCH, WRITE)

# Amount of LEDs in XmasPi
LED_COUNT = 40

# Web service URL
URL = "http://192.168.1.102/~plysiu/XmasPi-REST/index.php/animation/get.json"

##################################

def send_one_bit(value):
    w.digitalWrite(DATA, value)
    
    w.digitalWrite(CLOCK, HIGH)
    w.digitalWrite(CLOCK, LOW)

def display():
    w.digitalWrite(LATCH, HIGH)
    w.digitalWrite(LATCH, LOW)

def clear(amount):
    for x in range(0, amount):
        send_one_bit(0, False)
    display()

def download_contents(url):
     return u.urlopen(url).read()

def parse_json(content):
    animation = json.loads(contents.decode('utf8'))
    return animation

def play_animation(frames, fps=4):
    frame_duration = 1/fps
    for frame in frames:
        for state in reversed(frame):
            send_one_bit(state)
        display()
        t.sleep(frame_duration)

# def play_dev_animation():
#     t.sleep(0.25)
#     for f in dev.DEV_FRAMES:
#         # Load registers with diod states
#         for diod_state in reversed(f):
#             send_one_bit( diod_state )
#         # Discharge regsisters to light LEDs
#         display()
#         # Sleep to make current frame visable for a while
#         t.sleep(0.1)
#     #t.sleep(frame_duration * f['repetition_count'])
#     t.sleep(0.25)

def play_christmas():
    for state in range(0, 39):
        send_one_bit(random.choice([0, 1]))
        t.sleep(0.25)
        display()
    
##################################

while True:
	# play_animation(dev.DEV_FRAMES)
    # play_animation(dev.TEST_FRAMES)
	# play_christmas()