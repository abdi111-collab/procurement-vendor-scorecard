import random
import csv

# 1. SETUP MOCK PROCUREMENT VENDOR METRICS (Addis Ababa Context)
random.seed(88)
vendors = ['Ethio Freight Solutions', 'Abyssinia Logistics Ltd', 'Horn of Africa Trading', 'Sheba Supply Corp']
items = ['Medical Consumables', 'Water Treatment Chemicals', 'Nutritional Supplements', 'Operational Equipment']

print("="*60)
print("   BUILDING VENDOR PERFORMANCE ACCOUNTABILITY MATRIX  ")
print("="*60)

# 2. GENERATE AND COMPUTE PERFORMANCE MATRIX DATA
scorecard_data = []
for i in range(1, 51):  # 50 structural purchase order histories
    vendor = random.choice(vendors)
    item = random.choice(items)
    
    # Simulate realistic business operations variables
    qty_ordered = random.randint(100, 1000)
    unit_cost = round(random.uniform(15.0, 250.0), 2)
    po_value = round(qty_ordered * unit_cost, 2)
    
    # Introduce real procurement metrics: On-Time Delivery & Damage Defect rates
    on_time = random.choices([1, 0], weights=[0.85, 0.15], k=1)[0]  # 85% baseline OTD
    defect_free = random.choices([1, 0], weights=[0.94, 0.06], k=1)[0] # 6% standard defect rate
    
    # Determine delivery status strings for Excel presentation
    delivery_status = "ON-TIME" if on_time == 1 else "DELAYED"
    quality_status = "COMPLIANT" if defect_free == 1 else "DEFECTIVE DETECTED"
    
    # Evaluate strategic operational risk tiers based on performance variables
    if on_time == 0 or defect_free == 0:
        vendor_tier = "CRITICAL RISK - AUDIT REQUIRED"
    else:
        vendor_tier = "PREFERRED SUPPLIER"

    scorecard_data.append({
        'PO_Reference': f'PO-2026-X{2000+i}',
        'Vendor_Name': vendor,
        'Procured_Material': item,
        'Quantity_Units': qty_ordered,
        'Unit_Cost_USD': unit_cost,
        'Total_PO_Value_USD': po_value,
        'Logistics_KPI': delivery_status,
        'Quality_Assurance': quality_status,
        'Strategic_Vendor_Tier': vendor_tier
    })

# 3. EXPORT EXCEL-COMPATIBLE WORKBOOK LEDGER (.csv for spreadsheet intake)
output_filename = 'vendor_performance_matrix.csv'

with open(output_filename, mode='w', newline='', encoding='utf-8') as excel_file:
    if scorecard_data:
        writer = csv.DictWriter(excel_file, fieldnames=scorecard_data[0].keys())
        writer.writeheader()
        writer.writerows(scorecard_data)

print(f"[✔] Successfully processed 50 vendor operational histories.")
print(f"[✔] Compiled performance data exported to '{output_filename}'.")
print("[!] Open this file natively in Microsoft Excel to view calculated filters.")
print("="*60)
