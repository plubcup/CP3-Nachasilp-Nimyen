from tkinter import *
import math
def leftclickbutton(event):
    Result = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    textResult.configure(text = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if Result >=30:
        print("อ้วนมาก ")
    elif Result >= 25.0 and Result <= 29.9:
        print("อ้วน")
    elif Result >= 23.0 and Result <= 24.9:
        print("น้ำหนักเกิน")
    elif Result >= 18.6 and Result <= 22.9:
        print("น้ำหนักปกติ เหมาะสม")
    else:
        print("ผอมเกินไป")
main = Tk()
labelHeight = Label(main,text = "ส่วนสูง (Cm.)").grid(row = 0,column =0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row = 0,column = 1)
labelWeight = Label(main,text = "น้ำหนัก (Kg.)").grid(row = 1,column =0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row = 1,column = 1)
calculateButton=Button(main,text = "คำนวน")
calculateButton.bind('<Button-1>',leftclickbutton)
calculateButton.grid(row = 2,column = 0)
textResult = Label(main,text = "ผลลัพธ์")
textResult.grid(row = 2,column = 1)
main.mainloop()