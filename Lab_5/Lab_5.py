import numpy as np
import random

print(np.__version__)

#განსაზღვრეთ 36 ელემენტიანი შემთხვევით [0, 100] შუალედიდან მთელ რიცხვთა 1
#განზომილებიანი, 2 განზომილებიანი და 3 განზომილებიანი numpy მასივები და
#დაბეჭდეთ.

matrix1 =np.random.randint(100, size=(1,36))
matrix2 =np.random.randint(100, size=(2,18))
matrix3 =np.random.randint(100, size=(3,12))
print(matrix1)

#numpy-ის საშუალებით ააგეთ მიმატება, გამოკლება, გამრავლება, გაყოფა ოპერაციები
#ორ რიცხვზე.

newarr1 = np.add(10, 2)
newarr2 = np.subtract(10, 2)
newarr3 = np.multiply(10, 2)
newarr4 = np.divide(10, 2)


#განსაზღვრეთ ორი 12 ელემენტიანი შემთხვევით [0, 100] შუალედიდან numpy
#მასივები, იპოვეთ შიდა, გარე და ჯვარედინი ნამრავლი.

arr1 =np.random.rand(100,12)
arr2 =np.random.randint(100, size=(1,12))

arr = np.array(np.random.randint(100, size=(1,3)), ndmin=1)
arr11 = np.array(np.random.randint(100, size=(1,3)), ndmin=1)
arr1 = arr.reshape(-1)
arr2 = arr11.reshape(-1)
print(arr1)
print(arr2)
x = [3, 2, 6]
y = [3, 1, 7]
print(arr1)
np.cross(arr1,arr2)
print(np.cross(x,y))
