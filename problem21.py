val = float(input())
import math
hundred = math.trunc(val / 100)
fifty = math.trunc(val % 100 / 50)
twenty = math.trunc(val % 100 % 50 / 20)
ten = math.trunc(val % 100 % 50 % 20 / 10)
five = math.trunc(val % 100 % 50 % 20 % 10 / 5)
two = math.trunc(val % 100 % 50 % 20 % 10  % 5 / 2)
coin_1 = math.trunc(val % 100 % 50 % 20 % 10  % 5 % 2)
rest = math.trunc((val - math.trunc(val)) * 100)
coin_50 = math.trunc(rest / 50)
coin_25 = math.trunc(rest % 50 / 25)
coin_10 = math.trunc(rest % 50 % 25 / 10)
coin_05 = math.trunc(rest % 50 % 25 % 10 / 5)
coin_01 = math.trunc(rest % 50 % 25 % 10 % 5)
print(f'NOTAS:\n{hundred} nota(s) de R$ 100.00\n{fifty} nota(s) de R$ 50.00\n{twenty} nota(s) de R$ 20.00\n{ten} nota(s) de R$ 10.00\n{five} nota(s) de R$ 5.00\n{two} nota(s) de R$ 2.00\nMOEDAS:\n{coin_1} moeda(s) de R$ 1.00\n{coin_50} moeda(s) de R$ 0.50\n{coin_25} moeda(s) de R$ 0.25\n{coin_10} moeda(s) de R$ 0.10\n{coin_05} moeda(s) de R$ 0.05\n{coin_01} moeda(s) de R$ 0.01')