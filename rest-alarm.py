from microbit import *
import music

start = 0
last_minus = 0
last_second = 0
silent_mode = False

TIMEOUT_MINUTES = 20

run_image = Image("00000:"
                  "05050:"
                  "00000:"
                  "00000:"
                  "00000")

while True:
    if pin_logo.is_touched():
        silent_mode = True
        start = running_time()
        display.show(Image.SMILE)
        sleep(1000)
    elif button_a.was_pressed():
        silent_mode = False
        start = running_time()
        display.show(Image.SMILE)
        sleep(1000)
    elif button_b.was_pressed():
        start = 0
        display.clear()
        sleep(1000)

    if start > 0:
        time = running_time() - start
        current_second = int(time / 1000)
        current_minus = int(time / 1000 / 60)

        if current_minus == TIMEOUT_MINUTES:
            display.show(Image.HEART)
            music.play(music.CHASE)
            start = 0
        else:
            if last_minus != current_minus:
                print("current_minus=")
                print(current_minus)
                display.show(current_minus)
                last_minus = current_minus
                if not silent_mode:
                    music.pitch(440, 300)
                sleep(1000)
            else:
                if last_second != current_second:
                    print("current_second=")
                    print(current_second)
                    last_second = current_second

                    display.show(run_image)
                    sleep(300)
                    display.clear()
                    sleep(700)
