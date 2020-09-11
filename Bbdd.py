import sqlite3
from tkinter import *
from tkinter import messagebox


BBDD_name = StringVar()

root = Toplevel()
root.title('Crear Base de Datos')
root.iconbitmap('images/logo.ico')
root.geometry('365x180')
root.geometry('+760+340')


class data_Base:

    def assign():

        if BBDD_name.get() != " ":

            name = BBDD_name.get()

            myConnection = sqlite3.connect(f'{name}')
            myCursor = myConnection.cursor()

            myCursor.execute('CREATE TABLE DEUDAS (GASTOS VARCHAR(20), VALOR DECIMAL)')

            root.destroy()

    frame = Frame(root)
    frame.config(relief='groove', bd=20)
    frame.config(bg='#1F1F1F')
    frame.pack(fill='both', expand=True)

    box_Name = Entry(frame, textvariable=BBDD_name)
    box_Name.config(justify='center', font=('Arial', 12))
    box_Name.grid(row=1, column=1, columnspan=3, pady=10, padx=10)

    button_Accept = Button(frame, text='Aceptar', width=10, height=1, borderwidth=3, command=assign)
    button_Accept.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    label_Tittle = Label(frame, text='Dale un nombre a la nueva Base de Datos:')
    label_Tittle.config(font=('Arial', 12), fg='#1AC', bg='#1F1F1F')
    label_Tittle.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky='e')

    root.mainloop()
