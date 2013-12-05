import wiringpi2 as w
import time as t
import urllib.request as u
import json
import dev_animation as dev

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

##################################

def send_one_bit(value, with_delay = True):
    w.digitalWrite(DATA, value)
    #if with_delay:
    #    t.sleep(0.5)
    w.digitalWrite(CLOCK, HIGH)
    w.digitalWrite(CLOCK, LOW)

def display():
    w.digitalWrite(LATCH, HIGH)
    w.digitalWrite(LATCH, LOW)

def clear(amount):
    for x in range(0, amount):
        send_one_bit(0, False)

def download_contents(url):
     return u.urlopen(url).read()

def play_dev_animation:
    while True:
        t.sleep(0.25)
        for f in dev.FRAMES:
            # Load registers with diod states
            for diod_state in reversed(f):
                send_one_bit( diod_state )
            # Discharge regsisters to light LEDs
            display()
            # Sleep to make current frame visable for a while
            t.sleep(0.1)
            #t.sleep(frame_duration * f['repetition_count'])
        t.sleep(0.25)

##################################

clear(40)
display()

play_dev_animation()

# Download JSON file with an animation
#contents = download_contents( "http://192.168.1.102/~plysiu/XmasPi-REST/index.php/animation/get.json" )
# Parse JSON to extract animation data
#animation = json.loads(contents.decode('utf8')) 

# Set one frame duration
#frame_duration = 1 / animation['fps']
# Get frames
#frames = animation['frames']

# # Play ">DEV" animation
# while True:
#     t.sleep(0.25)
#     for f in frames:
#         # Load registers with diod states
#         for diod_state in reversed(f):
#             send_one_bit( diod_state )
#         # Discharge regsisters to light LEDs
#         display()
#         # Sleep to make current frame visable for a while
#         t.sleep(0.1)
#         #t.sleep(frame_duration * f['repetition_count'])
#     t.sleep(0.25)
