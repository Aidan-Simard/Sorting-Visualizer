import pygame
import tkinter as tk
import random

pygame.init()

# Screen sizing
screen_width = 1200
screen_height = 600

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
LIGHT_GREY = (220, 220, 220)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

screen = pygame.display.set_mode((screen_width, screen_height))

lines = [val for val in range(1, 51)]


# RANDOMIZE LINES ON SCREEN
def randomize_lines(lines):
    '''(List)->None
    Randomizes the lines on the screen'''
    # Shuffle the lines 7 times
    for shuffle in range(7):

        # Allows user to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        lines_index = [ind for ind in range(len(lines))]
        for swap in range(25):
            pygame.time.wait(8)

            # Pick 2 random indeces and swap the positions of the indeces in the lines list

            first = lines_index.pop(random.randint(0, len(lines_index)-1))
            second = lines_index.pop(random.randint(0, len(lines_index)-1))
            lines[first], lines[second] = lines[second], lines[first]

            # Update the screen
            screen.fill(LIGHT_GREY)
            draw_all_lines(lines)
            pygame.display.update()


# DRAW ALL LINES ON SCREEN
def draw_all_lines(lines):
    '''(List)->None
    Draws all lines on the screen'''
    x = 100
    for line in lines:
        draw_line(line, x, BLUE)
        x += 20

def draw_line(line, x, colour):
    '''(Line, Integer, Colour)->None
    Draws a line on the screen
    Precondition: 0 <= x <= 980'''
    height = line*10
    pygame.draw.rect(screen, colour, (x, screen_height-height, 19, height))


# UPDATE LINES ON SCREEN
def update_screen():
    pygame.time.wait(10)
    screen.fill(LIGHT_GREY)
    draw_all_lines(lines)
    pygame.display.update()


# BUBBLE SORT
def bubble_sort(lines):
    '''(List)->None
    Sorts the list using bubble sort'''
    swapped = True
    while swapped:

        # Allows user to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        swapped = False
        ind = 1
        while ind < len(lines):
            if lines[ind-1] > lines[ind]:
                lines[ind-1], lines[ind] = lines[ind], lines[ind-1]
                swapped = True
            ind += 1

            update_screen()


# INSERTION SORT
def insertion_sort(lines):
    '''(List)->None
    Sorts the list using insertion sort'''
    for i in range(1, len(lines)):

        # Allows user to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        j = i

        while j > 0 and lines[j-1] > lines[j]:
            lines[j-1], lines[j] = lines[j], lines[j-1]
            j -= 1

            update_screen()


# MERGE SORT
def merge_sort(lines):
    '''(List)->List
    Recursively creates sublists from list'''
    if len(lines) <= 1:
        return lines

    # Allows user to exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    left = lines[len(lines)/2:]
    right = lines[:len(lines)/2]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    '''(List, List)->List
    Merges lists left and right in sorted order'''
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

        update_screen()
    
    while len(left) != 0:
        result.append(left.pop(0))
    
    while len(right) != 0:
        result.append(right.pop(0))

    return result


# QUICK SORT
def quick_sort(lines, l=0, r=len(lines)-1):
    # Allows user to exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if l < r:        
        pivot = partition(lines, l, r)
        quick_sort(lines, l, pivot-1)
        quick_sort(lines, pivot+1, r)

def partition(lines, l, r):
    pivot = lines[r]
    i = l
    for j in range(l, r):
        if lines[j] < pivot:
            lines[i], lines[j] = lines[j], lines[i]
            i += 1

        update_screen()

    lines[i], lines[r] = lines[r], lines[i]

    update_screen()

    return i


# COMPLETED SORT ANIMATION
def sort_complete(lines):
    x = 100
    for line in lines:
        pygame.time.wait(5)
        draw_line(line, x, GREEN)
        pygame.display.update()
        x += 20


# EXECUTE SORTING ALGORITHMS
def execute_bubble_sort(lines, window):
    window.destroy()
    pygame.time.wait(1000)
    bubble_sort(lines)
    sort_complete(lines)

def execute_insertion_sort(lines, window):
    window.destroy()
    pygame.time.wait(1000)
    insertion_sort(lines)
    sort_complete(lines)

def execute_merge_sort(lines, window):
    window.destroy()    
    pygame.time.wait(1000)
    insertion_sort(lines)
    sort_complete(lines)

def execute_quick_sort(lines, window):
    window.destroy()    
    pygame.time.wait(1000)
    quick_sort(lines)
    sort_complete(lines)


def close_tk(window):
    window.destroy()
    pygame.quit()


# MAIN
def main():
    running = True
    randomized = False
    complete = False
    FPS = 60
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(LIGHT_GREY)

        draw_all_lines(lines)

        pygame.display.update()
        pygame.time.wait(1000)
        randomize_lines(lines)

        window = tk.Tk()
        greet = tk.Label(text="Please select a sorting algorithm")
        greet.pack()
        window.title("Sorting Visualizer")
        window.geometry("180x180")

        bubble = tk.Button(text="Bubble Sort", width=20, command=lambda: execute_bubble_sort(lines, window)).pack()
        insertion = tk.Button(text="Insertion Sort", width=20, command=lambda: execute_insertion_sort(lines, window)).pack()
        merge = tk.Button(text="Merge Sort", width=20, command=lambda: execute_merge_sort(lines, window)).pack()
        quick_sort = tk.Button(text="Quick Sort", width=20, command=lambda: execute_quick_sort(lines, window)).pack()
        exit_button = tk.Button(text="Exit", width=20, command=lambda: close_tk(window)).pack()
        
        window.mainloop()

        pygame.display.update()

main()