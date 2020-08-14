import pygame
import random

pygame.init()

# Setting Caption
pygame.display.set_caption("Sorting Visualizer")
# ----------------------------Global Variabless-----------------------------------------------

# Mouse Positions
mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

# Font
font = pygame.font.Font('Fonts/Comic.ttf', 32)
options = pygame.font.Font('Fonts/Comic.ttf', 20)

# Display Size
display_width = 800
display_height = 600

# Manipulation Container Size
container_width = 400

# Header Container Size
h_container_height = 50
h_container_width = display_width + container_width

# Background
bg = pygame.image.load('BG/background.jpg')
h_bg = pygame.image.load('BG/h_bg.jpg')
c_bg = pygame.image.load('BG/c_bg.png')
bg1 = pygame.transform.scale(bg, (display_width + 5, display_height))
h_bg1 = pygame.transform.scale(h_bg, (h_container_width, h_container_height))
c_bg1 = pygame.transform.scale(c_bg, (container_width, h_container_height + display_height))

# Array Length
arr_length = 50
unsorted_arr = []
while len(unsorted_arr) < arr_length:
    element = random.randint(100, 500)
    if element not in unsorted_arr:
        unsorted_arr.append(element)

speed = 100

# Bar Positions
x = 5

# Button Position
button_arr = [(100, 10, 100, 30), (870, 10, 300, 30)]
size_arr = [(810, 100, 120, 30), (940, 100, 120, 30), (1070, 100, 120, 30), (890, 150, 120, 30), (1020, 150, 120, 30)]
speed_arr = [(810, 250, 120, 30), (940, 250, 120, 30), (1070, 250, 120, 30), (890, 300, 120, 30), (1020, 300, 120, 30)]

# Bar Width
gap = 5

# Screen
screen = pygame.display.set_mode((display_width + container_width, display_height))

# Colours
button_color = (0, 255, 255)
bar_color = (255, 0, 0)
bar_selected = [(0, 0, 255), (0, 225, 200), (204, 153, 255)]
screen_color = (0, 255, 0)
line_color = (0, 0, 0)
color_arr = []
button_hover = (204, 153, 255)

run = True
arr = False


# ----------------------------Global Variables-----------------------------------------------

