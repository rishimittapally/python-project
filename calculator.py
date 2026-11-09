import pgzrun
import pygame
WIDTH = 650
HEIGHT = 950

# -------------------------
# Layout Settings
# -------------------------

BUTTON_W = 105
BUTTON_H = 110
PADDING = 25

# Colors

BG = (30, 30, 30)
BTN = (60, 60, 60)
BTN_HOVER = (90, 90, 90)

TEXT_COLOR = "green"
# Display area

display_value = ""
# -------------------------
# Button Definitions
# -------------------------

buttons = []
labels = [

    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

def create_buttons():
    y = 100
    for row in labels:
        x = PADDING
        for label in row:
            rect = Rect((x, y), (BUTTON_W, BUTTON_H))
            buttons.append({"rect": rect, "label": label})
            x += BUTTON_W + PADDING
        y += BUTTON_H + PADDING
create_buttons()

# -------------------------
# Drawing
# -------------------------

def draw():
    screen.fill(BG)
    # Draw display

    screen.draw.filled_rect(Rect(10, 20, 280, 60), (20, 20, 20))
    screen.draw.text(
        display_value,
        topleft=(20, 30),
        fontsize=40,
        color=TEXT_COLOR
    )

    # Draw buttons
    for btn in buttons:
        rect = btn["rect"]

        # Hover effect
        color = BTN_HOVER if rect.collidepoint(pygame.mouse.get_pos()) else BTN
        screen.draw.filled_rect(rect, color)

        # Button text
        screen.draw.text(
            btn["label"],
            center=rect.center,
            fontsize=32,
            color=TEXT_COLOR
        )

# -------------------------
# Handle Clicks
# -------------------------

def on_mouse_down(pos):
    global display_value
    for btn in buttons:
        if btn["rect"].collidepoint(pos):
            value = btn["label"]
            if value == "C":
                display_value = ""
            elif value == "=":
                try:
                    display_value = str(eval(display_value))
                except:
                    display_value = "Error"         
            else:
                display_value += value

pgzrun.go()