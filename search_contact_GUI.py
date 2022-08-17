from tkinter import *
from tkinter import messagebox
from tkinter.font import *


from phonebook import Phonebook, Contact

from exception import EmptyField, InvalidEmail, InvalidNumber, SameContact

def show_search_gui():

    def get_info_from_user():
        search_number = number_entry.get()
        search_name = name_entry.get()

        if search_number:
            try:
                messagebox.showinfo("show info", f"{Phonebook.search_with_number(search_number)}")
                clear_entry()

            except InvalidNumber:
                messagebox.showwarning("showwarning", "Invalid Number")

        elif search_name:
            messagebox.showinfo("show info", f"{Phonebook.search_with_name(search_name)}")
            clear_entry()

        else:
            messagebox.showwarning("showwarning", "Empty Feild")


    def back_to_menu():
        window_3.destroy()
        from show_list_GUI import show_menu
        show_menu()


    def clear_entry():
        number_entry.delete(0, END)
        name_entry.delete(0, END)


    window_3 = Tk()

    window_3.geometry("450x450")
    window_3.title("Add Contact")

    my_font = Font(family='Helvatica' , size=20)

    window_3['bg'] = '#ffcccb'

    label_1 = Label(window_3, text="Enter name that you wanna find")
    label_1.grid(row=0,column=0, columnspan=2)

    name_label = Label(window_3, text="name: ")
    name_label.grid(row=1, column=0, pady=8)
    name_label.config(bg='#90ee90')

    name_entry = Entry(width=30)
    name_entry.grid(row=1, column=1, padx=10)
    

    label_2 = Label(window_3, text="OR", font=my_font)
    label_2.grid(row=3,column=0, columnspan=2, pady=15)


    label_3 = Label(window_3, text="Enter number that you wanna delelte")
    label_3.grid(row=5,column=0, columnspan=2, pady=8)

    number_label = Label(window_3, text="Phonenumber: ")
    number_label.grid(row=6, column=0, pady=8)

    number_entry = Entry(width=30)
    number_entry.grid(row=6, column=1, padx=10)
    number_label.config(bg='#90ee90')

    delete_buttun = Button(window_3, text="FIND", width=10, \
                        command=get_info_from_user)
    delete_buttun.grid(row=7, column=1, padx=5, pady=15)


    back_buttun = Button(window_3, text="BACK TO MENU", width=10, \
                        command=back_to_menu)
    back_buttun.grid(row=8, column=1, padx=5, pady=50)


    window_3.mainloop()