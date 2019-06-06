file = open("count.txt","r+")
count = {}
for word in file.read().split():
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

for item in count.items():
    print("{}\t{}".format(*item),file=open("output.txt", "a"))
file.close();