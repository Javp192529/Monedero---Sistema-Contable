from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Monedero - Sistema Contable - Novedades')
root.iconbitmap('images/logo.ico')
root.geometry('850x550')
root.geometry('+560+200')
root.resizable(True, True)

class Novelties:

	frame = Frame(root)
	frame.config(relief='groove', bd=20)
	frame.config(bg='#1F1F1F')
	frame.pack(fill='both', expand=True)

	label_Novelties = Label(frame, text='Novedades', font=('Arial', 30), fg='#1AC', bg='#1F1F1F')
	label_Novelties.place(relwidth=1, relheight=0.25)

	box_Novelties = Text(frame)
	box_Novelties.place(relwidth=0.978, relheight=0.75, rely=0.25)
	box_Novelties.config(bg='#1F1F1F', fg='#FFF', font=('Console', 20))
	box_Novelties.insert(1.0, '                                       Versión: 1.0.0\n')
	# Son 39 espacios para que quede en el centro
	box_Novelties.insert(2.0, '* Se ha creado la aplicación en su versión 1.0.0\n')
	box_Novelties.insert(3.0, '* Ya es posible salir desde el menú archivos\n')
	box_Novelties.insert(4.0, '* Se puede consultar información sobre la aplicación y su creador a través del menú de ayuda\n')
	box_Novelties.insert(5.0, '* Se ha diseñado una Interfáz Gráfica amigable con la vista\n')
	box_Novelties.config(state='disabled')

	scroll_V = Scrollbar(frame, command=box_Novelties.yview)
	scroll_V.place(relheight=0.75, rely=0.25, relx=0.978)
	box_Novelties.config(yscrollcommand=scroll_V.set)

	root.mainloop()
