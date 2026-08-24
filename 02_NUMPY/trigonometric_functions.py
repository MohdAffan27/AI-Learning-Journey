import numpy as np

angles = np.array([0, 30, 45, 60, 90]) 
rad = np.deg2rad(angles)  # convert degrees to radians

# Sine of angles
sin_vals = np.sin(rad)
print("Sine values:", sin_vals)

# Inverse sine in degrees
inv_sin = np.rad2deg(np.arcsin(sin_vals))
print("Inverse sine (degrees):", inv_sin)

# Hyperbolic sine
sinh_vals = np.sinh(rad)
print("Hyperbolic sine:", sinh_vals)

# Hypotenuse of a right triangle
hyp = np.hypot(3, 4)
print("Hypotenuse:", hyp)