import pandas as pd
df = pd.DataFrame({
    "client": ["Moses","Albert","Kelvin","Hope","Dama","Aston","Jady","Loice"],
    "item": ["gate","grill","frame","gate","grill","tankstand","frame","gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes": [28000,14500,9800,32000,12000,18500,11000,29500],
    "status": ["paid","paid","pending","paid","paid","pending","paid","paid"],
    "region": ["Nairobi","Kiambu","Machakos","Nairobi","Machakos","Nairobi","Kiambu","Nairobi"],
})
print("Revenue by material type:")
by_material = df.groupby("material")["price_kes"].agg(["sum","mean","count"]).round(0)
by_material.columns = ["total_kes","avg_kes","jobs"]
print(by_material.sort_values("total_kes", ascending = False).to_string())

print("\n Paid vs pending jobs:")
print(df["status"].value_counts())

print("\nAverage job value by status:")
print(df.groupby("status")["price_kes"].mean().round(0))

print("Region by material :")
by_region_material = df.groupby(["region","material"])["price_kes"].agg(["sum","mean","count"]).round(0)
by_region_material.columns = ["total_kes","avg_kes","jobs"]
print(by_region_material.to_string())