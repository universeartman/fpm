""" FPM calculator inputs MPH, Distance to target and delta altitude and
outputs FPM rquirements """

def fpm():
    ''' Input the required data and set as usable variables'''
    ''' Input MPH and set as mph'''
    
    '''Input distnce in miles and set as dist'''
    
    '''Input delta altitude in feet and set as alt_d'''
    
    """Make the conversions required to do the math"""
    
    '''Do the math'''
    
    """Print the required FPM requirement"""
    from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()


x = 15

blackline = canvas.create_line(0, 70, 200, 70)
redline = canvas.create_line(0,70, 200, x, fill="red")
red2line = canvas.create_line(200,70, 200, x, fill="red")


root.mainloop()
