from microbit import *
import music

# Thời gian Pomodoro (đơn vị: phút)
WORK_TIME = 2  # 25 phút làm việc
BREAK_TIME = 5   # 5 phút nghỉ

# Biến trạng thái
is_running = False  # Trạng thái: Đang chạy hay không
is_working = True   # Trạng thái: Đang làm việc hay nghỉ
time_left = WORK_TIME  # Thời gian còn lại (phút)

def show_leds(current_minute, total_minutes):
    """Hiển thị số phút còn lại qua đèn LED."""
    for y in range(5):
        for x in range(5):
            idx = y * 5 + x
            if idx < current_minute:
                display.set_pixel(x, y, 7)  # Sáng đèn
            elif idx < total_minutes:
                display.set_pixel(x, y, 3)  # Đèn mờ (chưa đến phút đó)
            else:
                display.set_pixel(x, y, 0)  # Tắt đèn

def blink_current_led(current_minute):
    """Nhấp nháy LED hiện tại 30 lần trong một phút."""
    if 1 <= current_minute <= 25:  # Chỉ xử lý nếu LED hợp lệ
        x = (current_minute - 1) % 5
        y = (current_minute - 1) // 5
        for _ in range(30):  # Nhấp nháy 30 lần
            display.set_pixel(x, y, 0)  # Tắt LED
            sleep(1000)  # 0.5 giây
            display.set_pixel(x, y, 9)  # Sáng lại LED
            sleep(1000)  # 0.5 giây

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
            current_minute = (WORK_TIME - time_left if is_working else BREAK_TIME - time_left) + 1
            show_leds(current_minute, WORK_TIME if is_working else BREAK_TIME)
            blink_current_led(current_minute)  # Nhấp nháy LED trong một phút
            time_left -= 1
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
