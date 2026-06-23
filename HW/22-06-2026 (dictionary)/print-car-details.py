car = {
  'name':'Car',
  'price':5000,
  'qty':5,
  'colour':["black","blue"],
  'model':["mo1","mo2"]
}


for i in range(len(car["colour"])):
  print("Name : ",car['name'])
  print("Price : ",car['price'])
  print("Quantity : ",car['qty'])
  print("Colour : ",car['colour'][i])
  print("Model : ",car['model'][i])
  print()