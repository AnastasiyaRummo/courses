class User:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def get_first_name(self):
        return self.fname

    def get_last_name(self):
        return self.lname

    def get_info(self):
        return f"User: {self.fname} {self.lname}"
