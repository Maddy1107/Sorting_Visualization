import pygame
import random

pygame.init()

# Setting Caption
pygame.display.set_caption("Sorting Visualizer")
# ----------------------------Global Variables-----------------------------------------------

# Mouse Positions
mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

# Font
font = pygame.font.Font('Fonts/Comic.ttf', 32)
options = pygame.font.Font('Fonts/Comic.ttf', 20)
value = pygame.font.Font('Fonts/Comic.ttf', 15)

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

# Default Sie,Speed,Algorithm
speed = 2
arr_length = 40

# Default Array
unsorted_arr = []
while len(unsorted_arr) < arr_length:
    element = random.randint(100, 500)
    if element not in unsorted_arr:
        unsorted_arr.append(element)

# Bar Positions
x = 5

# Button Position
button_pos = [
    (100, 10, 100, 30),
    (870, 10, 300, 30)
]

# Option Button Positions
option_pos = [
    # Size
    (810, 100, 120, 30),
    (940, 100, 120, 30),
    (1070, 100, 120, 30),
    (890, 150, 120, 30),
    (1020, 150, 120, 30),
    # Speed
    (810, 250, 120, 30),
    (940, 250, 120, 30),
    (1070, 250, 120, 30),
    (890, 300, 120, 30),
    (1020, 300, 120, 30),
    # Size Text
    (955, 55),
    (830, 100),
    (960, 100),
    (1077, 100),
    (910, 150),
    (1030, 150),
    # Speed Text
    (955, 200),
    (815, 250),
    (960, 250),
    (1077, 250),
    (910, 300),
    (1040, 300)

]

# Option Text Positions
option_texts = [
    # Size
    'SIZE', 'Huge-100', 'Large-80', 'Medium-40', 'Small-20', 'V-Small-10',
    # Speed
    'SPEED', 'V-Slow-100', 'Slow-80', 'Normal-40', 'Fast-10', 'V-Fast-1'

]

# Bar Width
gap = 5

# Screen
screen = pygame.display.set_mode((display_width + container_width, display_height))

# Colours
button_color = (0, 255, 255)
bar_selected = [(255, 0, 0), (0, 0, 255), (0, 225, 200), (204, 153, 255), (119, 221, 119)]
screen_color = (0, 255, 0)
line_color = (0, 0, 0)
color_arr = []
button_hover = (204, 153, 255)

run = True


# ----------------------------Global Variables-----------------------------------------------

# ----------------------------Draw Functions-----------------------------------------------

# Draw the Bars
def draw():
    global x
    draw_heading('BUBBLE SORT VISUALIZATION')
    draw_option_button()
    draw_buttons()
    values()
    bar_width = round((((display_width - 1) - ((arr_length - 1) * gap)) / arr_length))
    x = 5
    if arr_length < 9:
        pygame.draw.rect(screen, line_color, (display_width + 10, h_container_height, 3, display_height))
    else:
        pygame.draw.rect(screen, line_color, (display_width + 5, h_container_height, 3, display_height))
    pygame.draw.rect(screen, line_color, (0, h_container_height, display_width + container_width, 3))
    for i in range(len(unsorted_arr)):
        color_arr.append(bar_selected[0])
        pygame.draw.rect(screen, color_arr[i], (x, h_container_height + 3, bar_width, unsorted_arr[i]))
        x = x + bar_width + gap
    pygame.display.update()


