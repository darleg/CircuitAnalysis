from numpy import array, linalg

# Kirchhoff's Current Law to find the Voltages
# Resistances (in ohms)
R1 = 10
R2 = 20
R3 = 30
# Currents entering the nodes (in amperes)
I1 = 1.5
I2 = 2.5
# Coefficient matrix
A = array([[1/R1 + 1/R3, -1/R3], [-1/R3, 1/R2 + 1/R3]])
# Constant matrix
B = array([I1, I2])
# Solve for the node voltages using numpy's linear algebra solver
nodeVoltages = linalg.solve(A, B)

# Display the results
V1, V2 = nodeVoltages
print("Node Voltages:")
print(f"Node Voltage V1: {V1:.2f} V")
print(f"Node Voltage V2: {V2:.2f} V")
