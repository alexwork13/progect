

st1 = input("Enter first line: ")
st2 = input("Enter second line: ")


if st1.isdigit() and st2.isdigit():
    print((list(st1) + [str((sum([int(s) for s in list(st1)]) + sum([int(s) for s in list(st2)])))] + list(st2)))
else:
    print(st1 + " " + st2)




