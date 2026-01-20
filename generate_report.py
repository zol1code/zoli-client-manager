# Zoli Code - Business Intelligence Tool
# This script simulates generating a monthly financial report for freelance activities.

import datetime

def generate_monthly_report(freelance_data):
    print(f"--- ZOLI CODE | FINANCIAL REPORT ---")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 40)
    
    total_revenue = 0
    paid_count = 0
    pending_count = 0
    
    # Processamento dos dados (Lógica de Backend)
    for entry in freelance_data:
        amount = entry['value']
        total_revenue += amount
        
        status_icon = "✅" if entry['status'] == "Paid" else "⏳"
        if entry['status'] == "Paid":
            paid_count += 1
        else:
            pending_count += 1
            
        print(f"{status_icon} Client: {entry['client']:<15} | Amount: €{amount:>8.2f}")

    # Cálculos de Impostos (Simulação para Irlanda)
    tax_provision = total_revenue * 0.20 # Estimativa de 20% para Income Tax
    net_profit = total_revenue - tax_provision

    print("-" * 40)
    print(f"GROSS REVENUE:        €{total_revenue:>8.2f}")
    print(f"TAX PROVISION (20%): -€{tax_provision:>8.2f}")
    print(f"ESTIMATED NET PROFIT: €{net_profit:>8.2f}")
    print("-" * 40)
    print(f"Summary: {paid_count} Paid | {pending_count} Pending")
    print(f"Status: {'CRITICAL' if pending_count > paid_count else 'HEALTHY'}")
    print("-" * 40)

# Dados simulados (Mock Data) que viriam do seu Dashboard
current_month_data = [
    {"client": "Tech Corp IE", "value": 1200.00, "status": "Paid"},
    {"client": "Local Cafe", "value": 350.00, "status": "Pending"},
    {"client": "Dublin Devs", "value": 800.00, "status": "Paid"},
    {"client": "Zoli Design", "value": 150.00, "status": "Pending"}
]

if __name__ == "__main__":
    generate_monthly_report(current_month_data)
