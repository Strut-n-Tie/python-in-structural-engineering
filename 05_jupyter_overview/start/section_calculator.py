# I-beam dimensions (equivalent to IPE 360)
H = 360 # overall depth [mm]
B = 170 # flange width [mm]
tf = 12.7 # flange thickness [mm]
tw = 8  # web thickness [mm]

# Cross-sectional area
A = tf*B*2 + (H-2*tf)*tw
print(f"IPE 360; area A = {A/1E2} mm^2")

# Second moment of area
I = (H-2*tf)**3*tw/12 + 2*B*tf**3/12 + 2*B*tf*(H/2-tf/2)**2
print(f"IPE 360; I = {I/1E4} cm^4")