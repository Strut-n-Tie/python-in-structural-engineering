# I-beam dimensions (equivalent to IPE 360)
H = 360 # overall depth [mm]
B = 170 # flange width [mm]
tf = 12.7 # flange thickness [mm]
tw = 8  # web thickness [mm]

# # Cross-sectional area
# A = tf*B*2 + (H-2*tf)*tw
# print(f"IPE 360; area A = {A/1E2} mm^2")

# # I-beam dimensions (equivalent to IPE 400)
# H = 400 # overall depth [mm]
# B = 180 # flange width [mm]
# tf = 13.5 # flange thickness [mm]
# tw = 8.6  # web thickness [mm]

# Cross-sectional area
A = tf*B*2 + (H-2*tf)*tw
print(f"IPE 400; area A = {A/1E2} mm^2")