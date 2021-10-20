import os
from datetime import datetime, timedelta
import string

def clear():
    # print(os.name)
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

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
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print("Bill To: ",  bill_to, sep="", end="")
    bill_to_line_spaces_needed = 100 - 9 - len(bill_to) - 14 - len(invoice_date)
    print(" " * bill_to_line_spaces_needed, "Invoice date: ", invoice_date, sep="")
    print("Term: Custom".rjust(100, " "))
    print(" ".join(["Due Date:", due_date]).rjust(100, " "))
    print(" ".join(["P.O.", "1111"]).rjust(100, " "))
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" ".join(["Subject", subject]).ljust(100, " "))
    print(" " * 100)
    print(" " * 100)
    # print(" ".join(["#", "\t\t\t", "Item", "\t" * 7, "Qty", "\t\t\t", "Rate", "\t\t\t", "Amount"]).ljust(100, " "))
    print(" ".join(["#         ", "Item"+" "*36,
                    "Qty       ", "Rate      ", "Amount    "]).ljust(100, " "))
    for item in items:
        print(" ".join([item[0].ljust(10, " "), item[1].ljust(40, " "),
                        item[2].ljust(10, " "), item[3].ljust(10, " "), item[4]]).ljust(100, " "))
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" " * 100)
    print(" ".join(["Sub Total: ", sub_total]).rjust(100, " "))
    print(" ".join(["HST(13%): ", hst_total]).rjust(100, " "))
    print(" ".join(["Total: ", total]).rjust(100, " "))
    print(" ".join(["Balance Due: ", total]).rjust(100, " "))


if __name__ == "__main__":
    while True:
        input("Enter Any Key To Start Another Invoice")
        clear()
        invoice_number = input("Enter invoice Number (OR '.exit' to exit): ")
        if invoice_number == ".exit":
            continue
        bill_to = input("Enter bill to company (OR '.exit' to exit): ")
        if bill_to == ".exit":
            continue
        subject = input("Enter invoice's subject (OR '.exit' to exit): ")
        if bill_to == ".exit":
            continue
        entered_date = input("Enter invoice date in format mm/dd/yyyy").split("/")
        if entered_date == ".exit":
            continue
        invoice_date = datetime(int(entered_date[2]), int(entered_date[0]), int(entered_date[1]))
        invoice_date_str = datetime.today().strftime('%m/%d/%Y')
        due_date = invoice_date + timedelta(days=15)
        due_date_str = due_date.strftime('%m/%d/%Y')
        items_count = 1
        items = []
        the_exit = 0
        while True:
            print("*" * 100)
            item = input(f"Enter {items_count}(st/d) item in format: \"Item_name Qty Rate\" (space separated). (item name with NO spaces)\n"
                         f"OR 'exit' to exit \n"
                         f"OR .nomoreites to finish entering items\n").split(" ")
            print("*" * 100)
            if item[0] == ".exit":
                the_exit = 1
                break
            elif item[0] == ".nomoreitems":
                break
            elif not len(item) == 3:
                continue
            try:
                item.insert(0, str(items_count))
                item.append(str(round(float(item[2]) * float(item[3]))))
                items.append(item)
                items_count += 1
            except TypeError:
                continue
            except ValueError:
                continue
        if the_exit == 1:
            continue
        sub_total = str(sum([int(x[4])  for x in items]))
        hst_total = str(round(float(sub_total) * 0.13, 2) )
        total = str(float(sub_total) + float(hst_total))
        print_invoice(invoice_number=invoice_number, sub_total=sub_total, hst_total=hst_total,
                      total=total, items=items, bill_to=bill_to, due_date=due_date_str,
                      invoice_date=invoice_date_str, subject=subject)




