import random
import yaml

class PasswordMaker:
    fileext = ".yaml"
    filepath = "chars" + fileext
    
    chars:list = []
    password:str = ""
    length:int = 0

    def __init__(self, length:int):
        self.reload_chars()
        self.length = length

    def reload_chars(self):
        self.chars = []
        with open(self.filepath) as file:
            content = yaml.safe_load(file)
            self.chars = content["chars"]

    def generate(self):
        newpass:str = ""

        for i in range(self.length):
            newpass += random.choice(self.chars)
        
        self.password = newpass