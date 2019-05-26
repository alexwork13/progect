list_a = [int(i) for i in input().split()]
count = ""

for i in list_a:
    if list_a.count(int(i)) == 1:
        count += " " + str(i) 
print(count)