# Display Heading
def draw_heading(message):
    h_text = font.render(message, True, line_color)
    h_text_rect = h_text.get_rect()
    h_text_rect.center = (h_container_width // 2, h_container_height // 2)
    screen.blit(h_text, h_text_rect)


# Draw the buttons
def draw_buttons():
    pygame.draw.rect(screen, button_color, button_pos[0], 2)
    pygame.draw.rect(screen, button_color, button_pos[1], 5)
    draw_buttons_text()


# Draw text in button
def draw_buttons_text():
    screen.blit(options.render('SORT', True, line_color), (120, 10))
    screen.blit(options.render('GENERATE NEW ARRAY', True, line_color), (900, 10))


# Option Buttons
def draw_option_button():
    for num in range(10):
        pygame.draw.rect(screen, button_color, option_pos[num], 5)
    draw_options_text()


# Draw the options
def draw_options_text():
    for num in range(12):
        screen.blit(options.render(option_texts[num], True, line_color), option_pos[num + 10])

#Timer
def draw_timer():

# ----------------------------Draw Functions-----------------------------------------------

# ----------------------------Functions for manipulating-----------------------------------------------

def values():
    screen.blit(value.render('Length:' + str(arr_length), True, line_color), (810, 500))
    if speed == 0:
        screen.blit(value.render('Speed:100', True, line_color), (890, 500))
    elif speed == 1:
        screen.blit(value.render('Speed:80', True, line_color), (890, 500))
    elif speed == 2:
        screen.blit(value.render('Speed:40', True, line_color), (890, 500))
    elif speed == 3:
        screen.blit(value.render('Speed:10', True, line_color), (890, 500))
    elif speed == 4:
        screen.blit(value.render('Speed:1', True, line_color), (890, 500))


# Delay
def delay():
    global speed
    if speed == 0:
        pygame.time.delay(100)
    if speed == 1:
        pygame.time.delay(80)
    if speed == 2:
        pygame.time.delay(40)
    if speed == 3:
        pygame.time.delay(10)
    if speed == 4:
        pygame.time.delay(1)


# Set new bar color
def set_color(pos, index):
    color_arr[pos] = bar_selected[index]


# Set the color of final sorted array
def set_final_color():
    for i in range(len(unsorted_arr)):
        set_color(i, 1)
        set_color(i, 3)
        refresh()
        pygame.time.delay(5)


# Refresh
def refresh():
    refill()
    draw()


# Fill screen
def refill():
    screen.fill(screen_color)
    screen.blit(bg1, (0, h_container_height + 3))
    screen.blit(h_bg1, (0, 0))
    screen.blit(c_bg1, (display_width + 5, h_container_height + 3))


# Generates a new list
def generate_new_list():
    global unsorted_arr, color_arr
    color_arr = [bar_selected[0]] * arr_length
    unsorted_arr = []
    while len(unsorted_arr) < arr_length:
        element = random.randint(100, 500)
        if element not in unsorted_arr:
            unsorted_arr.append(element)
    draw()


# Sort & Refresh button press
def button_press():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    for i in range(len(button_pos)):
        if button_pos[i][0] < mouse_x < button_pos[i][0] + button_pos[i][2] and \
                button_pos[i][1] < mouse_y < button_pos[i][1] + button_pos[i][3]:
            return i + 1
    return False


# Validating option button position
def option_pos_validate(index):
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    if option_pos[index][0] < mouse_x < option_pos[index][0] + option_pos[index][2] and \
            option_pos[index][1] < mouse_y < option_pos[index][1] + option_pos[index][3]:
        return True
    else:
        return False


# Option button press
def option_button_press():
    global arr_length, speed
    for num in range(5):
        if option_pos_validate(num):
            if num + 5 == 5:
                arr_length = 100
            elif num + 5 == 6:
                arr_length = 80
            elif num + 5 == 7:
                arr_length = 40
            elif num + 5 == 8:
                arr_length = 20
            elif num + 5 == 9:
                arr_length = 10
            generate_new_list()
            return num
    for num in range(5):
        if option_pos_validate(num + 5):
            speed = num


# ----------------------------Functions for manipulating and drawing-----------------------------------------------

# -------------------------------------Sort Functions----------------------------------------------

# Swap
def swap(pos1, pos2):
    unsorted_arr[pos1], unsorted_arr[pos2] = unsorted_arr[pos2], unsorted_arr[pos1]


# Bubble Sort
def bubble_sort():
    for i in range(len(unsorted_arr) - 1, -1, -1):
        for j in range(i):
            set_color(j, 1)
            set_color(j + 1, 1)
            delay()
            if unsorted_arr[j] > unsorted_arr[j + 1]:
                swap(j, j + 1)
                refresh()
            set_color(j, 0)
            set_color(j + 1, 0)
        set_color(i, 4)


# Selection Sort
def selection_sort():
    print(unsorted_arr)
    for i in range(len(unsorted_arr) - 1, -1, -1):
        iMin = 0
        for j in range(i + 1):
            set_color(j, 1)
            set_color(iMin, 2)
            delay()
            if unsorted_arr[j] > unsorted_arr[iMin]:
                set_color(iMin, 0)
                iMin = j
                set_color(iMin, 2)
            refresh()
            set_color(j, 0)
        set_color(iMin, 0)
        swap(i, iMin)
        set_color(i, 4)


# Insertion Sort
def insertion_sort():
    for i in range(1, len(unsorted_arr)):
        curr_el = unsorted_arr[i]
        pos = i
        set_color(i, 1)
        set_color(pos, 2)
        delay()
        while curr_el < unsorted_arr[pos - 1] and pos > 0:
            unsorted_arr[pos] = unsorted_arr[pos - 1]
            pos = pos - 1
            set_color(pos, 1)
            refresh()
            set_color(pos, 4)
        unsorted_arr[pos] = curr_el


# -------------------------------------Sort Functions----------------------------------------------

# -------------------------------------Main----------------------------------------------

# While it is running
while run:
    start_sort = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            option_button_press()
            if button_press() == 1:
                # bubble_sort()
                selection_sort()
                # insertion_sort()
                set_final_color()
            elif button_press() == 2:
                generate_new_list()

    refill()
    draw()
    pygame.display.update()

# -------------------------------------Main----------------------------------------------
