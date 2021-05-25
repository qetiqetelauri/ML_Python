import mysql.connector
import numpy
from scipy import stats
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

#დაადგინეთ სქესის მიხედვით რომელი მომხარებელი მეტი;
mycursor.execute("SELECT * FROM persons WHERE Gender='male'")

row=mycursor.fetchall()
male=mycursor.rowcount

mycursor.execute("SELECT * FROM persons WHERE Gender='female'")
row=mycursor.fetchall()
female=mycursor.rowcount

print(male,female)

if(male>female):
    print("male არის მეტი")
elif(female>male):
    print("female არის მეტი")
else:
    print("ტოლია")

#2) დაადგინეთ რამდენი მომხარებელია 30 წელზე ნაკლები;
mycursor.execute("SELECT  TIMESTAMPDIFF(YEAR, Date, CURDATE()) FROM persons WHERE  TIMESTAMPDIFF(YEAR, Date, CURDATE())< 30")

row=mycursor.fetchall()

print(mycursor.rowcount)
#3) დაადგინეთ ასაკის საშუალო მონაცემი, მოდა, მედეა, საშუალო კვადრატული გადახრა;
mycursor.execute("SELECT  TIMESTAMPDIFF(YEAR, Date, CURDATE()) FROM persons ")

row=mycursor.fetchall()

print(mycursor.rowcount)
mean = numpy.mean(row)
median = numpy.median(row)
mode = stats.mode(row)
std=numpy.std(row)

print(mean,median,mode,std)

#4) რომელ ასაკზე ნაკლებია მომხარებლების 70%;
x = numpy.percentile(row, 70)

print(x)
#5) რომელ ასაკზე ნაკლებია მომხარებლის 87%;
x = numpy.percentile(row, 87)

print(x)
#6) დაადგინეთ ყელაზე ხშირად რა რომელი ეროვნების მომხარებელი გვხვდება
mycursor.execute("SELECT Nationality,COUNT(*) FROM persons GROUP BY Nationality ORDER BY COUNT(*) DESC LIMIT 1")
row=mycursor.fetchall()
for r in row:
    print(r)
#7) დაადგინეთ სახელებში სიმბოლოების რაოდენობის საშუალო არითმეტიკული;


mycursor.execute("SELECT CHAR_LENGTH(Name)FROM persons")
row=mycursor.fetchall()
mean = numpy.mean(row)
print(mean)
#8) საშუალოდ რამდენი შვილი ყავს არამწეველ მომხარებელს;
mycursor.execute("SELECT COALESCE(Children, 0) AS Children FROM persons WHERE Smoke='no'")
row=mycursor.fetchall()
mean = numpy.mean(row)
print(mean)
#9) საშუალოდ რამდენი შვილი ყავს არამწეველ ქალბატონ მომხარებელს;
mycursor.execute("SELECT COALESCE(Children, 0) AS Children FROM persons WHERE Smoke='no' AND Gender='female'")
row=mycursor.fetchall()
mean = numpy.mean(row)
print(mean)
#10) საშუალოდ რა ასიკაა ქალბატონი მწეველი მომხარებლები.
mycursor.execute("SELECT TIMESTAMPDIFF(YEAR, Date, CURDATE()) As Age FROM persons WHERE Smoke='yes' AND Gender='female'")
row=mycursor.fetchall()
mean = numpy.mean(row)
print(mean)