import os
from datetime import datetime, timedelta
import time

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# this function only print data on previously generated/inputed data
def print_invoice(company_name="Acer inc", invoice_number = "___", gst_number="HST2346345",
                  bill_to="---", invoice_date="mm/dd/yyyy", due_date="mm/dd/yyyy",
                  subject="---", items=[["1","default item", "2", "100", "200"]], sub_total="0",
                  hst_total="0", total="0"
                  ):
    address = "12 Bell Street,"
    city = "Ottawa, ON 3f5 H3D"
    print("*"*100)
    print(company_name.upper().center(100, " "))
    print("*"*100)
    print("Company name & address:", company_name, end="")
    company_line_spaces_needed = 100 - (24 + len(company_name) + 16 + len(invoice_number))
    print(" " * company_line_spaces_needed, end="")
    print("Invoice Number:", invoice_number)
    address_line_spaces_needed = 100 - 23 - len(address)
    city_line_spaces_needed = 100 - 23 - len(address)
    print(" " * 23, address, " " * address_line_spaces_needed)
    print(" " * 23, city, " " * city_line_spaces_needed)
    print("Gst/HST No: ",gst_number, sep="", end="")
    gst_line_spaces_needed = 100 - 12 - len(gst_number) - 13 - len(total)
    print(" " * gst_line_spaces_needed, "Balance Due: ", total, sep="")
    [print(" " * 100) for _ in range(4)]
    print("Bill To: ",  bill_to, sep="", end="")
    bill_to_line_spaces_needed = 100 - 9 - len(bill_to) - 14 - len(invoice_date)
    print(" " * bill_to_line_spaces_needed, "Invoice date: ", invoice_date, sep="")
    print("Term: Custom".rjust(100, " "))
    print(" ".join(["Due Date:", due_date]).rjust(100, " "))
    print(" ".join(["P.O.", "1111"]).rjust(100, " "))
    [print(" " * 100) for _ in range(6)]
    print(" ".join(["Subject", subject]).ljust(100, " "))
    [print(" " * 100) for _ in range(2)]
    print(" ".join(["#         ", "Item"+" "*36,
                    "Qty       ", "Rate      ", "Amount    "]).ljust(100, " "))
    for item in items:
        print(" ".join([item[0].ljust(10, " "), item[1].ljust(40, " "),
                        item[2].ljust(10, " "), item[3].ljust(10, " "), item[4]]).ljust(100, " "))
    [print(" " * 100) for _ in range(6)]
    print(" ".join(["Sub Total: ", sub_total]).rjust(100, " "))
    print(" ".join(["HST(13%): ", hst_total]).rjust(100, " "))
    print(" ".join(["Total: ", total]).rjust(100, " "))
    print(" ".join(["Balance Due: ", total]).rjust(100, " "))

#function requests data from the used, needed to generate invoice
def print_invoice_menu(inventory_items):
    invoice_number = input("Enter invoice Number (OR '.exit' to exit): ")
    if invoice_number == ".exit":
        return 0
    bill_to = input("Enter bill to company (OR '.exit' to exit): ")
    if bill_to == ".exit":
        return 0
    subject = input("Enter invoice's subject (OR '.exit' to exit): ")
    if bill_to == ".exit":
        return 0
    entered_date = input("Enter invoice date in format mm/dd/yyyy").split("/")
    if entered_date == ".exit":
        return 0
    invoice_date = datetime(int(entered_date[2]), int(entered_date[0]), int(entered_date[1]))
    invoice_date_str = invoice_date.strftime('%m/%d/%Y')
    due_date = invoice_date + timedelta(days=15)
    due_date_str = due_date.strftime('%m/%d/%Y')
    items_count = 1
    items = []
    the_exit = 0
    while True:
        print("*" * 100)
        print_inventory_item_names(inventory_items)
        item_id = input(
            f"Enter item number from the list above\n"
            f"OR '.exit' to exit \n"
            f"OR .nomoreitems to finish entering items\n")
        if item_id == ".exit":
            the_exit = 1
            break
        elif item_id == ".nomoreitems":
            break
        elif item := get_item_by_id(inventory_items, item_id):
            print("*" * 100)
            try:
                item_qty = int(input("Enter quantity of the items to add to the invoice:\n>>"))
                item.insert(0, str(items_count))
                item.insert(3, str(item_qty))
                item.append(str(round(float(item[2]) * float(item[3]))))
                items.append(item)
                items_count += 1
            except TypeError:
                continue
            except ValueError:
                continue
        else:
            print("WRONG ITEM NUMBER OR QUANTITY INFO. TRY AGAIN")
            time.sleep(3)
            continue
    if the_exit == 1:
        return 0
    sub_total = str(sum([int(x[4]) for x in items]))
    hst_total = str(round(float(sub_total) * 0.13, 2))
    total = str(float(sub_total) + float(hst_total))
    print_invoice(invoice_number=invoice_number, sub_total=sub_total, hst_total=hst_total,
                  total=total, items=items, bill_to=bill_to, due_date=due_date_str,
                  invoice_date=invoice_date_str, subject=subject)
    return 1

