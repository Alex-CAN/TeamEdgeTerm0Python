
def getItemForPerson(name):
  item = input(f"What would you like to order {name}?: ")
  cost = input(f"How much does this {item} cost?: $")
  return item, float(cost)

def calculateTotal(cost):
  tip = input("How much would you like to tip?: $")
  tax = cost * float(0.1025)
  total = cost + tax + float(tip)
  return round(total, 2)

def printReceipt(name, item, cost, total):
  print(f"{name} you ordered {item} for ${cost}. Your total, with tax and tip included, is ${total}")
  
def getOrder():
  name = input("What is your name?: ")
  item, cost = getItemForPerson(name)
  total = calculateTotal(cost)
  printReceipt(name, item, cost, total)

getOrder()
getOrder()