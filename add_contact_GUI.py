from tkinter import *
from tkinter import messagebox


from phonebook import Phonebook, Contact

from exception import EmptyField, InvalidEmail, InvalidNumber, SameContact



def show_add_gui():

    def get_info_from_user():    
        contact_name = name_entry.get()
        contact_number = number_entry.get()
        contact_email = email_entry.get()

        try:
            person = Contact(fullname= contact_name, phonenumber= contact_number, email= contact_email)
        
        except InvalidNumber:
            messagebox.showwarning("showwarning", "Invalid Number")

        except InvalidEmail:
            messagebox.showwarning("showwarning", "Invalid Email")

        try:
            added_con = Phonebook.add_contact(person)
            if added_con == EmptyField:
                raise EmptyField

            elif added_con == SameContact:
                raise SameContact

            messagebox.showinfo("Add Successfully", person.show_info())
            clear_entry()

        except EmptyField:
            messagebox.showwarning("showwarning", "Empty Field")

        except SameContact:
            messagebox.showwarning("showwarning", "Same Number")


    def clear_entry():
        name_entry.delete(0, END)
        number_entry.delete(0,END)
        email_entry.delete(0,END)


    def back_to_menu():
        window_2.destroy()
        from show_list_GUI import show_menu
        show_menu()


    window_2 = Tk()

    window_2.geometry("450x350")
    window_2.title("Add Contact")

    window_2['bg'] = '#ffcccb'

    name_label = Label(window_2, text="Name: ")
    name_label.grid(row=0, column=0, pady=8)
    name_label.config(bg='#90ee90')

    name_entry = Entry(width=30)
    name_entry.grid(row=0, column=1 , padx=10)


    number_label = Label(window_2, text="Phonenumber: ")
    number_label.grid(row=1, column=0, pady=8)
    number_label.config(bg='#90ee90')

    number_entry = Entry(width=30)
    number_entry.grid(row=1, column=1, padx=10)

    

    email_label = Label(window_2, text="Email: ")
    email_label.grid(row=2, column=0, pady=8)
    email_label.config(bg='#90ee90')

    email_entry = Entry(width=30)
    email_entry.grid(row=2, column=1, padx=10)


    add_buttun = Button(window_2, text="ADD", width=10, \
                        command=get_info_from_user)
    add_buttun.grid(row=4, column=1, padx=5, pady=15)


    clear_butten = Button(window_2, text="Clear", width=5, command=clear_entry)
    clear_butten.grid(row=5, column=1)


    back_buttun = Button(window_2, text="BACK TO MENU", width=10, \
                        command=back_to_menu)
    back_buttun.grid(row=6, column=1, padx=5, pady=50)

    window_2.mainloop()

