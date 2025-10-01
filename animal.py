class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"

    def info(self) -> str:
        return f"This is an animal named {self.name}."

    def sleep(self) -> str:
        return f"{self.name} is sleeping."
