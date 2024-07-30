from models.name import Name
from models.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        if phone not in self.phones:
            self.phones.append(Phone(phone))
        else:
            print(f'Phone {phone} already added.', )

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, requested):
        for phone in self.phones:
            if phone.value == requested:
                return phone

    def delete_phone(self, phone_to_delete):
        self.phones = [phone for phone in self.phones if phone.value != phone_to_delete]

    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"
