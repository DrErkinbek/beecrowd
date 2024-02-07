val = int(input())
import math
notes100 = math.trunc(val / 100)
notes50  = math.trunc(val % 100 / 50)
notes20  = math.trunc(val % 100 % 50 / 20)
notes10  = math.trunc(val % 100 % 50 % 20 / 10)
notes5   = math.trunc(val % 100 % 50 % 20 % 10 / 5)
notes2   = math.trunc(val % 100 % 50 % 20 % 10 % 5 / 2)
notes1   = val % 100 % 50 % 20 % 10 % 5 % 2

print(val)
print(f'{notes100} nota(s) de R$ 100,00')
print(f'{notes50} nota(s) de R$ 50,00')
print(f'{notes20} nota(s) de R$ 20,00')
print(f'{notes10} nota(s) de R$ 10,00')
print(f'{notes5} nota(s) de R$ 5,00')
print(f'{notes2} nota(s) de R$ 2,00')
print(f'{notes1} nota(s) de R$ 1,00')