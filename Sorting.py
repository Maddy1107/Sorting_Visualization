import pygame
import random
import time
import math

pygame.init()

# Setting Caption
pygame.display.set_caption("Sorting Visualizer")
# ----------------------------Global Variables-----------------------------------------------

# duration, start = 0, time.time()

# Mouse Positions
mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

# Font
font = pygame.font.Font('Fonts/Bold.ttf', 32)
options = pygame.font.Font('Fonts/Bold.ttf', 20)
options1 = pygame.font.Font('Fonts/Bold.ttf', 30)
value = pygame.font.Font('Fonts/Comic.ttf', 18)

# Display Size
display_width = 800
display_height = 600

# Manipulation Container Size
container_width = 408

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

# Default Size,Speed,Algorithm
speed = 2
arr_length = 40
algorithm = 0

# Text Input
user_element = ""

# Default Array
unsorted_arr = []
while len(unsorted_arr) < arr_length:
    element = random.randint(100, 500)
    if element not in unsorted_arr:
        unsorted_arr.append(element)

# Bar Positions
x = display_height

# Button Position
button_pos = [
    (1050, 370, 100, 50),
    (1015, 450, 160, 50)
]

# Option Button Positions
option_pos = [
    # Size
    (815, 80, 120, 30),
    (945, 80, 120, 30),
    (1075, 80, 120, 30),
    (815, 120, 120, 30),
    (945, 120, 120, 30),
    (1075, 120, 120, 30),
    # Speed
    (810, 250, 120, 30),
    (940, 250, 120, 30),
    (1070, 250, 120, 30),
    (890, 300, 120, 30),
    (1020, 300, 120, 30),
    # Algorithm
    (820, 390),
    (820, 420),
    (820, 450),
    (820, 480),
    (820, 510),
    (820, 540),
    # Size Text
    (800, 55),
    (830, 80),
    (970, 80),
    (1087, 80),
    (817, 120),
    (958, 120),
    (1083, 120),
    # Speed Text
    (800, 220),
    (815, 250),
    (960, 250),
    (1077, 250),
    (910, 300),
    (1040, 300),
    # Algorithm text
    (830, 345),
    (830, 375),
    (830, 405),
    (830, 435),
    (830, 465),
    (830, 495)

]

# Option Texts
option_texts = [
    # Size
    '------------------------SIZE-------------------------',
    'Huge-400', 'XL-100', 'Large-80', 'Medium-40', 'Small-20', 'V-Small-10',
    # Speed
    '---------------------- SPEED-------------------------',
    'V-Slow-100', 'Slow-80', 'Normal-40', 'Fast-10', 'V-Fast-1',
    # Algorithm
    'ALGORITHM:', 'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort'

]

# Bar Width
gap = 5

# Screen
screen = pygame.display.set_mode((display_width + container_width, display_height))

# Colours
button_color = (200, 100, 255)
bar_selected = [(36, 226, 31),  # Default Color
                (0, 0, 255),  # Traverse Color
                (0, 255, 255),  # Final Color
                (255, 0, 127),  # Sorted Color
                # Insertion Sort
                (255, 255, 0),  # Position Color
                # Quick Sort
                (255, 24, 0),  # Pivot
                (32, 70, 73),  # Border
                (183, 4, 238),  # Left
                (6, 2, 105),  # Right
                # Selection Sort
                (51, 102, 0),  # Selected(iMin)
                # Merge Sort
                (128, 0, 0)  # Final Traverse Color
                ]
screen_color = (0, 255, 0)
line_color = (0, 0, 0)
inactive_color = (128, 128, 128)
active_color = (255, 255, 255)
color_arr = []

# Input Box
active = False
box_color = inactive_color
input_box = pygame.Rect(810, 190, 395, 33)

run = True


# ----------------------------Global Variables-----------------------------------------------

# ----------------------------Draw Functions-----------------------------------------------

# Draw the Bars
def draw():
    global x
    draw_heading('SORT VISUALIZATION')
    draw_text_box()
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
        color_arr.append((bar_selected[0]))
        if arr_length == 400:
            pygame.draw.rect(screen, color_arr[i], (x, display_height - 3, bar_width, -unsorted_arr[i]))
        elif arr_length == 100 or arr_length == 80:
            pygame.draw.rect(screen, color_arr[i], (x, display_height - 3, bar_width, -unsorted_arr[i]))
            pygame.draw.rect(screen, (0, 0, 0), (x, display_height - 3, bar_width, -unsorted_arr[i]), 1)
        elif arr_length == 10:
            pygame.draw.rect(screen, color_arr[i], (x, display_height - 3, bar_width, -unsorted_arr[i]))
            pygame.draw.rect(screen, (0, 0, 0), (x, display_height - 3, bar_width, -unsorted_arr[i]), 3)
        else:
            pygame.draw.rect(screen, color_arr[i], (x, display_height - 3, bar_width, -unsorted_arr[i]))
            pygame.draw.rect(screen, (0, 0, 0), (x, display_height - 3, bar_width, -unsorted_arr[i]), 2)
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
    pygame.draw.rect(screen, button_color, button_pos[0])
    pygame.draw.rect(screen, button_color, button_pos[1])
    pygame.draw.rect(screen, (0, 0, 0), button_pos[0], 2)
    pygame.draw.rect(screen, (0, 0, 0), button_pos[1], 2)
    if button_press() == 1:
        pygame.draw.rect(screen, (255, 100, 0), button_pos[0])
    if button_press() == 2:
        pygame.draw.rect(screen, (255, 100, 0), button_pos[1])
    draw_buttons_text()


