import numpy as np
import matplotlib.pyplot as plt

# Summing Amplifier Function
def summing_amplifier(V1, V2, Rf, R1, R2):
    # Output of the summing amplifier
    Vout = -(V1 * (Rf / R1) + V2 * (Rf / R2))
    return Vout

# Difference Amplifier Function
def difference_amplifier(V1, V2, Rf, Rin):
    # Output of the difference amplifier
    Vout = (Rf / Rin) * (V2 - V1)
    return Vout

# Resistor values in ohms
Rf = 10000  # 10k ohms
R1 = 10000  # 10k ohms
R2 = 10000  # 10k ohms
Rin = 10000  # 10k ohms

# Test Input Voltages for Summing Amplifier
V1_summing = 2  # 2V input
V2_summing = 3  # 3V input

# Test Input Voltages for Difference Amplifier
V1_difference = 2  # 2V input
V2_difference = 5  # 5V input

# Simulate the summing amplifier
Vout_summing = summing_amplifier(V1_summing, V2_summing, Rf, R1, R2)

# Simulate the difference amplifier
Vout_difference = difference_amplifier(V1_difference, V2_difference, Rf, Rin)

# Print Results
print(f"Summing Amplifier Output: Vout = {Vout_summing}V")
print(f"Difference Amplifier Output: Vout = {Vout_difference}V")

# Plotting the results for visualization
# This will show how the outputs behave for a range of input values

V1_range = np.linspace(-10, 10, 100)  # Range of input values
V2_range = np.linspace(-10, 10, 100)

# Calculate outputs across the input ranges
Vout_summing_range = summing_amplifier(V1_range, V2_range, Rf, R1, R2)
Vout_difference_range = difference_amplifier(V1_range, V2_range, Rf, Rin)

# Plotting
plt.figure(figsize=(12, 6))

# Summing Amplifier Plot
plt.subplot(1, 2, 1)
plt.plot(V1_range, Vout_summing_range, label='Summing Amplifier Output')
plt.title("Summing Amplifier")
plt.xlabel("Input Voltage (V1)")
plt.ylabel("Output Voltage (Vout)")
plt.legend()

# Difference Amplifier Plot
plt.subplot(1, 2, 2)
plt.plot(V1_range, Vout_difference_range, label='Difference Amplifier Output')
plt.title("Difference Amplifier")
plt.xlabel("Input Voltage (V1)")
plt.ylabel("Output Voltage (Vout)")
plt.legend()

plt.tight_layout()
plt.show()

