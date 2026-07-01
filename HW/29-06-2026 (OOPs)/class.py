from datetime import datetime 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.units import inch




class Product:
  def __init__(self,name,brand,price,mfg,exp,qty):
    self.name=name
    self.brand=brand
    self.price=price
    self.qty=qty
    self.mfg=datetime.strptime(mfg,"%d-%m-%Y").date()
    self.exp=datetime.strptime(exp,"%d-%m-%Y").date()

prod_list = []
orders=[]

def add_product():
  name = input("Enter your product name : ")
  brand = input("Enter your product brand : ")
  price = int(input("Enter price : "))
  qty = int(input("Enter product quantity : "))
  mfg = input("Enter manufacturing date (DD-MM-YYYY) : ")
  exp = input("Enter expiry date (DD-MM-YYYY) : ")

  name = Product(name,brand,price,mfg,exp,qty)

  prod_list.append(name)

def display_all_products():
  print("\nAll Products : \n")
  print("Product_Name\tBrand\tPrice\tQuantity\tM.F.G.\t\tExpiry")
  print("--------------------------------------------------------------------------------------")
  for i in prod_list:
    
    print(f"{i.name}\t\t{i.brand}\t{i.price}\t{i.qty}\t\t{i.mfg}\t{i.exp}")


def search_products():
    search_found=False
    ip = input("Search product by name , brand or price : ")
    print("\nProduct_Name\tBrand\tPrice\tQuantity\tM.F.G.\t\tExpiry")
    print("--------------------------------------------------------------------------------------")

    if len(prod_list) == 0 :
        print("There is no products found in list to filter")
        return

    for i in prod_list:
        if i.name == ip or i.brand == ip or str(i.price) == ip:
            print(f"{i.name}\t\t{i.brand}\t{i.price}\t{i.qty}\t\t{i.mfg}\t{i.exp}")
            search_found=True 

    if search_found == False :
        print("There is no products matched to your search")
        
        
def purchase_products():
    found = False
        
    while True:
        if len(prod_list) == 0:
            print("There is no item in system to purchase")
            return

        display_all_products()

        print("\nPurchase your products from above products...!\n")
        ip = input("Enter product name : ")

            
        for item in prod_list:
            if item.name == ip :
                found = True
                units = int(input("Enter quantity you want to buy : "))
                if units>0 and units <= item.qty :
                    orders.append({
                        "name":item.name,
                        "brand":item.brand,
                        "price":item.price,
                        "quantity":units,
                        "total":item.price * units
                    })
                    item.qty -= units
                else :
                    print("Invalid quantity...!") 

        if found == False : 
            print("Invalid product name") 

        again = int(input("\nDo you want to purchace another item - press 1 (if yes) otherwise press 2 : "))   

        if again != 1 :
            break
       
              
def bill():
    if len(orders) == 0 :
        print("\nYou dont have purchesed any item yet...!")
        return

    subtotal = 0
    print("\nYour purchased products are : \n")
    print("Product\tBrand\tPrice\tQuantity\tTotal")
    print("--------------------------------------------------------------------------------------")
    for item in orders:
        print(f"{item['name']}\t\t{item['brand']}\t{item['price']}\t{item['quantity']}\t{item['total']}")
        subtotal += item["total"]

    cgst = subtotal * 0.06   
    sgst = subtotal * 0.06 
    final_total = subtotal + cgst + sgst 

    print("--------------------------------------------------------------------------------------\n\n\n")

    print(f"SubTotal : {subtotal}") 
    print(f"CGST : {cgst}")
    print(f"SGST : {sgst}")
    print("---------------------------------")
    print(f"Final Bill : {final_total}")

    choice =  int(input("Do you want to generate pdf of your bill if yes - (press 1) itherwise (press 2) : "))

    if choice == 1:
        generate_pdf()
    
            
      
def generate_pdf():
    if len(orders) == 0:
        print("No orders found to geenerate PDF")
        return
    
    pdf = SimpleDocTemplate("Invoice.pdf")

    elements = []

    styles = getSampleStyleSheet()

    title = Paragraph("Product Management")
    elements.append(title)

    elements.append(Spacer(1,0.25 * inch))

    data = [
        ["Product", "Brand", "Price", "Quantity", "Total"]
    ]

    subtotal = 0

    for item in orders:
        data.append([
            item["name"],
            item["brand"],
            str(item["price"]),
            str(item["quantity"]),
            str(item["total"])
        ])
        subtotal += item["total"]

    cgst = subtotal * 0.06
    sgst = subtotal * 0.06
    final_total = subtotal + cgst + sgst

    data.append(["","","","Subtotal",f"{subtotal}"])
    data.append(["","","","CGST",f"{cgst}"])
    data.append(["","","","SGST",f"{sgst}"])
    data.append(["","","","Final Bill",f"{final_total}"])

    table = Table(data)

    table.setStyle(TableStyle([

        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),

        ('ALIGN', (0,0), (-1,-1), 'CENTER'),

        ('GRID', (0,0), (-1,-1), 1, colors.black),

        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),

        ('BOTTOMPADDING', (0,0), (-1,0), 10),

        ('BACKGROUND', (0,1), (-1,-1), colors.beige)

    ]))
     
    elements.append(table)

    elements.append(Spacer(1,0.3 * inch))

    thank = Paragraph(
        "<b>Thank You For Shopping With Us!</b><br/>Visit Again...!",
        styles["Heading2"]
    )

    elements.append(thank)

    # Build PDF
    pdf.build(elements)

    print("\nInvoice.pdf generated successfully!")



  
    

print("\n------------------------------------- Products Management -------------------------------")

while(True):
  print("\n1.Add Products \n2.Display All \n3.Search Product \n4.Purchase Product \n5.Bill \n6.Exit\n")

  choice = int(input("Enter your choice : "))

  match choice:
       case 1:
           add_product()
       case 2:
           display_all_products()
       case 3:
           search_products()
       case 4: 
           purchase_products()
       case 5:
           bill()
       case 6:
           print("Exit")
           break
       case _ :
           print("Invalid choice, please try with valid choice...!")
  

