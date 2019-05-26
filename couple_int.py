list_a = [int(i) for i in input("Enter: ").split()]
count = 0

for i in range(len(list_a)):
    for j in range(i + 1, len(list_a)):
        if list_a[i] == list_a[j]:
            count += 1

print(count)
