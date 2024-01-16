
print("Hello World!")
a = 3
b = 4
c = a + b
print(c/(a*b))
mas = []

mas.append(a)
mas.append(mas[-1] + b)
print(mas[-1])

mas.append(mas)
mas.append(1)
print(mas[-2])