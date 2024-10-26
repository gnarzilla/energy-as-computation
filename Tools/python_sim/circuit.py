import numpy as np
import matplotlib.pyplot as plt

# Define a basic Resistor class
class Resistor:
    def __init__(self, resistance_ohms):
        self.resistance = resistance_ohms
    
    def get_voltage_drop(self, current_amps):
        return current_amps * self.resistance

# Define a basic LED class
class LED:
    def __init__(self, forward_voltage, max_current):
        self.forward_voltage = forward_voltage
        self.max_current = max_current
        self.is_on = False
    
    def apply_voltage(self, voltage):
        if voltage >= self.forward_voltage:
            self.is_on = True
        else:
            self.is_on = False
    
    def current_draw(self):
        return self.max_current if self.is_on else 0

# Example of testing the components
resistor = Resistor(1000)  # 1k Ohm resistor
led = LED(2.0, 0.02)       # LED with 2V forward voltage, 20mA max current

# Simulate voltage and current
current = 0.01  # 10mA current flowing through the circuit
voltage_drop = resistor.get_voltage_drop(current)
print(f"Voltage drop across resistor: {voltage_drop}V")

applied_voltage = 5.0  # 5V applied to the circuit
led.apply_voltage(applied_voltage)
print(f"Is the LED on? {'Yes' if led.is_on else 'No'}")

# Define a basic modulation function (e.g., simple PWM)
def modulate_power(frequency, amplitude, time):
    """
    A simple power modulation: square wave PWM for simulating modulated signals.
    :param frequency: Frequency of the signal (in Hz)
    :param amplitude: Peak amplitude (e.g., voltage level)
    :param time: Time array for simulation (in seconds)
    :return: Modulated power signal as an array of voltages
    """
    return amplitude * np.sign(np.sin(2 * np.pi * frequency * time))

# Example usage
time = np.linspace(0, 1, 1000)  # 1 second of time, divided into 1000 intervals
frequency = 10  # 10 Hz modulation
amplitude = 5   # 5V peak

# Simulate the modulated signal
modulated_signal = modulate_power(frequency, amplitude, time)

# Plot the result
plt.plot(time, modulated_signal)
plt.title("Power Modulation (PWM)")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()

# Define a simple feedback loop for error correction
def feedback_loop(target_voltage, actual_voltage):
    """
    A simple feedback mechanism that adjusts voltage to meet a target.
    :param target_voltage: The voltage we want to achieve (setpoint)
    :param actual_voltage: The actual measured voltage
    :return: Corrected voltage
    """
    error = target_voltage - actual_voltage
    correction = 0.1 * error  # Adjust based on proportional gain (simplified)
    return actual_voltage + correction

# Function to calculate frequency
def calculate_frequency(R1, R2, C1):
    return 1.44 / ((R1 + 2 * R2) * C1)

# Set your component values here
R1 = 10000  # Resistor 1 in Ohms
R2 = 10000  # Resistor 2 in Ohms
C1 = 100e-6  # Capacitor in Farads (100µF)

# Calculate frequency
frequency = calculate_frequency(R1, R2, C1)

# Time for the LED to blink (period is inverse of frequency)
T = 1 / frequency

print(f"Frequency: {frequency} Hz")
print(f"LED blinking period: {T} seconds")


# Example usage in a loop
# target_voltage = 5.0  # Target voltage for LED to stay on
# actual_voltage = 3.5  # Starting at a lower voltage
# for i in range(10):
#    actual_voltage = feedback_loop(target_voltage, actual_voltage)
#    print(f"Iteration {i+1}: Corrected Voltage = {actual_voltage:.2f}V")

def calculate_frequency(R1, R2, C1):
    return 1.44 / ((R1 + 2 * R2) * C1)

def main():
    print("Welcome to the 555 Timer Frequency Calculator")
    
    # User inputs
    R1 = float(input("Enter value for Resistor R1 (in ohms): "))
    R2 = float(input("Enter value for Resistor R2 (in ohms): "))
    C1 = float(input("Enter value for Capacitor C1 (in microfarads): ")) * 1e-6  # Convert µF to F

    # Calculate frequency
    frequency = calculate_frequency(R1, R2, C1)
    period = 1 / frequency

    # Display the result
    print(f"Frequency: {frequency:.2f} Hz")
    print(f"LED blinking period: {period:.2f} seconds")

if __name__ == "__main__":
    main()
