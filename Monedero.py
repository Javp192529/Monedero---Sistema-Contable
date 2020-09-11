import sys
from tkinter import *
from tkinter import messagebox

sys.path.extend(['Práctica Guiada - Python Avanzado - Interfáz Gráfica'])

root = Tk()
root.title('Monedero - Sistema Contable - Acceso')
root.iconbitmap('images/logo.ico')
root.geometry('+820+400')
root.geometry('280x175')
root.resizable(False, False)


def login():

    if usser.get() == 'Juan' and password.get() == '1234':
        messagebox.showinfo('Login Correcto', f'Bienvenido {usser.get()}')
        root.destroy()
        import Principal
        Principal.CoinPurse()

    else:
        messagebox.showerror('Login Incorrecto', 'Usuario y/o contraseña incorrectos')


frame = Frame(root)
frame.config(relief='groove', bd=20)
frame.config(bg='#1F1F1F')
frame.pack(fill='both', expand='True')

usser = StringVar()
password = StringVar()

box_Usser = Entry(frame, textvariable=usser)
box_Usser.grid(row=0, column=1, padx=10, pady=10)

box_Password = Entry(frame, textvariable=password)
box_Password.grid(row=1, column=1, padx=10, pady=10)
box_Password.config(show='*')

button_Login = Button(frame, text='Ingresar', width=10, height=1, borderwidth=3, command=login)
button_Login.grid(row=2, column=1, padx=10, pady=10)

label_Usser = Label(frame, text='Usuario: ', fg='#1AC', bg='#1F1F1F')
label_Usser.grid(row=0, column=0, sticky='e', padx=10, pady=10)

label_Password = Label(frame, text='Contraseña: ', fg='#1AC', bg='#1F1F1F')
label_Password.grid(row=1, column=0, sticky='e', padx=10, pady=10)

root.mainloop()
