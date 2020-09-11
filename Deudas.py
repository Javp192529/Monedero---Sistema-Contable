import sys
from tkinter import *
from tkinter import messagebox

sys.path.extend(['Práctica Guiada - Python Avanzado - Interfáz Gráfica'])

class Debts:

	def save():
		pass

	def clean():
		pass

	def load():
		pass

	# Para evitar un error por ejecución de dos Tk() simultaneamente, el root lo establecí como Toplevel() en vez de Tk()

	root = Toplevel()
	root.title('Monedero - Sistema Contable - Deudas')
	root.iconbitmap('images/logo.ico')
	root.geometry('750x550')
	root.geometry('+585+265')
	root.resizable(False, False)

	myID = str(1)
	myVISA = StringVar()
	myTV = StringVar()
	myInternet = StringVar()
	myDividend = StringVar()
	myCommon_Expense = StringVar()
	myGAS = StringVar()
	myCommodity = StringVar()
	myFair = StringVar()
	myGasoline = StringVar()
	myTelephone = StringVar()
	myLight = StringVar()
	myWater = StringVar()
	total_Debt = StringVar()

	frame = Frame(root)
	frame.config(relief='groove', bd=20)
	frame.config(bg='#1F1F1F')
	frame.pack(fill='both', expand=True)

	image_Tittle = PhotoImage(file='images/deudas.png')
	label_Tittle = Label(frame, image=image_Tittle, bg='#1F1F1F').grid(row=0, column=1, columnspan=2, pady=10)

	label_Total_Debt = Label(frame, text='DEUDA TOTAL:', font=('Arial', 15), fg='#1AC', bg='#1F1F1F')
	label_Total_Debt.grid(row=1, column=1, columnspan=1, pady=20)

	box_label_Total_Debt = Label(frame, bd=0, textvariable=total_Debt)
	box_label_Total_Debt.grid(row=1, column=2, sticky='w', columnspan=2, padx=10, pady=10)
	box_label_Total_Debt.config(bg='#1F1F1F', fg='#FFF', font=('Arial', 15))

	box_VISA = Entry(frame, font=('Arial', 11), textvariable=myVISA)
	box_VISA.grid(row=2, column=1, padx=10, pady=10)

	box_TV = Entry(frame, font=('Arial', 11), textvariable=myTV)
	box_TV.grid(row=3, column=1, padx=10, pady=10)

	box_Internet = Entry(frame, font=('Arial', 11), textvariable=myInternet)
	box_Internet.grid(row=4, column=1, padx=10, pady=10)

	box_Dividend = Entry(frame, font=('Arial', 11), textvariable=myDividend)
	box_Dividend.grid(row=5, column=1, padx=10, pady=10)

	box_Common_Expense = Entry(frame, font=('Arial', 11), textvariable=myCommon_Expense)
	box_Common_Expense.grid(row=6, column=1, padx=10, pady=10)

	box_GAS = Entry(frame, font=('Arial', 11), textvariable=myGAS)
	box_GAS.grid(row=7, column=1, padx=10, pady=10)

	box_Commodity = Entry(frame, font=('Arial', 11), textvariable=myCommodity)
	box_Commodity.grid(row=2, column=3, padx=10, pady=10)

	box_Fair = Entry(frame, font=('Arial', 11), textvariable=myFair)
	box_Fair.grid(row=3, column=3, padx=10, pady=10)

	box_Gasoline = Entry(frame, font=('Arial', 11), textvariable=myGasoline)
	box_Gasoline.grid(row=4, column=3, padx=10, pady=10)

	box_Telephone = Entry(frame, font=('Arial', 11), textvariable=myTelephone)
	box_Telephone.grid(row=5, column=3, padx=10, pady=10)

	box_Light = Entry(frame, font=('Arial', 11), textvariable=myLight)
	box_Light.grid(row=6, column=3, padx=10, pady=10)

	box_Water = Entry(frame, font=('Arial', 11), textvariable=myWater)
	box_Water.grid(row=7, column=3, padx=10, pady=10)

	label_VISA = Label(frame, text='VISA:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_VISA.grid(row=2, column=0, padx=10, pady=10, sticky='e')
	label_TV = Label(frame, text='TV:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_TV.grid(row=3, column=0, padx=10, pady=10, sticky='e')
	label_Internet = Label(frame, text='INTERNET:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Internet.grid(row=4, column=0, padx=10, pady=10, sticky='e')
	label_Dividend = Label(frame, text='DIVIDENDO:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Dividend.grid(row=5, column=0, padx=10, pady=10, sticky='e')
	label_Common_Expense = Label(frame, text='GASTO COMÚN:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Common_Expense.grid(row=6, column=0, padx=10, pady=10, sticky='e')
	label_GAS = Label(frame, text='GAS:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_GAS.grid(row=7, column=0, padx=10, pady=10, sticky='e')

	label_Commodity = Label(frame, text='MERCADERIA:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Commodity.grid(row=2, column=2, padx=10, pady=10, sticky='e')
	label_Fair = Label(frame, text='FERIA:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Fair.grid(row=3, column=2, padx=10, pady=10, sticky='e')
	label_Gasoline = Label(frame, text='GASOLINA:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Gasoline.grid(row=4, column=2, padx=10, pady=10, sticky='e')
	label_Telephone = Label(frame, text='TELEFONO:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Telephone.grid(row=5, column=2, padx=10, pady=10, sticky='e')
	label_Light = Label(frame, text='LUZ:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Light.grid(row=6, column=2, padx=10, pady=10, sticky='e')
	label_Water = Label(frame, text='AGUA:', font=('Arial', 14), fg='#1AC', bg='#1F1F1F')
	label_Water.grid(row=7, column=2, padx=10, pady=10, sticky='e')

	button_Save = Button(frame, text='Guardar', command=save).grid(row=8, column=1, columnspan=1, padx=10, pady=10)
	button_Clean = Button(frame, text='Limpiar', command=clean).grid(row=8, column=2, columnspan=1, padx=10, pady=10)

	root.mainloop()
