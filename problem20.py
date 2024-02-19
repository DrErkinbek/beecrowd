val = int(input())
years = int(val / 365)
months = int((val % 365) / 30)
days = (val % 365) % 30
print(f'{years} ano(s)\n{months} mes(es)\n{days} dia(s)')