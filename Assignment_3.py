from tkinter import *

# Set up the tkinter window
root = Tk()
root.title("Drawing Shapes with Tkinter")

# Set up the canvas
canvas = Canvas(root, width=500, height=500, bg='black')
canvas.pack()

# Define the function to draw a rectangle
def draw_rect(event):
    x1, y1 = (event.x - 60), (event.y - 40)
    x2, y2 = (event.x + 60), (event.y + 40)
    canvas.create_rectangle(x1, y1, x2, y2, fill='yellow')

# Define the function to draw a circle
def draw_circle(event):
    x1, y1 = (event.x - 50), (event.y - 50)
    x2, y2 = (event.x + 50), (event.y + 50)
    canvas.create_oval(x1, y1, x2, y2, fill='blue')
def draw_square(event):
    x1, y1 = (event.x - 40), (event.y - 40)
    x2, y2 = (event.x + 40), (event.y + 40)
    canvas.create_rectangle(x1, y1, x2, y2, fill='red')
# Bind the left mouse click to the draw functions
canvas.bind('<Button-1>', draw_square)
canvas.bind('<Button-2>', draw_rect)
canvas.bind('<Button-3>', draw_circle)

# Start the tkinter event loop
root.mainloop()