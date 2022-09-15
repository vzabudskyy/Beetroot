"""
Task 1

Create a class method named `validate`, which should be called from the
`__init__` method to validate parameter email, passed to the constructor.
The logic inside the `validate` method could be to check if the passed
email parameter is a valid email string."""


class ContactInfo:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = self.validate(email)

    @staticmethod
    def validate(email):
        domain = email.split(".")[-1]
        if not all(i.isdigit() or i.isalpha() for i in email[::len(email)-1]):
            raise ValueError("Email should begins and ends with a letter or digit.")
        elif "@" not in email:
            raise ValueError("Email should contains '@'")
        elif 2 > len(domain) or "@" in domain:
            raise ValueError("Incorrect domain")
        else:
            for i in range(len(email)):
                if not email[i].isalpha() and not email[i].isdigit() and email[i] not in [".", "_", "-", "@"]:
                    raise ValueError
                elif email[i] in [".", "_", "-", "@"] and not all(j.isdigit() or j.isalpha() for j in email[i-1:i+2:2]):
                    raise ValueError

        return email


if __name__ == "__main__":
    test1 = ["abc-@mail.com", "abc..def@mail.com", ".abc@mail.com", "abc#def@mail.com"]  # incorrect address
    test2 = ["abc-d@mail.com", "abc.def@mail.com", "abc@mail.com", "abc_def@mail.com"]  # correct
    test3 = ["abc.def@mail.c", "abc.def@mail#archive.com", "abc.def@mail", "abc.def@mail..com"]  # incorrect domain
    sample = test1 + test2 + test3
    for index in range(len(sample)):
        try:
            c = ContactInfo("Vladyslav", "Zabudskyi", sample[index])
            print(f"Confirmed address: {c.email}")
        except ValueError:
            print(f"Wrong address: {sample[index]}")
