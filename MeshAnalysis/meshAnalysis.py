from numpy import array, linalg

# Mesh analysis using the resistance matrix and voltage vector.
def meshAnalysis(Rmat, Vvec):
    # Solve for the mesh currents using numpy's linear algebra solver
    meshCurrents = linalg.solve(Rmat, Vvec)
    return meshCurrents
# Example usage:
# Resistance matrix (R) and voltage vector (V) for a circuit with 3 loops
R = array([[10, -5, 0], [-5, 15, -10], [0, -10, 20]])
V = array([10, 0, 5])

# Perform mesh analysis
I = meshAnalysis(R, V)

print("Mesh currents:", I)
