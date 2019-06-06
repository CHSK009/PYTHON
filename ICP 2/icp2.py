n = int(input("How many  numbers  do you have? "))
lb=[]
for i in range(n):
    s = int(input("Enter a number  >> "))
    lb.append(s)

print(lb)
kg = [(x/2.2046525820) for x in lb]
print(kg)