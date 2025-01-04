# Calculate voltage using Ohm's Law
def voltage(ampers, ohms):
    return ampers * ohms
# Calculate current using Ohm's Law
def current(volts, ohms):
    return volts / ohms
# Calculate resistance using Ohm's Law
def resistance(volts, ampers):
    return volts / ampers

# Example values
volts = 10   # in volts
ampers = 2   # in amperes
ohms = 5     # in ohms

# Calculations
volts = voltage(ampers, ohms)
ampers = current(volts, ohms)
ohms = resistance(volts, ampers)

# Printing results
print("Results:")
print("Voltage: {} V".format(volts))
print("Current: {} A".format(ampers))
print("Resistance: {} Ω".format(ohms))
