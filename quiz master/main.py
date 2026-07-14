import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50}, {50}'

import pgzrun

HEIGHT = 650
WIDTH = 870

#creating rectangles sizes
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
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4] #set in a list as same instructions are applied to every answer box
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

    #displaying question in question box
    screen.draw.textbox(question_row[0], question_box, color = 'black')

    #displaying answer options in answer boxes
    screen.draw.textbox(question_row[1], answer_box1, color = 'black')
    screen.draw.textbox(question_row[2], answer_box2, color = 'black')
    screen.draw.textbox(question_row[3], answer_box3, color = 'black')
    screen.draw.textbox(question_row[4], answer_box4, color = 'black')
        
def read_question_file():
    global questions_set, question_count

    #read question file
    q_file = open("questions.txt", "r") #opens questions file not reading. 
    ''' 
    opening q_file means opening the file from secondary memory to main memory RAM. 
    Each row in the file holds a different question, so instead of loading the whole file
    it loads question by question. 
    '''
    for row in q_file: 
        questions_set.append(row)
        question_count = question_count + 1
    q_file.close() #closes the file after use
    print(questions_set)

#fetching each question set one by one
def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions_set.pop(0).split(",")

def update_timer():
    global time_left
    if time_left > 0:
        time_left = time_left - 1
    else:
        game_over()

def game_over():
    global score, questions_set, question_row, time_left, is_game_over   
    message = f"Game over! Your score was {score} out of {question_count}"
    question_row = [message, "-", "-", "-", "-", 5] #message goes inside question box and the dashes fill the answer boxes
    time_left = 0
    is_game_over = True

def on_mouse_down(pos):
    index = 1
    for a_box in answer_boxes:
        if a_box.collidepoint(pos):
            if index == question_row[5]:
                correct_answer()
            else:
                game_over()
        index = index + 1
    if skip_box.collidepoint(pos):
        question_row = read_next_question()

read_question_file()
question_row = read_next_question()
clock.schedule_interval(update_timer, 1)



pgzrun.go()
