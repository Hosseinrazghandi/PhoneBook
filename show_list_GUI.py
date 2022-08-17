from tkinter import *
from tkinter import messagebox
from tkinter.font import *

from add_contact_GUI import show_add_gui

from delete_contact_GUI import show_delete_gui

from search_contact_GUI import show_search_gui

def show_menu():

    def open_choose_window():
        chose = list_box.get(ACTIVE)

        if chose == "1. Add Contact":
            window.destroy()
            show_add_gui()

        elif chose == "2. Delete Contact":
            window.destroy()
            show_delete_gui()

        elif chose == "3. Search Contact":
            window.destroy()
            show_search_gui()

        elif chose == "4. Exit":
            window.destroy()
        
        else:
            messagebox.showwarning("Choise", "Please choose one")

            



    window = Tk()

    my_font = Font(family='Helvatica' , size=20)
    my_font_2 = Font(family='Consolas' , size=15)

    window.geometry("400x550")
    window.title("Menu")

    window['bg'] = '#ffcccb'

    list_box = Listbox(window, font=my_font, bg='#CEFCBA', activestyle= 'dotbox')

    label = Label(window, text="Choose One", font=my_font_2)
    label.grid(row=0,column=0, padx=30, pady=15)

    list_box.insert(1, "1. Add Contact")
    list_box.insert(2, "")
    list_box.insert(3, "2. Delete Contact")
    list_box.insert(4, "")
    list_box.insert(5, "3. Search Contact")
    list_box.insert(6, "")
    list_box.insert(7, "4. Exit")

    list_box.grid(row=1,column=0, padx=30, pady=15)


    button = Button(window, text='Ok', font = my_font_2 ,command=open_choose_window)
    button.grid(row=2,column=0, padx=30, pady=15)

    





    window.mainloop()