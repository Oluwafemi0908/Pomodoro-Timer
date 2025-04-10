from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# color codes were gotten  from color hunt website
# fg (foreground) is used to change font colour
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
time_diff = ''


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, time_diff, marks
    window.after_cancel(time_diff)
    reps = 0
    marks = ''
    title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, marks
    reps += 1
    print(marks)

    if reps % 2 == 1:
        seconds = convert_seconds(WORK_MIN)
        count_down(seconds)
        title.config(text='Work', fg=GREEN)
    elif reps == 8:
        seconds = convert_seconds(LONG_BREAK_MIN)
        count_down(seconds)
        reps = 0
        title.config(text='Long rest', fg=RED)
        marks += '✔'
    else:
        seconds = convert_seconds(SHORT_BREAK_MIN)
        count_down(seconds)
        title.config(text='Short rest', fg=PINK)
        marks += '✔'


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def convert_seconds(minute):
    count_to_seconds = minute * 60
    return count_to_seconds


def count_down(count):
    global time_diff
    minute = math.floor(count / 60)
    seconds = count % 60
    check_mark.config(text=marks)
    if len(str(seconds)) > 1:
        seconds_digit = f"{seconds}"
    else:
        seconds_digit = f"0{seconds}"
    time_digit = f"{minute}:{seconds_digit}"
    canvas.itemconfig(timer, text=time_digit)
    if count > 0:
        # Countdown after 1000 mSec
        time_diff = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=50, bg=YELLOW)
window.attributes('-topmost', True)

# Adding Image and Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
canvas.grid(row=1, column=1)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

# Adding Title
title = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 40, 'normal'), bg=YELLOW)
title.grid(row=0, column=1)

# Adding Buttons
start_button = Button(text='Start', command=start_timer, width=5, height=1, bg=GREEN, fg='white', font=('Calibri', 12,
                                                                                                        'bold'),
                      highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', command=reset_timer, width=5, height=1, bg=RED, fg='white', font=('Calibri', 12,
                                                                                                      'bold'),
                      highlightthickness=0)
reset_button.grid(row=2, column=2)

# Adding tick mark
check_mark = Label(text=marks, font=('Arial', 15, 'bold'), bg=YELLOW, fg=GREEN, pady=15)
check_mark.grid(row=2, column=1)

window.mainloop()
