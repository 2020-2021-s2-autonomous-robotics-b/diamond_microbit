# Add your Python code here. E.g.
from microbit import *

# defining images

d1 = Image("00000:00000:00000:00000:00000")

d2 = Image("00800:00000:00000:00000:0000")

d3 = Image("08080:00800:00000:00000:00000")

d4 = Image("00800:08080:00800:00000:00000")

d5 = Image("00000:00800:08080:00800:00000")
           
d6 = Image("00000:00000:00800:08080:00800")
           
d7 = Image("00000:00000:00000:00800:08080")
           
d8 = Image("00000:00000:00000:00000:00800")
           
d9 = Image("00000:00000:00000:00000:00000")

# defining animations using the images 

all_diamonds_down = [d1, d2, d3, d4, d5, d6, d7, d8, d9]

all_diamonds_up = [d9, d8, d7, d6, d5, d4, d3, d2, d1] 

# making a while true loop for playing different animations based on pressing button A or B

while True:
    if button_a.is_pressed():
        display.show(all_diamonds_up, delay=200)
    elif button_b.is_pressed():
        display.show(all_diamonds_down, delay=200)
    else:
        display.show(d1)
        
# end of code
