class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(self.name, "は大人です。")
        else:

            print(self.name, "は大人ではありません。")

human = [
    Human("太郎", 20),
    Human("花子", 19),
    Human("次郎", 34),
    Human("三郎", 5)
]

num = 0

for i in human:
    human[num].check_adult()
    num += 1
