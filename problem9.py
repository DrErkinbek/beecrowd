prod1Elems = input().split()
prod2Elems = input().split()

prod1Quantity = int(prod1Elems[1])
prod1Price = float(prod1Elems[2])
prod2Quantity = int(prod2Elems[1])
prod2Price = float(prod2Elems[2])
total = (prod1Quantity * prod1Price) + (prod2Quantity * prod2Price)
print("VALOR A PAGAR: R$ {:.2f}".format(total))