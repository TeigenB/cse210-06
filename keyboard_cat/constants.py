from game.casting.color import Color
import random

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Keyboard Cat"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

#ARTIFACT ENTRY POINTS
UP = int(SCREEN_HEIGHT * 0.75)
MIDDLE = int(SCREEN_HEIGHT/2)
DOWN = int(SCREEN_HEIGHT * 0.25)

# FONT
FONT_FILE = "cse210-06/keyboard_cat/assets/fonts/font.ttf"
FONT_SMALL = 28
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "cse210-06/keyboard_cat/assets/sounds/boing.wav"
WELCOME_SOUND = "cse210-06/keyboard_cat/assets/sounds/start.wav"
OVER_SOUND = "cse210-06/keyboard_cat/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255, 200)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
IN_PLAY = 1
GAME_OVER = 2

# artifact
artifact_GROUP = "artifacts"
#picks a random number between 2 and 4
number = random.randrange(1, 5)
#calls that image to randomize the artifact appearance
artifact_IMAGE = (f"cse210-06/keyboard_cat/assets/images/{number}.png")
artifact_WIDTH = 15
artifact_HEIGHT = 15
artifact_VELOCITY = 3


# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5

# HUD
HUD_MARGIN = 15
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"


# cat
#this is the player picture at the bottom of the screen
cat_GROUP = "cat"
cat_IMAGES = "cse210-06/keyboard_cat/assets/images/1.png"
cat_WIDTH = 30
cat_HEIGHT = 30
cat_RATE = 4
cat_VELOCITY = 0

# word_window
word_window_GROUP = "word_window"
word_window_IMAGES = "cse210-06/keyboard_cat/assets/images/5.png"
word_window_WIDTH = 150
word_window_HEIGHT = 100
word_window_RATE = 4
word_window_VELOCITY = 0

# DIALOG
DIALOG_GROUP = "dialogs"
INSTRUCTIONS = "Welcome to Keyboard Cat!\n\
    Type the words as they come across the screen.\n\
    Press Enter to submit your word. \n\
    You will gain a point if it is correct and the word will disappear.\n\
    If you fail to type the word before it reaches the edge of the screen, you lose a life.\n\
    Good luck!\n\
        \n\nPress Enter to Start"

WAS_GOOD_GAME = "Game Over!"

print("constants")