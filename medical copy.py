from tkinter import *
from tkcalendar import DateEntry
med=Tk()
med.title("BILL")
med.config(bg='#ECF5F2')
med.geometry("800x400")
Label(med,text='AK MEDICALS',font='times 28 bold',bg='#ECF5F2').grid(row=0,column=2)
Label(med,text='Near Petrol Pump EDAPPAL, Pin:679582 \nPhone:9645703011 \n________________________________________________________',bg='#ECF5F2').grid(row=1,column=2)
DateEntry(med,text='DATE: ').grid(row=2,column=4)
Label(med,text='DATE:',bg='#ECF5F2').grid(row=2,column=3)
Label(med,text='BILL NO: ',bg='#ECF5F2').grid(row=2,column=0)
Entry(med).grid(row=2,column=1)
Label(med,text='NAME: ',bg='#ECF5F2').grid(row=3,column=0)
Entry(med).grid(row=3,column=1)
Label(med,text='AGE: ',bg='#ECF5F2').grid(row=4,column=0)
Entry(med).grid(row=4,column=1)
Label(med,text='PHONE: ',bg='#ECF5F2').grid(row=5,column=0)
Entry(med).grid(row=5,column=1)
Label(med,text='Consulting DR: ',bg='#ECF5F2').grid(row=4,column=3)
Entry(med).grid(row=4,column=4)

Label(med,text='--------------',bg='#ECF5F2').grid(row=7,column=0)
Label(med,text='------------------',bg='#ECF5F2').grid(row=7,column=1)
Label(med,text='------------------',bg='#ECF5F2').grid(row=7,column=2)
Label(med,text='------------------',bg='#ECF5F2').grid(row=7,column=3)
Label(med,text='Sl.no',bg='#ECF5F2').grid(row=6,column=0)
Label(med,text='MEDICINES',bg='#ECF5F2').grid(row=6,column=1)
Entry(med).grid(row=8,column=1)
Entry(med).grid(row=9,column=1)
Label(med,text='QUANTITY',bg='#ECF5F2').grid(row=6,column=2)
Entry(med).grid(row=8,column=2)
Entry(med).grid(row=9,column=2)
Label(med,text='PRICE',bg='#ECF5F2').grid(row=6,column=3)
Entry(med).grid(row=8,column=3)
Entry(med).grid(row=9,column=3)
Entry(med).grid(row=8,column=0)
Entry(med).grid(row=9,column=0)
Label(med,text=':TOTAL',bg='#ECF5F2').grid(row=13,column=4)
Entry(med).grid(row=13,column=3)









med.mainloop()
