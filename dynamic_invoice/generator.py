from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date

def generate_invoice():
    
    company_name = input("Enter your company name: ")
    company_address = input("Enter your company address: ")

    
    client_name = input("Enter the client's name: ")

    
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {item_name}: "))
        price = float(input(f"Enter price for {item_name}: "))
        items.append((item_name, quantity, price))

    
    file_name = f"invoice_{client_name}_{date.today()}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    c.setFont("Helvetica", 12)

    
    c.drawString(30, 750, company_name)
    c.drawString(30, 735, company_address)

    
    c.drawString(400, 750, f"Invoice for: {client_name}")
    c.drawString(400, 735, f"Date: {date.today()}")

    
    c.drawString(30, 680, "Item")
    c.drawString(200, 680, "Quantity")
    c.drawString(300, 680, "Price")
    c.drawString(400, 680, "Total")

  
    y_position = 660
    total_amount = 0
    for item, quantity, price in items:
        total = quantity * price
        c.drawString(30, y_position, item)
        c.drawString(200, y_position, str(quantity))
        c.drawString(300, y_position, f"${price:.2f}")
        c.drawString(400, y_position, f"${total:.2f}")
        y_position -= 20
        total_amount += total

    
    c.drawString(300, y_position - 20, "Total:")
    c.drawString(400, y_position - 20, f"${total_amount:.2f}")

    
    c.save()

    print(f"Invoice saved as {file_name}")
