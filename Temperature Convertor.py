# Temperature Convertor By Coder Mohit.
# Follow me On Instagram, Facebook.
# Subscribe Coder Mohit YouTube Channel.

from tkinter import *
window= Tk()
window.title('Temperature Converter By Coder Mohit ')
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

label=Label(text='Convert Celsius Into Fahrenheit:',font=('Courier',25,'bold'))
label2=Label(text='Project By Coder Mohit',font=('Courier',15))
label3=Label(text='Enter Temperature in Celsius',font=('Courier',10,'bold'))

label.grid(column=2, row=0)
label.config(pady=10)
label2.grid(column=2, row=1)
label2.config(pady=10)
label3.grid(column=2, row=3)
label3.config(pady=10)


input = Entry()
input.grid(row=2,column=2)

ans=Label(text='Formula : (10°C × 9/5) + 32 = 50°F',font=('Courier',15,'bold'))
ans.grid(row=4,column=2)

def convert():
    temp = float(input.get())
    temp_F= temp*9/5+32
    ans['text']='Temperature in Fahrenheit is: '+str(int(temp_F))


button=Button(text='Convert',font=('Courier',10,'bold'), command=convert)
button.grid(row=5,column=2)

window.mainloop()