# ----------------------------Text Functions-----------------------------------------------
# Display Heading
def display_heading(message):
    h_text = font.render(message, True, line_color)
    h_text_rect = h_text.get_rect()
    h_text_rect.center = (h_container_width // 2, h_container_height // 2)
    screen.blit(h_text, h_text_rect)


# draw text in button
def draw_buttons_text():
    screen.blit(options.render('SORT', True, line_color), (120, 10))
    screen.blit(options.render('GENERATE NEW ARRAY', True, line_color), (900, 10))


# Draw the options
def draw_options_text():
    screen.blit(font.render('SIZE', True, line_color), (955, 55))
    screen.blit(options.render('Huge-100', True, line_color), (830, 100))
    screen.blit(options.render('Large-80', True, line_color), (960, 100))
    screen.blit(options.render('Medium-40', True, line_color), (1077, 100))
    screen.blit(options.render('Small-20', True, line_color), (910, 150))
    screen.blit(options.render('X-Small-10', True, line_color), (1030, 150))

    screen.blit(font.render('SPEED', True, line_color), (955, 200))
    screen.blit(options.render('V-Slow-100', True, line_color), (815, 250))
    screen.blit(options.render('Slow-80', True, line_color), (960, 250))
    screen.blit(options.render('Normal-40', True, line_color), (1077, 250))
    screen.blit(options.render('Fast-10', True, line_color), (910, 300))
    screen.blit(options.render('V-Fast-1', True, line_color), (1040, 300))


# ----------------------------Text Functions-----------------------------------------------

# ----------------------------Draw Functions-----------------------------------------------

# Draw the Bars
def draw():
    global x
    display_heading('BUBBLE SORT VISUALIZATION')
    draw_option_button()
    draw_buttons()
    bar_width = round((((display_width - 1) - ((arr_length - 1) * gap)) / arr_length))
    x = 5
    if arr_length < 9:
        pygame.draw.rect(screen, line_color, (display_width + 10, h_container_height, 3, display_height))
    else:
        pygame.draw.rect(screen, line_color, (display_width + 5, h_container_height, 3, display_height))
    pygame.draw.rect(screen, line_color, (0, h_container_height, display_width + container_width, 3))
    for i in range(len(unsorted_arr)):
        color_arr.append(bar_color)
        pygame.draw.rect(screen, color_arr[i], (x, h_container_height + 3, bar_width, unsorted_arr[i]))
        x = x + bar_width + gap
    pygame.display.update()


# Draw the buttons
def draw_buttons():
    pygame.draw.rect(screen, button_color, button_arr[0], 2)
    pygame.draw.rect(screen, button_color, button_arr[1], 5)
    draw_buttons_text()


# Option Buttons
def draw_option_button():
    pygame.draw.rect(screen, button_color, size_arr[0], 5)
    pygame.draw.rect(screen, button_color, size_arr[1], 5)
    pygame.draw.rect(screen, button_color, size_arr[2], 5)
    pygame.draw.rect(screen, button_color, size_arr[3], 5)
    pygame.draw.rect(screen, button_color, size_arr[4], 5)

    pygame.draw.rect(screen, button_color, speed_arr[0], 5)
    pygame.draw.rect(screen, button_color, speed_arr[1], 5)
    pygame.draw.rect(screen, button_color, speed_arr[2], 5)
    pygame.draw.rect(screen, button_color, speed_arr[3], 5)
    pygame.draw.rect(screen, button_color, speed_arr[4], 5)
    draw_options_text()


# ----------------------------Draw Functions-----------------------------------------------

# ----------------------------Functions for manipulating and drawing-----------------------------------------------

# Generates a new list
def generate_new_list():
    global unsorted_arr, color_arr
    color_arr = [bar_color] * arr_length
    unsorted_arr = []
    while len(unsorted_arr) < arr_length:
        element = random.randint(100, 500)
        if element not in unsorted_arr:
            unsorted_arr.append(element)
    draw()


# Fill screen
def refill():
    screen.fill(screen_color)
    screen.blit(bg1, (0, h_container_height + 3))
    screen.blit(h_bg1, (0, 0))
    screen.blit(c_bg1, (display_width + 5, h_container_height + 3))


# Sort & Refresh button press
def button_press():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    for i in range(len(button_arr)):
        if button_arr[i][0] < mouse_x < button_arr[i][0] + button_arr[i][2] and \
                button_arr[i][1] < mouse_y < button_arr[i][1] + button_arr[i][3]:
            return i + 1
    return False


# Validating option button position
def size_pos_validate():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    for j in range(len(size_arr)):
        if size_arr[j][0] < mouse_x < size_arr[j][0] + size_arr[j][2] and \
                size_arr[j][1] < mouse_y < size_arr[j][1] + size_arr[j][3]:
            return j + 1
    return False


# Option button press
def size_button_press():
    global arr_length,arr
    if size_pos_validate() == 1:
        arr_length = 100
        arr = True
    elif size_pos_validate() == 2:
        arr_length = 80
        arr = True
    elif size_pos_validate() == 3:
        arr_length = 40
        arr = True
    elif size_pos_validate() == 4:
        arr_length = 20
        arr = True
    elif size_pos_validate() == 5:
        arr_length = 10
        arr = True
    return arr


# Validating option button position
def speed_pos_validate():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    for k in range(len(speed_arr)):
        if speed_arr[k][0] < mouse_x < speed_arr[k][0] + speed_arr[k][2] and \
                speed_arr[k][1] < mouse_y < speed_arr[k][1] + speed_arr[k][3]:
            return k + 6
    return False


# Option button press
def speed_button_press():
    global speed
    if speed_pos_validate() == 6:
        speed = 100
    elif speed_pos_validate() == 7:
        speed = 80
    elif speed_pos_validate() == 8:
        speed = 40
    elif speed_pos_validate() == 9:
        speed = 10
    elif speed_pos_validate() == 10:
        speed = 1


# ----------------------------Functions for manipulating and drawing-----------------------------------------------

# -------------------------------------Sort Functions----------------------------------------------

# Bubble Sort
def bubble_sort(unsorted_arr):
    for i in range(len(unsorted_arr)):
        for j in range(len(unsorted_arr) - 1):
            color_arr[j] = bar_selected[0]
            color_arr[j + 1] = bar_selected[0]
            pygame.time.delay(speed)
            if unsorted_arr[j] > unsorted_arr[j + 1]:
                unsorted_arr[j], unsorted_arr[j + 1] = unsorted_arr[j + 1], unsorted_arr[j]
                refill()
                draw()
            color_arr[j] = bar_color
            color_arr[j + 1] = bar_color
    for i in range(len(unsorted_arr)):
        color_arr[i] = bar_selected[2]
        refill()
        draw()
        pygame.time.delay(speed)


# -------------------------------------Sort Functions----------------------------------------------

# -------------------------------------Main----------------------------------------------

# While it is running
while run:
    start_sort = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if size_button_press():
                generate_new_list()
            speed_button_press()
            if button_press() == 1:
                bubble_sort(unsorted_arr)
            elif button_press() == 2:
                generate_new_list()

    refill()
    draw()
    arr = False
    pygame.display.update()

# -------------------------------------Main----------------------------------------------
