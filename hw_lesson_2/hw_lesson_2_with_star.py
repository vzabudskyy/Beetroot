"""
1.  на форматування. Зробіть форматування так щоб отримати ось таке

"000012 Василий 110110 32.10"

заповніть ___ , майте на увазі 110110 - це бінарний формат.

print("____________________".format(12, "Василий", 54, 32.1))
"""

print("{0:0>6} {1} {2:b} {3:.2f}".format(12, "Василий", 54, 32.1))


"""
2. Спробуйте "зібрати" зі слова "Корован" слово "ворона". Використайте слайсінг та вашу фантазію. 

s1 = "Корован"

print(s1[4]+s1[1]+s1[2] +...  <-   можлиіий але не самий цікавий варіант.
"""

s1 = "Корован"
print(s1[-3:-7:-1]+s1[-1:-3:-1])
