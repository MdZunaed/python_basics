
######### For loop #########

##for i in range(start,end,skip):

for i in range(1,11,2):
    print(i)

###### 1+2+3+4+5+....+100 = ?

sum = 0
for i in range(1,101):
    sum = sum+i #shortcut-> sum += 1
    print(sum)

###### 1+3+5+7+...+99 = ? 
## method 1:

sum = 0
for i in range(1,100, 2):
    sum = sum+ i
    print(sum)

## method 2:

sum = 0
for i in range(1,101):
    if i % 2 == 0:
        continue
    else:
        sum = sum + i
        print(sum)    

## method 3:

sum = 0
for i in range(1,101):
    if i % 2 != 0:
        sum = sum + i
        print(sum)

fruits = ["banana", "mango", "Apple"]

for item in fruits:
    print(item)    

######### While loop #########

## while condition:
#         statement
         
###### 1+3+5+7+...+99 = ? 

sum = 0
counter = 1
while counter <= 100:
    sum += counter
    counter += 1
print(sum)

