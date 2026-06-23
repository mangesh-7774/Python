mobile = {
  "category":"mobile",
  "prod_name":["Iphone","oppo","vivo"],
  "price":[100000,50000,40000]
}

for i in range(len(mobile["prod_name"])):
  print("Category : ",mobile["category"])
  print("Product Name : ",mobile["prod_name"][i])
  print("Price : ",mobile["price"][i])
  print()