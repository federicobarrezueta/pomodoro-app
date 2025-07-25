from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark_text =""

CHECKMARK ="✓"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    # 2nd/4th/6th -> short_break_sec
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)

    #8th rep -> long_break_sec
    elif reps % 2 == 0:
        timer_label.config(text="Break",fg=PINK)
        count_down(short_break_sec)

    # 1st/3rd/5th/7th rep -> work_sec
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global checkmark_text
    #245 / 60 - 4 minutes
    #245 % 60 - x seconds

    count_min = math.floor(count/60)
    count_sec = count%60

    #Using dynamic typing to
    if count_sec == 0:
        count_sec = "00"
    elif 10 > count_sec > 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(10, count_down, count - 1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady=50, bg=YELLOW)



#Canvas Widget
canvas = Canvas(width=200,height=224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#Labels
#fg = GREEN
#Timer
timer_label = Label()
timer_label.config(text="Timer",font=(FONT_NAME,50),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1,row=0)

#Checkmark
checkmarks = Label(text=checkmark_text + f"{reps}",padx=10,pady=10)
checkmarks.config(font=(FONT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)
checkmarks.grid(column=1,row=3)


#Buttons
#Start
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)


#Reset
reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2)



window.mainloop()