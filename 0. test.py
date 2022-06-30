import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

window = tk.Tk()

#btn = tk.Label(window, text='A simple plot')
#btn.grid(row=0, column=0, padx=20, pady=10)

x = ['Col A', 'Col B', 'Col C']

y = [50, 20, 80]

def plot_graph(figsize_x, figsize_y):
        fig = plt.figure(figsize=(figsize_x, figsize_y))
        plt.bar(x=x, height=y)

        # You can make your x axis labels vertical using the rotation
        plt.xticks(x, rotation=90)

        # specify the window as master
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        # navigation toolbar
        toolbarFrame = tk.Frame(master=window)
        toolbarFrame.pack(side='bottom', fill='both', expand=True)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

def resize(event):
        print('Widget: ', event.widget, 'Height: ', event.height, 'Width: ', event.width)
        if event.widget == '.':
                plot_graph(event.width/100, event.height/100)

plot_graph(4, 5)
#window.bind('<Configure>', resize)

window.mainloop()