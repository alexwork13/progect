

def find_two_smallest(L):
    smallest = min(L)
    
    min1 = L.index(smallest)
    L.remove(smallest) # удаляем первый минимальный элемент
    print(L)
    
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    L.insert(min1, smallest) # возвращаем первый минимальный обратно
    print(L)
    if min1 <= min2: # проверяем индекс второго минимального из-за смещения
        min2 += 1 # min2 = min2 + 1
    return (smallest, next_smallest) # возвращаем кортеж


print(find_two_smallest([44, 2, 46, 4, 67, 6]))