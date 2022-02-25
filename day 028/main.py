import math
from tkinter import *

INITIAL_REPS = 4
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
round = 0
timer = None
marks=""

# -------------------------------------------TIMER RESET--------------------------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global round
    round=0
    canvas.itemconfig(text_timer, text="00:00")
    timer_label.config(text="Timer Stopped", font=(FONT_NAME, 20, "bold"), fg=RED)
    check_label.config(text="")
# -------------------------------------------COUNTDOWN MECHANISH------------------------------------------- #

def start_timer():
    global round
    round += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if round == 1 or round == 3 or round == 5 or round == 7:
        timer_label.config(text="Work",font=(FONT_NAME, 20, "bold"), fg=GREEN)
        count_down(work_sec)
    elif round == 2 or round == 4 or round == 6:
        timer_label.config(text="Short Break", font=(FONT_NAME, 20, "bold"), fg=PINK)
        count_down(short_break_sec)
    elif round == 8:
        timer_label.config(text="Long Break", font=(FONT_NAME, 20, "bold"), fg=RED)
        count_down(long_break_sec)
    else:
        pass


# -------------------------------------------COUNTDOWN MECHANISH------------------------------------------- #

def count_down(count):
    minute = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(text_timer, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks=""
        work_done = math.floor(round/2)
        for i in range(work_done):
            marks+="✓"
        check_label.config(text = marks)



# --------------------------------------------------------------UI Setup----------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
text_timer = canvas.create_text(100, 128, text="00:00", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 14), fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=4)

start_button = Button(text="Start", highlightthickness=0, border=5, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, border=5, command = reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
