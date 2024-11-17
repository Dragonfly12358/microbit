from microbit import *
import music

# Thời gian Pomodoro (đơn vị: giây)
WORK_TIME = 25 * 60  # 25 phút làm việc
BREAK_TIME = 5 * 60  # 5 phút nghỉ

# Biến trạng thái
is_running = False  # Trạng thái: Đang chạy hay không
is_working = True   # Trạng thái: Đang làm việc hay nghỉ
time_left = WORK_TIME  # Thời gian còn lại

def show_time(t):
    """Hiển thị thời gian còn lại trên LED."""
    minutes = t // 60
    seconds = t % 60
    display.scroll(str(minutes) + ":" + str(seconds))  # Hiển thị thời gian

def pomodoro_completed():
    """Xử lý khi hoàn thành một Pomodoro."""
    music.play(music.POWER_UP)
    if is_working:
        display.show(Image.HAPPY)  # Biểu tượng nghỉ
    else:
        display.show(Image.TRIANGLE)  # Biểu tượng làm việc
    sleep(2000)

while True:
    if is_running:
        if time_left > 0:
            sleep(1000)  # Đếm từng giây
            time_left -= 1
            if time_left % 10 == 0:  # Hiển thị thời gian mỗi 10 giây
                show_time(time_left)
        else:
            pomodoro_completed()
            # Đổi trạng thái
            is_working = not is_working
            time_left = WORK_TIME if is_working else BREAK_TIME
    else:
        display.show(Image.NO)  # Biểu tượng tạm dừng

    # Nút A: Bắt đầu hoặc tạm dừng
    if button_a.was_pressed():
        is_running = not is_running
        display.show(Image.HEART if is_running else Image.NO)

    # Nút B: Reset
    if button_b.was_pressed():
        is_running = False
        is_working = True
        time_left = WORK_TIME
        display.show(Image.NO)
