import pandas as pd
import numpy as np
#maize yield (90kg bags) per plot over a single season
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90 kg bags per plot)")
print(f" Plots:   {len(yields)}")
print(f" Total yield:  {np.sum(yields)} bags ({np.sum(yields) * 90:,} kg)")
print(f" Mean:  {np.mean(yields):.1f} bags/plot")
print(f" Median:  {np.median(yields):.1f} bags/plot")
print(f" Std dev: {np.std(yields):.1f}")
print(f" Best plot:  {np.max(yields)} bags")
print(f" Worst plot: {np.min(yields)} bags")
print(f" Top 25% (75th pctile): {np.percentile(yields,75):.0f} bags")

print()
#Revenue at KES 2,800 per 90kg bag
revenue = yields * 2800
print("REVENUE (KES 2,800 per bag)")
print(f" Total:  KES {np.sum(revenue):,}")
print(f" Avg/plot: KES {np.mean(revenue):,.0f}")

print()
#Correlation between rainfall and yield
corr = np.corrcoef(rainfall_mm, yields)[0, 1]
print(f" Rainfall vs yield correlation: {corr:.2f}")
print("(1.0 = perfect positive link, 0 = no link)")

print(f"\nAVERAGE RAINFALL FOR HIGH-PERFORMING PLOTS Vs LOW PERFORMING PLOTS:")
plots_above_min = (yields > (np.mean(yields)))
plots_below_min = (yields < (np.mean(yields)))

print("Plots above mean:", yields[plots_above_min])
print("Plots below mean:", yields[plots_below_min])
print(f"Average rainfall for plots above mean: {np.mean(rainfall_mm[plots_above_min]):.1f} mm")
print(f"Average rainfall for plots below mean: {np.mean(rainfall_mm[plots_below_min]):.1f} mm")

