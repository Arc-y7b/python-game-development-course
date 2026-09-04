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
skip_pox = Rect(0, 0, 150, 330)

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
questions_box.move_ip(0, 0)
timer_box.move_ip(20, 100)
answer_box1.move_ip(700, 100)
answer_box2.move_ip(20, 270)
answer_box3.move_ip(370, 270)
answer_box4.move_ip(20, 450)
skip_box.move_ip(700, 270)
