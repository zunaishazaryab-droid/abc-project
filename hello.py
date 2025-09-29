a=123455
print(type(a))
b="zunaisha"
print(type(b))
c=12.23
print(type(c))
d=True
print(type(d))

marks=int(input("enter your overall marks percentage:"))
cs_marks=int(input("enter overall cs_marks percentage:"))
if marks>=88 or cs_marks>=88:
    print("you are eligible for admission")
else:
    print("you are not eligible for admission")

marks=int(input("enter your marks:"))
print(type(marks))
if marks >=90:
    print("your garde is A")
elif marks >=80:
    print("your grade is B")
elif marks >=70:
    print("your grade is C")
else:
    print("your grade is D")


year=int(input("enter the year"))
print(type(year))
if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
     print("not leap year")

import random
randint=random.randint(1,10)
print(randint)


randfloat=random.random()
print(randfloat)

random23=random.randint(0,1)
if random23==1:
     print("head")
else:
     print("tail")


student1=88
student2=88
student3=88
studentmarks=[23,56,76,56,45,43]
print(studentmarks[-3])
print(len(studentmarks)-2)


name=["zunaisha","zaryab"]
for n in name:
    print(n)

numbers=[1,2,3,4,5,6,7,8,9]
for n in numbers:
    print(n)


sum=0
for n in range(1,101):
    sum=sum+n
print(sum)

even_no=0
for n in range(2,100,2):
    print(n)
    even_no=even_no+n
print(even_no)

odd_no=0
for n in range(1,100,2):
    print(n)
    odd_no=odd_no+n
print(odd_no)

def addnumber():
    print("add number")
    print("this is a addnumber function")
def totalnum(num1, num2,num3,num4):
    addtotal=num1+num2+num3+num4
    return addtotal
result=totalnum(1,2,3,4)
print(result)


class Car:
    name="BMW"
    color="black"
    wheels=4
    def forward(self):
        print("car is about to be forwarded")
obj=Car()
obj.forward()
print(obj.name)
print(obj.color)
print(obj.wheels)

marks=[20,40,50,69,60]
max_marks=max(marks)
print("marks")
print(max_marks)

marks=[12,34,56,78,78]
min_marks=min(marks)
print("marks")
print(min_marks)




