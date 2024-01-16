
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
print(mas)
for i in range(10):
    mas[-i-1].append(i)
print(mas)