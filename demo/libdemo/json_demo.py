import json


def dict_to_contact(d):
    return Contact(d["name"], d["phone"], d["email"])


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email}"


c = Contact("Srikanth", "9059057000", "srikanth@srikanthtechnologies.com")
jsonstr = json.dumps(c.__dict__)
print(jsonstr)

dict = json.loads(jsonstr)
c2 = dict_to_contact(dict)
print(c2)


