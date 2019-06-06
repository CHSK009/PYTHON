n = int(input("How many  numbers  do you have? "))
lb =[]
kg=[]
for i in range(n):
    s = int(input("Enter a number  >> "))
    lb.append(s)
print(lb)

for i in lb:
    x=i/2.2046525820
    kg.append(x)
print(kg)


