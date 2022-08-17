import re

from exception import EmptyField, InvalidEmail, InvalidNumber, SameContact


class Contact:
    def __init__(self, fullname, phonenumber, email):
        self.fullname = fullname
        self.phonenumber = self.__valid_phone(phonenumber)
        self.email = self.__valid_email(email)

    
    def __valid_phone(self, phonenumber):
        if phonenumber.isdigit():
            return phonenumber

        else:
            raise InvalidNumber

    
    def __valid_email(self, email):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if re.fullmatch(regex, email):
            return email

        else:
            raise InvalidEmail

    
    def show_info(self):
        return(f"Name: {self.fullname}\nPhonenumber: {self.phonenumber}\nEmail: {self.email}\n")


    def __call__(self):
        return (f"{self.fullname} {self.phonenumber} {self.email}")


class Phonebook:
    __list_of_contacts = list()

    @classmethod
    def add_to_list(cls, person_info):
        try:
            if person_info.phonenumber and person_info.email and person_info.fullname:
                if cls.search_with_number(person_info.phonenumber) == None:
                    cls.__list_of_contacts.append(person_info)

                else:
                    raise SameContact
            else:
                raise EmptyField

        except EmptyField:
            return EmptyField

        except SameContact:
            return SameContact


    @classmethod
    def add_contact(cls, person_info):
        try:
            if person_info.phonenumber and person_info.email and person_info.fullname:
                if not cls.search_with_number(person_info.phonenumber):
                    cls.__list_of_contacts.append(person_info)
                    file.write_in_file(person_info)

                else:
                    raise SameContact
            else:
                raise EmptyField

        except EmptyField:
            return EmptyField

        except SameContact:
            return SameContact

        
    @classmethod
    def search_with_number(cls, number):
        for person in cls.__list_of_contacts:
            if person.phonenumber == number:
                return person.show_info()

        return None


    @classmethod
    def search_with_name(cls, name):
        for person in cls.__list_of_contacts:
            if person.fullname == name:
                return person.show_info()
                
        return None


    @classmethod
    def delete_contact(cls, number):
        massage = "Phonenumber Not Foud"

        if not number.isdigit():
            return InvalidNumber
        
        for person in cls.__list_of_contacts:
            if person.phonenumber == number:
                cls.__list_of_contacts.remove(person)
                cls.write_final_list_in_file()
                massage = "Phonenumber Deleted Successfully"
                
        return massage

    
    @classmethod
    def get_list(cls):
        return cls.__list_of_contacts

    
    @classmethod
    def write_final_list_in_file(self):
        with open("database.txt", 'w') as writer:
            for person in Phonebook.__list_of_contacts:
                writer.write(f"{person()}\n")
            


class file:
    def __init__(self):
        pass
        

    @classmethod
    def read_from_file(self):
        with open("database.txt", 'a+') as reader:
            reader.seek(0)
            for line in reader.readlines():
                name, number, email = map(str,line.split())
                person = Contact(fullname= name, phonenumber= number, email= email)
                Phonebook.add_to_list(person)


    @classmethod
    def write_in_file(self, person):
        with open("database.txt", 'a') as writer:
            writer.write(f"{person()}\n")


    

            