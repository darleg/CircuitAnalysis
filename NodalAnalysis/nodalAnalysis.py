from numpy import array, linalg

# Perform nodal analysis using the conductance matrix and current vector.
def nodalAnalysis(Gmat, Ivec):
    # Solve for the node voltages using numpy's linear algebra solver
    nodeVoltages = linalg.solve(Gmat, Ivec)
    return nodeVoltages

# Example usage:
G = array([[10, -2, 0], [-2, 12, -5], [0, -5, 15]])
I = array([3, 0, 5])

# Perform nodal analysis
V = nodalAnalysis(G, I)

print("Node voltages:", V)
