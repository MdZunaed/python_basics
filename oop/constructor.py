class Man:
    # Constructor
    # def __init__(self, name, age):
    #     print(f"My  name is {name}, I'm {age}")

    # Instance Method
    def instanceMethod(self):
        print("This is Instance Method")

    # Class Method
    @classmethod
    def classMethod(cls):
        print("This is Class Method")

    # Class Method
    @staticmethod
    def staticMethod():
        print("This is Static Method")

# zunaed = Man("Zunaed", 21)
asif = Man()

asif.instanceMethod()

asif.classMethod()
Man.classMethod()

asif.staticMethod()
Man.staticMethod()