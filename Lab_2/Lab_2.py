import random
import statistics
#2
#a=int(input("Number 1:"))
#b=int(input("Number 2:"))
#=int(input("Number 3:"))

#print(max(a,b,c))

#6
count = 0
while count<10:
    print(random.randint(-100,100))
    count=count+1

#8
def func8(a,b):
    print((a+b)/2)
func8(1,2)
func8(5,7)
func8(4,2)

#11
def func11(a):
    if a%2==0:
        return False
    else:
        return True
print(func11(1))
print(func11(5))
print(func11(4))

#15
numbs = [5,7,11,24,4]
print("Sum - ",sum(numbs))
print("Min - ",min(numbs))
print("Max - ",max(numbs))
print("Avg - ",sum(numbs)/len(numbs))
numbs.append(102)
numbs.insert(2, 205)
numbs.pop(3)
numbs.sort()
print(numbs)

#19
def func19(a):
    for x in a:
        if x%2!=0:
            a.remove(x)
    print(a)


func19(numbs)

#21
list=[]
for x in range(10):
    list.append(random.randint(25,110))
print(list)

#24
random.shuffle(numbs)
print("shuffle ",numbs)

#27
list27=[1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
print("mode ",statistics.mode(list27))

#29
st="python php pascal javascript java c++"
list29=st.split()
print(list29)
print(max(list29, key=len))

#30
list=[]
list27=[1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
list27.sort()
print(sum(list27)/len(list27))
print(statistics.median(list27))
print(statistics.mode(list27))