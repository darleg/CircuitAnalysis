def ohmsLaw(V=None, I=None, R=None):
    if V is None:
        V = I * R
    elif I is None:
        I = V / R
    elif R is None:
        R = V / I
    return V, I, R

# Examples
print("Examples:")
v0, i0, r0 = ohmsLaw(V=10, R=5)
print(f"Voltage: {v0} V, Current: {i0} A, Resistance: {r0} Ω")
v1, i1, r1 = ohmsLaw(I=2, R=5)
print(f"Voltage: {v1} V, Current: {i1} A, Resistance: {r1} Ω")
v2, i2, r2 = ohmsLaw(V=10, I=2)
print(f"Voltage: {v2} V, Current: {i2} A, Resistance: {r2} Ω")
