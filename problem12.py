elems = input().split()
a = int(elems[0])
b = int(elems[1])
s = int(elems[2])
M = (a + b + a*b*s*(a-b)) / 2
print(f'{M} eh o maior')