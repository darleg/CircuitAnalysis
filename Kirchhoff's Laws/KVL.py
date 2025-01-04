from numpy import array, linalg

'''
Electronic Circuit is
┌─ R1 ┬ R2 ─┐
V1    R3    V2
└─────┴─────┘
with following values:
'''

# Kirchhoff's Voltage Law to find the currents
# Resistances (in ohms)
R1 = 10
R2 = 20
R3 = 30
# Voltage sources (in volts)
V1 = 10
V2 = 15
# Coefficient matrix A and the constant matrix B
A = array([[R1 + R2, -R2], [-R2, R2 + R3]])
B = array([V1, V2])
# Solve for the currents using numpy's linear algebra solver
currents = linalg.solve(A, B)

# Display the results
print("Currents:")
print(f"Current through R1 and R2 (I1): {currents[0]} A")
print(f"Current through R2 and R3 (I2): {currents[1]} A")
