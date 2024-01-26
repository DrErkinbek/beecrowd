values = input().split()
A = float(values[0])
B = float(values[1])
C = float(values[2])

area_triangle = A * C / 2
area_circle = 3.14159 * C * C
area_trapezium = 1/2 * C * (A + B)
area_square = B * B
area_rectangle = A * B

print('TRIANGULO: {:.3f}'.format(area_triangle))
print('CIRCULO: {:.3f}'.format(area_circle))
print('TRAPEZIO: {:.3f}'.format(area_trapezium))
print('QUADRADO: {:.3f}'.format(area_square))
print('RETANGULO: {:.3f}'.format(area_rectangle))