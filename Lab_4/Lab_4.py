import numpy as np

#3 შეიყვანეთ სტრიქონი. დაითვალეთ რამდენჯერ შეგხვდათ სიმბოლო “a” დაბეჭდეთ შედეგი.

a3=input("enter string")
print(a3.count('a'))

#5text ცვლადს მიანიჭეთ სტრიქონი “სწავლის ძირი მწარე არის, კენწეროში გატკბილდების”.
#სტრიქონიდან წაიკითხეთ პირველი 20 სიმბოლო და დაბეჭდეთ შედეგი. დაითვალეთ
#რამდენჯერ არის ნახსენები სიმბოლო ‘ს’.

a5="სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
ans5=a5[0:20]
print(ans5,ans5.count("ს"))

#11text ცვლადს მიანიჭეთ შემდეგი ტექსტი: “Have a nice day”. დაბეჭდეთ ტექსტის
#თითოეული სიმბოლო ეკრანზე უკუ მიმართულებით ცალ-ცალკე ხაზზე (ანუ პირველად
#დაბეჭდავ ბოლო სიმბოლოს, შემდეგ ბოლოს წინა სიმბოლოს, და ა.შ).

text="Have a nice day"
print(text[::-1])

#13. დაწერეთ პროგრამა, სადაც user შეიყვანს თავის სახელს და გვარს და პროგრამა
#დაუბეჭდავს შესაბამის იმეილის დასახელებას: მაგ: adam.giorgadze@edu.ge
firstName=input("firstName:")
LastName=input("LastName:")
print(firstName+'.'+LastName+"@edu.ge")

#15. მოახდინეთ ორი მატრიცის შეკრების მოდელირება. მოიყვანეთ ორი მაგალითი
#(შემთხვევითი და სტატიკური რიცხვებისთვის)
a = np.matrix('1 2; 3 4')
b = np.random.randint(10, size=(2, 2))
res=np.add(a,b)
print(a)
print(b)
print(res)

#17. მოახდინეთ ორი მატრიცის გამრავლების მოდელირება. მოიყვანეთ ორი მაგალითი
#(შემთხვევითი და სტატიკური რიცხვებისთვის)
a = np.matrix('1 2; 3 4')
b = np.random.randint(10, size=(2, 2))
res=np.matmul(a,b)
res1=a.dot(b)
print(a)
print(b)
print(res)
print(res1)

#19 შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. წაშალეთ
#კლავიატურიდან შეტანილი რიცხვი. გამოიყენეთ numpy ბიბლიოთეკა.
matrix = np.random.randint(10, size=(10, 10))
print(matrix)
matrix1=matrix.reshape(-1)
print(matrix1)
number=int(input("number"))
k1=matrix1[matrix1!=number]
print(k1)