import pgzrun

WIDTH = 600
HEIGHT = 400
def draw_cloud(x, y):
    screen.draw.filled_circle((x, y),18, (255, 255, 255))
    screen.draw.filled_circle((x + 22, y -10),22, (255, 255, 255))
    screen.draw.filled_circle((x +45, y), 18, (255, 255, 255))

def draw():
    screen.clear()
    screen.fill((135, 206, 235))    # Sky#

    # sun
    screen.draw.filled_circle((500, 80), 40, (255, 232, 20))

    # clouds 
    draw_cloud(80, 80) 
    draw_cloud(220, 60)
    draw_cloud(350,90)

    # Mountain 1 (filled using lines)
    for y in range(100, 300):
        x1 = 200 - (y - 100)
        x2 = 200 + (y - 100)
        screen.draw.line((x1, y), (x2, y), (64, 42, 18))

    # snow top 1
    for y in range(100, 150):
       x1 = 200 - (y - 100)
       x2 = 200 + (y - 100)
       screen.draw.line((x1, y), (x2, y), (255, 255, 255))

       
    # Mountain 2
    for y in range(120, 300):
        x1 = 400 - (y - 120)
        x2 = 400 + (y - 120)
        screen.draw.line((x1, y), (x2, y), (64, 42, 18))

    # snow top 2    
    for y in range(120, 170):
       x1 = 400 - (y - 120)
       x2 = 400 + (y - 120)
       screen.draw.line((x1, y), (x2, y), (255, 255, 255))
    # river (filled rectangle)
    river = Rect((270, 300), (60, 100))
    screen.draw.line((x1, y), (x2, y), (0, 150, 255))   
pgzrun.go()     