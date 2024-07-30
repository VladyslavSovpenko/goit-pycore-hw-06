from collections import UserDict

from models.record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data[name]

    def delete(self, name: str):
        del self.data[name]

    def __str__(self):
        output = ["AddressBook:"]
        for name, record in self.data.items():
            output.append(str(record))
        return "\n".join(output)
