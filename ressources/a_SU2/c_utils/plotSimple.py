# Import
import matplotlib.pyplot as plt
import pandas as pd


# Initialize file
df = pd.read_csv("history.csv")
df.columns = df.columns.str.strip().str.strip('"').str.strip()   # Remove spaces/brackets

# Plot
plt.plot(df['Inner_Iter'],df['rms[Rho]'], color= 'red', label=r'$\rho$')
plt.plot(df['Inner_Iter'],df['rms[RhoU]'], color= 'green', label=r'$\rho_U$')
plt.plot(df['Inner_Iter'],df['rms[RhoV]'], color= 'blue', label=r'$\rho_V$')
plt.plot(df['Inner_Iter'],df['rms[RhoE]'], color= 'black', label=r'$\rho_E$')


plt.legend()
plt.show()