from microbit import *
import music
import speech

music.set_tempo(bpm=125)
notes = [
            "C4:3", "C4:2", "D4:5", "C4:5", "F4:5", "E4:10", 
            "C4:3", "C4:2", "D4:5", "C4:5", "G4:5", "F4:10", 
            "C4:3", "C4:2", "C5:5", "A4:5", "F4:3", "F4:2", "E4:5", "D4:10",
            "A#:3", "A#:2", "A4:5", "F4:5", "G4:5", "F4:9"
        ]

def shinning(count):
    if count % 3 == 0:
        display.show(Image(
            "00000:"
            "00900:"
            "09990:"
            "00900:"
            "00000"))
    elif count % 3 == 1: 
        display.show(Image(
            "00000:"
            "09990:"
            "09990:"
            "09990:"
            "00000"))
    else:
        display.show(Image(
            "90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909"))

def beating_heart(count):
    while count > 0:
        display.show(Image.HEART_SMALL)
        sleep(500)
        display.show(Image.HEART)
        sleep(500)
        count -= 1

def turn_right():
    pin13.write_digital(0)
    pin14.write_digital(0)
    pin15.write_digital(0)
    pin16.write_digital(1)
    
def turn_left():
    pin13.write_digital(0)
    pin14.write_digital(0)
    pin15.write_digital(1)
    pin16.write_digital(0)
    sleep(500)

def backwark():
    pin13.write_digital(0)
    pin14.write_digital(1)
    pin15.write_digital(0)
    pin16.write_digital(0)
    
def forward():
    pin13.write_digital(1)
    pin14.write_digital(0)
    pin15.write_digital(0)
    pin16.write_digital(0)

def stop():
    pin13.write_digital(0)
    pin14.write_digital(0)
    pin15.write_digital(0)
    pin16.write_digital(0)     
    
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        count = 0
        for note in notes:
            shinning(count)
            count += 1
            music.play([note])

        display.show(Image(
            "90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909"))
        
        turn_left()
        sleep(500)

        forward()
        sleep(3000)
        
        stop()
        sleep(5000)

        backwark()
        sleep(3000)
        
        turn_right()
        sleep(1050)

        stop()
        sleep(500)
        display.show(Image.HAPPY)
        
        forward()
        sleep(500)
        stop()
        
        speech.say('Happy birthday to you')
        beating_heart(3)

        display.show(Image.HAPPY)
        
