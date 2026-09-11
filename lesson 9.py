import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150) 
timer_box = Rect(0, 0, 300, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

score = 0
time_left = 20
question_file_name = "questions.txt"
marquee_message = ""
is_game_over = False

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

questions = []
questions_count = 0
questions_index = 0

marquee_box.move_ip(0, 0)
question_box.move_ip(0, 0)
timer_box.move_ip(20, 100)
answer_box1.move_ip(700, 100)
answer_box2.move_ip(20, 270)
answer_box3.move_ip(370, 270)
answer_box4.move_ip(20, 450)
skip_box.move_ip(700, 270)

def draw ():
    global marquee_message

    screen.clear()
    screen.fill(color="black")

    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip, "navy green")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark green")

    marquee_message = "Welcome To The Quiz..."
    marquee_message += f"Q; {question_index} of {question_count}   

    screen.draw.textbox(marquee_message, marquee_box, color="white")

    screen.draw.textbox(
        str(time_left), timer_box,
        color="white", shadow=(0.5, 0.5),
        scolor="dim grey"
    )

    screen.draw.textbox("Skip", skip_box, color="black", angle=-90)

    screen.draw.textbox(
        questions[0].strip(), question_box,
    color="white", shadow=(0.5, 0.5),
    scolor="dim grey"
    )

    index = 1

    for answer_box in answer_boxes:
        screen.draw.teextbox(question[index].strip9(), answer_box, color="black")
        index += 1

    def update
        move_marquee()

    def move marquee():
    marquee_box.x -= 2

       if marquee_box.right < 0:
        marquee_box.left = WIDTH

    def read_question_file():

            