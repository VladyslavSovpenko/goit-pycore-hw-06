from models.field import Field


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return self.value
