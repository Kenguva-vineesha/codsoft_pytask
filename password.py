print("welcome to password generater😄")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','+','_']
l=int(input("how many letters would you like in password?\n"))
print()
s=int(input("how many symbols would you like?\n"))
print()
n=int(input("how many numbers would you like?\n"))
print()
import random
password=[]
for i in range(0,l):
   ch=random.choice(letters)
   password += ch
for i in range(0,s):
   ch=random.choice(symbols)
   password += ch
for i in range(0,n):
   ch=random.choice(numbers)
   password += ch
# print(password)
random.shuffle(password)
# print(password)
j=""
for i in password:
    j=j+i

print("your passwod is: ",j)
