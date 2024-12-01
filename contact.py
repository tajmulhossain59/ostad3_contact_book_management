class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @staticmethod
    def from_dict(data):
        try:
            return Contact(data["name"], data["phone"], data["email"])
        except KeyError as e:
            print(f"Error: Missing field {e} in contact data.")
            return None
