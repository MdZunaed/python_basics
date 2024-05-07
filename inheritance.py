class ParentClass:
    house = "5 floor"
    land = "100 sq/feet"
    business = "dollar business"

class ParentClassTwo:
    car = "BMW"
    bike = "Suzuki"


class ChildClass(ParentClass):
    job = "private job"

parent = ParentClass()
child = ChildClass()

print(child.land)
print(child.house)


########## Multiple Inheritance #################

class ChildClassTwo(ParentClass, ParentClassTwo):
    nothing = "Nothing"
    
childTwo = ChildClassTwo()
print(childTwo.land)
print(childTwo.bike)


########## Multi-level Inheritance #################

class ChildClassThree(ChildClass):
    nothing = "Nothing"
    
childThree = ChildClassThree()
print(childThree.job)
print(childThree.business)