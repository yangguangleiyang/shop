#print("hello world")

'''age_of_princal = 56
guess_age = int(input("your age:"))
if guess_age == age_of_princal:
    print("yes")
else:
    print("it's wrong")
#----------------------------------
age = 50
flag = True #True和False必须大写
while flag:
    user_age = int(input("请输入您的年龄："))
    if user_age == age:
        print("yes")
        flag = False
    elif user_age > age:
        print("it is bigger")
    elif user_age < age:
        print("it is smaller")
print("end")
#也可以这样写： 使用break
age = 50

while True:
    user_age = int(input("请输入您的年龄："))
    if user_age == age:
        print("yes")
        break
    elif user_age > age:
        print("it is bigger")
    elif user_age < age:
        print("it is smaller")
print("end")


num = 1
while num < 100:
    if num%2 == 1:
        print(num)
    num += 1
'''

num = 1
while num < 10:
    num += 1
    if num == 3:
        continue
    print(num)