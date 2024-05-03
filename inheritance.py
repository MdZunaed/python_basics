class ParentClass:
    house = "5 floor"
    land = "100 sq/feet"
    business = "dollar business"


class ChildClass(ParentClass):
    job = "private job"

parent = ParentClass
child = ChildClass

print(child.land)
print(child.house)
