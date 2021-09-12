from tkinter import *
from db import Database

DB = Database()
ws = Tk()
ws.title('Python Guides')
ws.geometry('400x300')
ws.config(bg='#446644')

lb = Listbox(ws, height=8, width= 50, border=0)
lb.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

def extract_data_db():
    size_lb = lb.size()

    if size_lb > 1:
        lb.delete(0, END)

    data = DB.get_testing()
    for position in range(0, len(data)):
        row = data[position]
        lb.insert(position, row)

btn3 = Button(ws, text="Actualizar", width=12, command=extract_data_db)
btn3.grid(row=2, column=2)

ws.title("Gerente de ventas")
ws.geometry("700x350")

ws.mainloop()