#function return 2-items(name, price) list based on itemid,
#if item exists in inventory, otherwise return None
def get_item_by_id(inventory_items, item_id):
    for item in inventory_items:
        if item["itemid"] == item_id:
            return [item["itemname"], str(item["itemprice"])]
    return None

#function prints itemid and itemname in the form of table
def print_inventory_item_names(inventory_items):
    print("Item ID".ljust(15, " "), "Item Name".ljust(40, " "))
    for item in inventory_items:
        print(item["itemid"].ljust(15, " "), item["itemname"].ljust(40, " "))

#function represents inventory menu
def print_inventory_menu(inventory_items):
    while True:
        operation = input("Input type of operation to perform with inventory\n"
                          "1) Add new item\n"
                          "2) View Invetory\n"
                          "3) Exit\n"
                          ">>")
        if operation == "1":
            itemname, sep, itemprice = input("Enter new item in format: "
                                             "\"Item_name Item_price\" (space separated).\n"
                                             ).rpartition(" ")
            if sep == " ":
                try:
                    new_item_id = str(max([int(x["itemid"]) for x in inventory_items]) + 1)
                    item_gst = round(float(itemprice) * 0.13, 2)
                    item_total = item_gst + float(itemprice)
                    inventory_items.append({"itemid":new_item_id, "itemname":itemname,
                                            "itemprice":float(itemprice), "itemgst": item_gst,
                                            "itemtotal":item_total})
                except TypeError:
                    print("WRONG FORMAT!!! TRY AGAIN")
                    time.sleep(3)
                    continue
                except ValueError:
                    print("WRONG FORMAT!!! TRY AGAIN")
                    time.sleep(3)
                    continue
            else:
                print("WRONG FORMAT!!! TRY AGAIN")
                time.sleep(3)
                continue
        elif operation == "2":
            clear()
            print("*" * 100)
            print(" ".join(["#         ", "Item Name" + " " * 32,
                            "Item Price", "GST       ", "Total     "]).ljust(100, " "))
            print("*" * 100)
            for item in inventory_items:
                print(" ".join([item["itemid"].ljust(10, " "), item["itemname"].ljust(40, " "),
                                str(item["itemprice"]).ljust(10, " "), str(item["itemgst"]).ljust(10, " "),
                                str(round(item["itemprice"] + item["itemgst"], 2))]).ljust(100, " "))
        elif operation == "3" or operation.lower() == "exit":
            break
    return 0

#function represent dummy database. All data saved in simple lists
def load_initial_data(inventory_items):
    inventory_items.append({"itemid":"1", "itemname":"Windows License",
                            "itemprice":120.0, "itemgst": 135.60})
    inventory_items.append({"itemid":"2", "itemname":"Support(monthly service)",
                            "itemprice":1000, "itemgst": 1130.00})
    inventory_items.append({"itemid":"3", "itemname":"Emergency support(monthly service)",
                            "itemprice":3000.0, "itemgst": 3390.00})
    inventory_items.append({"itemid":"4", "itemname":"Paperclips",
                            "itemprice":1.50, "itemgst": 1.69})

#application entry point
if __name__ == "__main__":
    inventory_items = []
    load_initial_data(inventory_items)

    #main cycle of application
    while True:
        input("Enter Any Key To Start Another Operation")
        clear()
        operation = input("Input type of operation to perform\n"
                          "1) Print invoice\n"
                          "2) Check Inventory\n"
                          "3) Exit\n"
                          ">>")
        if operation == "1":
            # return 1 meaning invoice creation was not canceled mid-way
            # return 0 meaning user cancelled creation of the invoice so we clear the screen
            if print_invoice_menu(inventory_items=inventory_items) == 0:
                clear()
        elif operation == "2":
            print_inventory_menu(inventory_items)
        elif operation == "3" or operation.lower() == "exit":
            break




