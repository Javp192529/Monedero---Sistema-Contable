import sys
from tkinter import *
from tkinter import messagebox

sys.path.extend(['Práctica Guiada - Python Avanzado - Interfáz Gráfica'])

root = Tk()
root.title('Monedero - Sistema Contable')
root.iconbitmap('images/logo.ico')
root.state('zoomed')
root.geometry('+0+0')


class CoinPurse:

    def exit_CoinPurse():
        value = messagebox.askokcancel('Atención', '¿Estás seguro que deseas salir?')

        if value:
            root.destroy()

    def license_Info():
        messagebox.showwarning('Licencia', 'Licencia Activada')

    def version_Info():
        """
        C: Correción de código N°
        B: Actualización de Base de Datos N°
        I: Actualización de Información N°
        AGS: AGAPITO - SEGISMUNDO
        """
        messagebox.showinfo('Versión', 'Versión: 1.0.0 - Build: C0B1I0AGS')

    def about_Info():
        messagebox.showinfo('Monedero', 'Creado por:\nJuan A. Villodres P.\nCopyright © 2020')

    def novelties_Info():
        import Novedades
        Novedades.Novelties
        
    def debts():
        import Deudas
        Deudas.Debts

    def bbdd():
        import Bbdd
        Bbdd.data_Base

    menu_Bar = Menu(root)
    root.config(menu=menu_Bar, width=300, height=300)

    menu_File = Menu(menu_Bar, tearoff=0)
    menu_File.add_command(label='Crear BBDD', command=bbdd)
    menu_File.add_separator()
    menu_File.add_command(label='Salir', command=exit_CoinPurse)

    menu_Accounting = Menu(menu_Bar, tearoff=0)
    menu_Accounting.add_command(label='Deudas', command=debts)
    menu_Accounting.add_command(label='Prestamos')
    menu_Accounting.add_command(label='General')
    menu_Accounting.add_command(label='Banco')

    menu_Help = Menu(menu_Bar, tearoff=0)
    menu_Help.add_command(label='Licencia', command=license_Info)
    menu_Help.add_command(label='Versión', command=version_Info)
    menu_Help.add_command(label='Novedades', command=novelties_Info)
    menu_Help.add_separator()
    menu_Help.add_command(label='Acerca de...', command=about_Info)

    menu_Bar.add_cascade(label='Archivo', menu=menu_File)
    menu_Bar.add_cascade(label='Contabilidad', menu=menu_Accounting)
    menu_Bar.add_cascade(label='Ayuda', menu=menu_Help)

    frame = Frame(root)
    frame.config(relief='groove', bd=20)
    frame.config(bg='#1F1F1F')
    frame.pack(fill='both', expand='True')

    image_Tittle = PhotoImage(file='images/titulo.png')
    label_Tittle = Label(frame, image=image_Tittle, bg='#1F1F1F').place(x=275, y=100)
    image_Accounting = PhotoImage(file='images/contabilidad.png')
    label_Image = Label(frame, image=image_Accounting, width=1860, height=600).place(x=10, y=325)

    root.mainloop()
