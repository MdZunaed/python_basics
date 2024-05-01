# Python Data Types

stringType = "Zunayed"
integerType = 450197
floatType = 3.64
booleanType = True
listType = ['mango', 'banana']
tupleType = ('abir', 'shaon')
setType = {3,3,3,5,8, 12, 12, 14}
dictionaryType = {'name': "Zunayed", 'roll': 450197, 'male': True}

########## List ##########

# list is mutable(changable), ordered, []
# listType.append('apple')
# listType.insert(1,'orange')
# listType.remove('mango')
# listType.reverse()
# print(listType.count)

########## Tuple ##########

# tuple is immutable(not changable), ordered, able to duplicate ()
# listFromTuple= list(tupleType)
# listFromTuple.append('johan')
# tupleType = listFromTuple
# print(tupleType)

########## Set ##########

# set is mutable(changable), unordered, doesn't allow duplicate {}
# setTwo = {2,4,6,12}
# setType.add(50)
# setType.remove(8)
# setTwo.update(setType)
# print(setType)
# print(setTwo)

########## Dictionary ##########

# dictionary is key value pair, mutable(changable), doesn't allow duplicate 'key'{'key': 'value'}

print(dictionaryType)
print(dictionaryType['name'])
dictionaryType['roll'] = 1
print(dictionaryType)
dictionaryType['result'] = 4.85
print(dictionaryType)
dictionaryType.pop('male')
print(dictionaryType)




