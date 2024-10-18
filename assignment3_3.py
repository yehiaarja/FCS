class item:
    def __init__(self,barcode,name,price):
        self.barcode = barcode
        self.name = name
        self.price = price

items = {
"001": item("001","Snickers",price =10),
"002": item("002","Twix",price =7),
"003": item("003","Chips",price = 5),
"004": item("004","Pepsi",price=3.5)
}

def display_receipt(receipt):
    total = 0
    print("--Receipt--")
    for item in receipt:
            item_total = item["quantity"]*item["price"]
            total = total + item_total
            print(f"{item["name"]}: {item["price"]}$,{item["quantity"]} = {item_total}$")
    print(f"Total: {total}$")
                  


 

def main():
    while True:
        receipt = []  
        add_receipt = input("do you want to start a new receipt?(y/n) ")
        if add_receipt != "y":
            print("exiting")
            break
        else:
            while True:
                barcode = input("add an item's barcode: ")
                if barcode in items:
                    item = items[barcode]
                    try:
                        quantity = int(input("item's quantity: "))
                    except ValueError:
                        print("invalid quantity(must be integer)")
                        continue
                    if item in receipt:
                        break
                    else:
                        receipt.append({
                            "name" : item.name,
                            "price" : item.price,
                            "quantity" : quantity
                            })
                else:
                    print("invalid barcode")
                    continue
                add_item = input("do you want to add another item?(y/n) ")
                if add_item != "y":
                    break
            display_receipt(receipt)

main()





       