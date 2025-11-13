import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)    #time update every second

label = tk.Label(root, font=('calibri', 40, 'bold'), background='Black', 
                                                    foreground='#00FF00',       
                                                    relief='ridge') # gives raised effect for 3D glow
label.pack(anchor='center') #pack= arrange the element in tkinter

time()

root.mainloop()  #mainloop = tkinter module method which keep the window in loop user wait for input