def min_max(str1):
    list_a = [int(i) for i in str1.split()]
    min1 = min(list_a)
    max1 = max(list_a)
    list_a[list_a.index(min1)] = max1
    list_a[list_a.index(max1)] = min1
    return " ".join([str(i) for i in list_a])

if __name__ == "__main__":
    print(min_max("3 4 5 2 1"))
    