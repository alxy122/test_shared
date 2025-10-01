class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"

    def info(self) -> str:
        return f"This is an animal named {self.name}."
