from tkinter import *
from tkinter import ttk 
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting ALgorithm Visualization')
root.maxsize(1100, 700)
root.config(bg="black")

#variables
selected_algo = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_width=750
    c_height=700
    x_width=c_width/(len(data)+1)
    offset = 30
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 660 
        x1 = (i+1)*x_width+offset
        y1 = c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()

def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data, ['red' for x in range(len(data))])

def startAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])

#frame
ui_frame = Frame(root, width=250, height=700, bg='grey')
ui_frame.grid(row=0, column=0)
ui_frame.grid_propagate(0)

canvas = Canvas(root, width=800, height=700, bg='white')
canvas.grid(row=0, column=1)

Label(ui_frame, text="Algorithm", bg='grey').grid(row=0, column=0, padx=5, pady=(50,10))
algMenu = ttk.Combobox(ui_frame,  textvariable=selected_algo, width=15, values=['Bubble Sort','Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=(50, 10))
algMenu.current(0)

# Buttons
# Start--Button--Goes--Here
Button(ui_frame, text="Generate", command=Generate, bg='red').grid(row=1, column=0, padx=5, pady=15, columnspan=2)
Button(ui_frame, text="Start", command=startAlgorithm, bg='red').grid(row=6, column=0, padx=5, pady=15, columnspan=2)
# User Input

speedScale = Scale(ui_frame, from_=0.1, to=2.0, length=130, digits=2, resolution=0.2, orient=HORIZONTAL, label="Speed [s]")
speedScale.grid(row=2, column=0, padx=5, pady=15, columnspan=2)

sizeEntry = Scale(ui_frame, from_=5, to=30, length=130, resolution=1, orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=3, column=0, padx=5, pady=15, columnspan=2)

minEntry = Scale(ui_frame, from_=1, to=10, length=130, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=4, column=0, padx=5, pady=15, columnspan=2)

maxEntry = Scale(ui_frame, from_=20, to=100, length=130, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=5, column=0, padx=5, pady=15, columnspan=2)



root.mainloop()
