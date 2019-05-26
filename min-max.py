def min_max(str1):
    list_a = [int(i) for i in str1.split()]
    min1 = min(list_a)
    max1 = max(list_a)
    index1 = list_a.index(max1)
    index2 = list_a.index(min1)
    list_a[index1] = min1
    list_a[index2] = max1
    
    return " ".join([str(i) for i in list_a])

if __name__ == "__main__":
    print(min_max("3 4 5 2 1"))
    