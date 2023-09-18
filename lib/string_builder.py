class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, my_string):
        self.str += my_string

    def size(self):
        return len(self.str)

    def output(self):
        return self.str