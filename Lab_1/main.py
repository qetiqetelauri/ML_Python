# 2 Task

a=int(input("enter number:"))

print(bin(a))

# 4 Task

a=int(input("enter number I:"))
b=int(input("enter number II:"))
c=int(input("enter number III:"))

print((a+b+c)/3)


# 7 Task

a=int(input("Enter number: "))

if a%10==0:
    print("რიცხვი ბოლოვდება 0 ით")
else:
    print("რიცხვი არ ბოლოვდება 0 ით ")

# 10 Task

a=int(input("Enter year: "))

if a%4==0:
    if a%100==0 and a%400!=0:
        print("წელი არ არის ნაკიანი")
    else:
        print("წელი არის ნაკიანი")

else:
    print("წელი არ არის ნაკიანი")

# 11 Task

for x in range(20,125):
    if x%5==0:
        print(x)


# 14 Task
s=0
for x in range(10):
    a=int(input("enter number: "))
    s=s+a
print(s/10)


# 21 Task


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


a=int(input("enter number I:"))
b=int(input("enter number II:"))
print(gcd(a,b))


# 24 Task
number=int(input("enter number I:"))
for i in range(1, number + 1):
  if number % i == 0:
    print(i)


# 24 Task

for num in range(2, 100):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# 28 Task
number=input("enter number :")
print(len(number))

# 31 Task

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
