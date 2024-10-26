import numpy as np
import matplotlib.pyplot as plt

# Define gate functions
def nand_gate(voltage1, voltage2):
    return 5.0 - min(voltage1, voltage2)  # Inverse of AND

def or_gate(voltage1, voltage2):
    return max(voltage1, voltage2)

def xor_gate(voltage1, voltage2):
    return abs(voltage1 - voltage2)  # Turn on when one input is high

def and_gate(voltage1, voltage2):
    return min(voltage1, voltage2)

# Generate data and plot results
def plot_gate_behavior():
    voltages = np.linspace(0, 5, 100)
    V1, V2 = np.meshgrid(voltages, voltages)
    
    # Simulate each gate
    nand_output = nand_gate(V1, V2)
    or_output = or_gate(V1, V2)
    xor_output = xor_gate(V1, V2)
    and_output = and_gate(V1, V2)
    
    # Create a 2x2 grid for each gate's output
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    
    axs[0, 0].contourf(V1, V2, nand_output, levels=100, cmap='coolwarm')
    axs[0, 0].set_title("NAND Gate")
    
    axs[0, 1].contourf(V1, V2, or_output, levels=100, cmap='coolwarm')
    axs[0, 1].set_title("OR Gate")
    
    axs[1, 0].contourf(V1, V2, xor_output, levels=100, cmap='coolwarm')
    axs[1, 0].set_title("XOR Gate")
    
    axs[1, 1].contourf(V1, V2, and_output, levels=100, cmap='coolwarm')
    axs[1, 1].set_title("AND Gate")
    
    plt.show()

# Call the function to visualize the gate behaviors
plot_gate_behavior()

