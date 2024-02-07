elems = input().split()
a = int(elems[0])
b = int(elems[1])
s = int(elems[2])
max1 = (a+b+abs(a-b))/2
max2 = (s+max1 + abs(s-max1))/2
print(f'{round(max2)} eh o maior')