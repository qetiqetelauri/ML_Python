import os
import math
#2 0-დან 100-მდე მთელი რიცხვები ჩაწერეთ data1.txt ფაილში. myFiles საქაღალდეში.


filename = "myFiles/data1.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    for x in range(0, 100):
        f.write(str(x)+ ' ')

#4. myFiles2 საქაღალდეში საქაღალდეში შექმენით 30 ფაილი, ფაილებში ჩაწერეთ სიტყვები  „Programmer2“ .... „Programmer30“.

filename = "myFiles2/Programmer"
for x in range(0, 30):
    filename = filename+str(x)+'.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("Programmer"+ str(x))

#7. დაწერეთ პროგრამა, რომელიც y=x^3+e^x  ფუნქციის მნიშვნელობებს დაითვლის [0; 2 ] შუალედში მეასედების სიზუსტით და შესაბამის მნიშვნელობებს ჩაწერს function.txt ფაილში myFiles საქაღალდეში.

filename = "myFiles/function.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    for x in range(0, 3):
        y=round(pow(x,3)+math.exp(x), 2)
        f.write(str(y)+' ')

#10.	შექმენით ლექსიკონი: {0: 10, 1: 20}. დაამატეთ 2 ახალი ელემენტი და დაბეჭდეთ მიღებული ლექსიკონი. (გამოიყენეთ update მეთოდიც). წაშალეთ რომელიმე ელემენტი.
dict = {
  0: 10,
  1: 20
}
dict.update({2: 30,3:40})
dict.pop(1)
print(dict)

#12.	დაწერეთ პროგრამა რომელიც შეამოწმებს რომელიმე key (გასაღები) არის თუ არა ლექსიკონში: d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} და დაბეჭდეთ შესაბამისი შეტობინება. (მითითება: გამოიყენეთ in ოპერატორი).
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

if 3  in d:
  print("არის")

#15.	შექმენით სიმრავლე შემდეგი ელემენტებით: 0, 1, 2, 3, 4. დაამატეთ ნებისმიერ 3 ელემენტი სურვილისამებრ. წაშალეთ ორი ელემენტი სიმრავლიდან. დაბეჭდეთ სიმრავლის ელემენტები ცალ-ცალკე ხაზზე (გამოიყენეთ for ციკლი). დაითვალეთ სიმრავლის ელემენტების რაოდენობა.

set1 = {0, 1, 2, 3, 4}
set1.update({7,34,56})
set1.remove(0)
print(len(set1))
for x in set1:
    print(x)

#18.	შექმენით tuple ტიპის ობიექტი, რომლის ელემენტებია 1-დან 100-მდე არსებული 5-ის ჯერადი რიცხვების კუბები. გამოიყენეთ for ციკლის მოკლე ჩაწერის ფორმა. შესაბამისი ფუნქციის გამოყენებით იპოვეთ tuple-ის სიგრძე (ელემენტების რაოდენობა).

a = []
for i in range (1,100):
    if i % 5==0:
        pow(i,3)
        a.append(i)
a = tuple(a)
print(a)
print(len(a))