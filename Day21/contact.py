# contact.py

class Contact:
    def __init__(self, name, phone, email, city):
        self.name = name
        self.phone = phone
        self.email = email
        self.city = city

    def to_dict(self):
        """Convert contact to dictionary for CSV saving"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "city": self.city
        }

    def __str__(self):
        return (f"Name  : {self.name}\n"
                f"Phone : {self.phone}\n"
                f"Email : {self.email}\n"
                f"City  : {self.city}")
