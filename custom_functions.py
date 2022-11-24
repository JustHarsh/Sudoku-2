class Input_manipulation:

    def __init__(self, string) -> None:
        self.string = string

    def fstrip(self, string):
        return string.replace(" ", "")
