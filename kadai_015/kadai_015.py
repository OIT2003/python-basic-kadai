class Homan:
    def __init__(self):
        self.name = ""
        self.age = ""

    def set_info(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name)
        print(self.age)

info = Homan()

info.set_info("taro", 40)
info.printinfo()
