# Zoli Code - Invoice Processing Logic
# Proves: Python Lists, Dictionaries, Math Operations, and Formatting

def calculate_invoice(services):
    """
    Calculates the total and tax for a list of freelance services.
    In Ireland, standard VAT can be 23%, but for many freelancers, 
    it might be different. Let's use a professional format.
    """
    subtotal = sum(service['price'] for service in services)
    tax_rate = 0.23  # Irish Standard VAT
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    print(f"--- ZOLI CODE INVOICE SUMMARY ---")
    for s in services:
        print(f"Service: {s['name']} | Price: €{s['price']:.2f}")
    
    print("-" * 30)
    print(f"Subtotal: €{subtotal:.2f}")
    print(f"VAT (23%): €{tax_amount:.2f}")
    print(f"TOTAL: €{total:.2f}")
    print("-" * 30)

# Mock data for demonstration
my_services = [
    {"name": "Web Development", "price": 450.00},
    {"name": "IT Support Setup", "price": 120.00},
    {"name": "SEO Optimization", "price": 85.00}
]

if __name__ == "__main__":
    calculate_invoice(my_services)
