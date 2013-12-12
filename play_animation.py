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

# Set fps boost rate ( real fps = fps * boost )
BOOST_FPS = 100

# Web service URL
URL = "http://dev.uek.krakow.pl/~xmaspi/index.php/animation/get.json"

##################################

def send_one_bit(value):
    w.digitalWrite(DATA, value)
    #t.sleep(0.02)
    w.digitalWrite(CLOCK, HIGH)
    #t.sleep(0.02)
    w.digitalWrite(CLOCK, LOW)
    #t.sleep(0.02)

def display():
    w.digitalWrite(LATCH, HIGH)
    #t.sleep(0.02)
    w.digitalWrite(LATCH, LOW)
    #t.sleep(0.02)

def clear(amount):
    for x in range(0, amount):
        send_one_bit(0, False)
    display()

def download_contents(url):
     return u.urlopen(url).read()

def parse_json(contents):
    animation = json.loads(contents.decode('utf8'))
    return animation

def play_animation(frames, fps=8):

    # If error returned from REST service go with default animation
    if  'error' in frames:
        frames = dev.SPOLI_FRAMES
        
    frame_duration = 1 / fps / BOOST_FPS
    for frame in frames:
        for i in range(0, BOOST_FPS):
            for state in reversed(frame):
                send_one_bit(state)
            display()
            t.sleep(frame_duration)

def play_christmas():
    for state in range(0, 39):
        send_one_bit(random.choice([0, 1]))
        t.sleep(random.uniform(0.1, 0.5))
        display()

def play_test_moving_dot():
    for frame in range(0, 40):
        for dot in range(0, 40):
            if dot == frame:
                send_one_bit(1)
            else:
                send_one_bit(0)
        display()
        t.sleep(0.1)
    
####################parse_json##############

while True:
    #play_test_moving_dot()
    #play_animation(dev.DEV_FRAMES)
    #play_animation(dev.TEST_FRAMES, 4)
    #play_animation(dev.SPOLI_FRAMES)
    #play_animation(dev.HIGH_LOW_FRAMES)
    #play_christmas()

    if random.choice( [0, 1, 2, 3, 4] ):
        play_animation( parse_json( download_contents( URL ) ) )
    else:
        play_animation( dev.DEV_FRAMES )
        
        
    
