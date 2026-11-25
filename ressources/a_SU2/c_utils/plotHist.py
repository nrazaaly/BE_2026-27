
#!/usr/bin/env python3
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Check input
if len(sys.argv) != 2:
    sys.exit("Usage: python plotHist.py history.csv")

# Get data 
filename = sys.argv[1]
df = pd.read_csv(filename)
df.columns = df.columns.str.strip().str.strip('"').str.strip()

# Plot
plt.plot(df["Inner_Iter"], df["rms[Rho]"],   color="blue",   label=r"$\|\rho\|$")
plt.plot(df["Inner_Iter"], df["rms[RhoU]"],  color="red",    label=r"$\|\rho u\|$")
plt.plot(df["Inner_Iter"], df["rms[RhoV]"],  color="green",  label=r"$\|\rho v\|$")
plt.plot(df["Inner_Iter"], df["rms[RhoE]"],  color="orange", label=r"$\|\rho E\|$")

plt.xlabel(r"$N_{iter}$", fontsize=13)
plt.ylabel(r"$|\cdot|$", fontsize=13)
plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.legend(fontsize=12)
plt.tight_layout()

output = os.path.splitext(filename)[0] + ".png"
plt.savefig(output, dpi=300)
print(f"Figure saved: {output}")
plt.show()