# Draw text in button
def draw_buttons_text():
    screen.blit(options1.render('SORT', True, line_color), (1060, 376))
    screen.blit(options1.render('GENERATE', True, line_color), (1020, 455))


# Option Buttons
def draw_option_button():
    screen.blit(options.render('or', True, line_color), (1020, 150))
    screen.blit(options.render('Enter your numbers manually(1-400)', True, line_color), (825, 165))
    for num in range(11):
        pygame.draw.rect(screen, button_color, option_pos[num])
        pygame.draw.rect(screen, (0, 0, 0), option_pos[num], 2)
        if option_pos_validate(num):
            pygame.draw.rect(screen, (255, 100, 0), option_pos[num])

    for num in range(5):
        pygame.draw.circle(screen, (0, 0, 0), option_pos[num + 11], 5)
        pygame.draw.circle(screen, (255, 0, 0), option_pos[num + 11], 3)

    if algorithm == 0:
        pygame.draw.circle(screen, (255, 255, 255), option_pos[11], 3)
    elif algorithm == 1:
        pygame.draw.circle(screen, (255, 255, 255), option_pos[12], 3)
    elif algorithm == 2:
        pygame.draw.circle(screen, (255, 255, 255), option_pos[13], 3)
    elif algorithm == 3:
        pygame.draw.circle(screen, (255, 255, 255), option_pos[14], 3)
    elif algorithm == 4:
        pygame.draw.circle(screen, (255, 255, 255), option_pos[15], 3)
    draw_options_text()


# Draw the options
def draw_options_text():
    for num in range(19):
        screen.blit(options.render(option_texts[num], True, line_color), option_pos[num + 17])


def draw_text_box():
    global box_color
    if check_text():
        box_color = active_color
        user_input()
    elif not check_text() and user_element != "":
        box_color = active_color
        user_input()
    else:
        box_color = inactive_color
    pygame.draw.rect(screen, box_color, input_box)
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
    screen.blit(value.render(user_element, True, line_color), (input_box.x + 5, input_box.y + 4))


# ----------------------------Draw Functions-----------------------------------------------

# ----------------------------Functions for manipulating-----------------------------------------------

# Change text to array
def text_to_array():
    global user_element, arr_length, unsorted_arr
    unsorted_arr = []
    user_txt = ""
    for i in user_element:
        if i == '[':
            continue
        elif i == ',' or i == ']':
            unsorted_arr.append(int(user_txt))
            user_txt = ""
        else:
            user_txt += i
    user_element = ""
    arr_length = len(unsorted_arr)
    refresh()


# User Input
def user_input():
    global user_element
    for eve in pygame.event.get():
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_LEFTBRACKET or eve.key == pygame.K_RIGHTBRACKET \
                    or eve.key == pygame.K_COMMA or eve.key == pygame.K_0 \
                    or eve.key == pygame.K_1 or eve.key == pygame.K_2 \
                    or eve.key == pygame.K_3 or eve.key == pygame.K_4 \
                    or eve.key == pygame.K_5 or eve.key == pygame.K_6 \
                    or eve.key == pygame.K_7 or eve.key == pygame.K_8 \
                    or eve.key == pygame.K_9:
                user_element += str(chr(eve.key))
            if eve.key == pygame.K_BACKSPACE:
                user_element = user_element[:-1]
            if eve.key == pygame.K_RETURN:
                text_to_array()


# Show selected values
def values():
    screen.blit(value.render('Length:' + str(arr_length), True, line_color), (810, 550))
    if speed == 0:
        screen.blit(value.render('|Speed:100', True, line_color), (899, 550))
    elif speed == 1:
        screen.blit(value.render('|Speed:80', True, line_color), (899, 550))
    elif speed == 2:
        screen.blit(value.render('|Speed:40', True, line_color), (899, 550))
    elif speed == 3:
        screen.blit(value.render('|Speed:10', True, line_color), (899, 550))
    elif speed == 4:
        screen.blit(value.render('|Speed:1', True, line_color), (899, 550))
    if algorithm == 0:
        screen.blit(value.render('|Algorithm:Bubble Sort', True, line_color), (990, 550))
    elif algorithm == 1:
        screen.blit(value.render('|Algorithm:Insertion Sort', True, line_color), (990, 550))
    elif algorithm == 2:
        screen.blit(value.render('|Algorithm:Selection Sort', True, line_color), (990, 550))
    elif algorithm == 3:
        screen.blit(value.render('|Algorithm:Quick Sort', True, line_color), (990, 550))
    elif algorithm == 4:
        screen.blit(value.render('|Algorithm:Merge Sort', True, line_color), (990, 550))


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


