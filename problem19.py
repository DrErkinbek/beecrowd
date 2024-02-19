val = int(input())
hours = int(val / 3600)
minutes = int((val % 3600) / 60)
seconds = (val % 3600) % 60
print(f'{hours}:{minutes}:{seconds}')