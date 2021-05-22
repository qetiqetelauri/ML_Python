#ჩაწერეთ data.xlsx ექსელის ფაილის „sheetOne“ ფურცელზე 100 მონაცემი (100 სტრიქონი).
# პირველ სვეტში ჩაწერეთ ათი სიმბოლოსგან შემდგარი შემთხვევითი სტრიქონი;
# მეორე სვეტში ჩაწერეთ შემთხვევითი რიცხვები [0, 10] შუალედიდან;
# მესამე სტრიქონში ჩაწერეთ შემთხვევითი რიცხვები [1, 7] შუალედიდან;
# მეოთხე სტრიქონში ჩაწერეთ შემთხვევითი განსხვავებული რიცხვები [1, 100] შუალედიდან.

import pandas as pd
import numpy as np
import random
import string

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))
list1=[]
for a in range(100):
  list1.append(randStr())

print(list1)

df1=pd.DataFrame(list1,columns=["A"])
df2 = pd.DataFrame(np.random.randint(low = 0,high=10,size=100),columns=["B"])
df3 = pd.DataFrame(np.random.randint(low = 1,high=8,size=100),columns=["C"])
df4 = pd.DataFrame(random.sample(range(0, 100), 100),columns=["D"])


frames = [df1, df2, df3,df4]
result = pd.concat(frames,axis=1)
print(result)
writer = pd.ExcelWriter('data.xlsx')

result.to_excel(writer, sheet_name='sheetOne', index=False)



#დაამატეთ data.xlsx ექსელის ფაილის „sheetTwo“ ფურცელზე 50 მონაცემი (50 სტრიქონი).
# პირველ სვეტში ჩაწერეთ განსხვავებული რიცხვები [1, 100] შუალედიდან.
# მეორე სვეტში ჩაწერეთ შემთხვევით სახელები (სახელი შეარჩიეთ წინასწარ გასზაღვრული მასივიდან);
# მეორე სვეტში ჩაწერეთ შემთხვევით გვარები (გვარი შეარჩიეთ წინასწარ გასზაღვრული მასივიდან);
# მეოთხე სტრიქონში ჩაწერეთ შემთხვევითი რიცხვები [2000, 5000] შუალედიდან.
def randStr1(chars = string.ascii_uppercase + string.digits, N=random.randint(2,10)):
	return ''.join(random.choice(chars) for _ in range(N))
RandomNames1=[]
for a in range(50):
  RandomNames1.append(randStr1())

RandomLastNames1=[]
for a in range(50):
  RandomLastNames1.append(randStr1())

df22=pd.DataFrame(RandomNames1,columns=["B"])
df23=pd.DataFrame(RandomLastNames1,columns=["C"])
df24 = pd.DataFrame(np.random.randint(low = 2000,high=5000,size=50),columns=["D"])
df21 = pd.DataFrame(random.sample(range(0, 100), 50),columns=["A"])

frames = [df21, df22, df23,df24]
result = pd.concat(frames,axis=1)
print(result)

result.to_excel(writer, sheet_name='sheetTwo', index=False)
writer.save()


#წაიკითხეთ data.xlsx ექსელის ფაილის ყველა ფურცელი და გადაწერეთ მონაცემები datanew.xlsx ფაილში.

data3 = pd.read_excel('data.xlsx')
print(data3)
writer1 = pd.ExcelWriter('data.xlsx')





