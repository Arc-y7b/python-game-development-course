import pgzrun
WIDTH = 640
HEIGHT = 640
CELL_SIZE = 80
levels = [
    # ---------------- LEVEL 1 ----------------
    [
        [0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 2],
    ],
    # ---------------- LEVEL 2 ----------------
    [
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 2],
    ],
    # ---------------- LEVEL 3 ----------------
    [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 0, 2],
    ],
]

current_level = 0
maze = levels[current_level]

player_row = 0
player_col = 0
game_won = False

player = Actor("bee")

def draw():
    screen.fill((30, 30, 40))

    for i in range(8):
        for j in range(8):
            x = j * CELL_SIZE
            y = i * CELL_SIZE

            rect = Rect((x, y),(CELL_SIZE, CELL_SIZE))
            if maze[i][j] == 1:
                screen.draw.filled_rect(rect, (0, 150, 140))
            else:
                screen.draw.filled_rect(rect,(255, 248, 220))

            screen.draw.rect(rect, (200, 200, 200))

            if maze[i][j] == 2:
                screen.draw.filled_rect(rect, (255, 215, 0))
                screen.draw.text(
                    "GOAL",
                     center=(x + 40, y + 40),
                     fontsize=24,
                     color="black",
                )

    screen.draw.text(
        "LEVEL" + str(current_level + 1),
        topleft=(10, 10),
        fontsize=35,
        color="white",

    player.pos = (
        player_col * CELL_SIZE + CELL_SIZE //2,
        player_row * CELL_SIZE + CELL_SIZE //2,
)

player.draw()

if game_won:
    screen.draw.text(
        "YOU WON THE GAME!!!"
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=50,
        color="lime",

    )
if game_won:
   screen.draw.text(
       "YOU WON THE GAME!!!"
       center=(WIDTH // 2, HEIGHT // 2)
       fontsize=50,
       color="lime"
 )    

 def on_key_down(key):
 global player_row
 global player_col
 global game_won
 global maze
 global current_level
             