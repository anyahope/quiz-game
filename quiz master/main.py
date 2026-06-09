import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50}, {50}'

import pgzrun

HEIGHT = 650
WIDTH = 870

#creating rectangles
marquee_box = Rect(0, 0, 880, 80) #class
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

#positioning rectangles
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700, 270)

#creating game variables
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 10
marquee_message = ''
is_game_over = False
questions_set = []
question_count = 0
question_index = 0

def draw():
    global marquee_message

    screen.clear()
    screen.fill("green")

    #drawing rectangle on screen
    screen.draw.filled_rect(marquee_box, 'white')
    screen.draw.filled_rect(question_box, 'blue')
    screen.draw.filled_rect(timer_box, 'purple')
    for a_box in answer_boxes:
        screen.draw.filled_rect(a_box, 'white')
    screen.draw.filled_rect(skip_box, 'yellow')

    #display text in rectangle boxes
    marquee_message = f"Welcome to the quiz game! Q: {question_index} of {question_count}" 
    screen.draw.textbox(marquee_message, marquee_box, color = 'black')
    screen.draw.textbox('Skip', skip_box, color = 'black')
    screen.draw.textbox( str(time_left), timer_box, color = 'black')

pgzrun.go()