# Select the algorithm
def sort():
    if algorithm == 0:
        bubble_sort()
    elif algorithm == 1:
        insertion_sort()
    elif algorithm == 2:
        selection_sort()
    elif algorithm == 3:
        quickSort(unsorted_arr, 0, len(unsorted_arr) - 1)
    elif algorithm == 4:
        merge_sort(unsorted_arr, 0, len(unsorted_arr) - 1)


# Set new bar color
def set_color(pos, index):
    color_arr[pos] = bar_selected[index]


# Set the color of final sorted array
def set_final_color():
    for i in range(len(unsorted_arr)):
        color_arr[i] = (255, 255, 0)
        color_arr[i + 1] = (255, 255, 0)
        refresh()
        set_color(i, 2)
        pygame.time.delay(100)


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
    for num in range(6):
        if option_pos_validate(num):
            if num + 6 == 6:
                arr_length = 400
            elif num + 6 == 7:
                arr_length = 100
            elif num + 6 == 8:
                arr_length = 80
            elif num + 6 == 9:
                arr_length = 40
            elif num + 6 == 10:
                arr_length = 20
            elif num + 6 == 11:
                arr_length = 10
            generate_new_list()
            return num
    for num in range(5):
        if option_pos_validate(num + 6):
            speed = num


# Circle Validate
def circle_option():
    global mouse_x, mouse_y, algorithm
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    for num in range(5):
        if check_area(mouse_x, mouse_y, option_pos[num + 10][0], option_pos[num + 10][1]) < 5:
            if num + 10 == 10:
                algorithm = 0
            elif num + 10 == 11:
                algorithm = 1
            elif num + 10 == 12:
                algorithm = 2
            elif num + 10 == 13:
                algorithm = 3
            elif num + 10 == 14:
                algorithm = 4


# Checking if the point is inside circle
def check_area(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Check if mouse pointer in textbox
def check_text():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    if input_box.x < mouse_x < input_box.x + input_box.width and \
            input_box.y < mouse_y < input_box.y + input_box.height:
        return True
    return False


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
        set_color(i, 3)


# Selection Sort
def selection_sort():
    for i in range(len(unsorted_arr) - 1, -1, -1):
        iMin = 0
        for j in range(i + 1):
            set_color(j, 1)
            set_color(iMin, 9)
            delay()
            if unsorted_arr[j] > unsorted_arr[iMin]:
                set_color(iMin, 0)
                iMin = j
                set_color(iMin, 9)
            refresh()
            set_color(j, 0)
        set_color(iMin, 0)
        swap(i, iMin)
        set_color(i, 3)


# Insertion Sort
def insertion_sort():
    for i in range(1, len(unsorted_arr)):
        curr_el = unsorted_arr[i]
        pos = i
        set_color(i, 1)
        set_color(pos, 1)
        delay()
        while curr_el < unsorted_arr[pos - 1] and pos > 0:
            unsorted_arr[pos] = unsorted_arr[pos - 1]
            pos = pos - 1
            set_color(pos, 4)
            refresh()
            set_color(pos, 3)
        unsorted_arr[pos] = curr_el
    set_color(i, 3)


# Quick Sort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    refresh()


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    set_color(high, 5)
    for j in range(low, high):
        set_color(i + 1, 6)
        set_color(j, 1)
        delay()
        if arr[j] <= pivot:
            set_color(i + 1, 0)
            i = i + 1
            set_color(i + 1, 6)
            swap(i, j)
            refresh()
        set_color(i + 1, 3)
        set_color(j, 0)
    swap(i + 1, high)
    # set_color(i + 1, 3)
    set_color(high, 0)
    return i + 1


# Merge Sort
def merge_sort(array, l, r):
    mid = (l + r) // 2
    if l < r:
        merge_sort(array, l, mid)
        merge_sort(array, mid + 1, r)
        merge(array, l, mid, mid + 1, r)


def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    while i <= y1 and j <= y2:
        set_color(i, 1)
        set_color(j, 1)
        delay()
        refresh()
        set_color(i, 10)
        set_color(j, 10)
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        set_color(i, 1)
        refresh()
        set_color(i, 0)
        temp.append(array[i])
        i += 1
    while j <= y2:
        set_color(j, 1)
        refresh()
        set_color(j, 0)
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        array[i] = temp[j]
        j += 1
        set_color(i, 3)
        refresh()
        if y2 - x1 == len(array) - 2:
            set_color(i, 5)
        else:
            set_color(i, 3)


# -------------------------------------Sort Functions----------------------------------------------

# -------------------------------------Main----------------------------------------------

# While it is running
while run:
    start_sort = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.MOUSEMOTION:
        #     draw_buttons()
        if event.type == pygame.MOUSEBUTTONUP:
            option_button_press()
            circle_option()
            if button_press() == 1:
                sort()
                set_final_color()
            elif button_press() == 2:
                generate_new_list()

    refill()
    draw()
    pygame.display.update()

# -------------------------------------Main----------------------------------------------
