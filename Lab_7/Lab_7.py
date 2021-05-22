import mysql.connector
import random
import string
import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="myML"
)


mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE myML")

#mycursor.execute("CREATE TABLE persons (Id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(30),Lastname VARCHAR(30),Date DATE,Gender VARCHAR(20), Nationality VARCHAR(50), Smoke VARCHAR(20), Children INT, Reg_Date DATE, Email VARCHAR(30),Password VARCHAR(50) )")
def randStr(chars = string.ascii_uppercase + string.digits,N=random.randint(5,20)):
	return ''.join(random.choice(chars) for _ in range(N))


def getData(start,end):
  start_date = datetime.date(start, 1, 1)
  end_date = datetime.date(end, 2, 1)

  time_between_dates = end_date - start_date
  days_between_dates = time_between_dates.days
  random_number_of_days = random.randrange(days_between_dates)
  return start_date + datetime.timedelta(days=random_number_of_days)



genderList=['male','female',None]
NationalityList=['georgian', 'armenian', 'azerbaijanian']
SmokerList=['yes','no','']
ChildrenList=[1,2,3,4,5,6,7,8,9,None,'Other']
EmailList=['@gmail.com', '@yahoo.com', '@mail.ru)']

def InsertFun(N):
  sql = "INSERT INTO persons (Name, Lastname,Date,Gender,Nationality,Smoke,Children,Reg_Date,Email,Password) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
  for i in range(N):
    data1=getData(1980,2000)
    gend=genderList[random.randint(0,2)]
    Nat=NationalityList[random.randint(0,2)]
    smok=SmokerList[random.randint(0,2)]
    child=ChildrenList[random.randint(0,10)]
    data2 = getData(2018, 2020)
    email=randStr()+EmailList[random.randint(0,2)]
    val = (randStr(),randStr(),data1,gend,Nat,smok,child,data2,email,randStr())
    mycursor.execute(sql, val)

InsertFun(5000)
mydb.commit()