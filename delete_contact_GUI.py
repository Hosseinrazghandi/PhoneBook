from tkinter import *
from tkinter import messagebox

from phonebook import Phonebook, Contact

from exception import EmptyField, InvalidEmail, InvalidNumber, SameContact

def show_delete_gui():

    def get_info_from_user():
        delete_number = number_entry.get()
        try:
            messagebox.showinfo("show info", f"{Phonebook.delete_contact(delete_number)}")
            clear_entry()
        except InvalidNumber:
            messagebox.showwarning("showwarning", "Invalid Number")

    def back_to_menu():
        window_3.destroy()
        from show_list_GUI import show_menu
        show_menu()

    def clear_entry():
        number_entry.delete(0,END)


    window_3 = Tk()

    window_3.geometry("450x350")
    window_3.title("Add Contact")

    window_3['bg'] = '#ffcccb'

    label = Label(window_3, text="Enter number that you wanna delelte")
    label.grid(row=0,column=0, columnspan=2)

    number_label = Label(window_3, text="Phonenumber: ")
    number_label.grid(row=1, column=0, pady=8)

    number_entry = Entry(width=30)
    number_entry.grid(row=1, column=1, padx=10)
    number_label.config(bg='#90ee90')

    delete_buttun = Button(window_3, text="DELETE", width=10, \
                        command=get_info_from_user)
    delete_buttun.grid(row=4, column=1, padx=5, pady=15)


    back_buttun = Button(window_3, text="BACK TO MENU", width=10, \
                        command=back_to_menu)
    back_buttun.grid(row=6, column=1, padx=5, pady=50)


    window_3.mainloop()