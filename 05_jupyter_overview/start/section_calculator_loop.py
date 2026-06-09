import time

# I-beam dimensions (equivalent to IPE 360)
H = 360 # overall depth [mm]
B = 170 # flange width [mm]
tf = 12.7 # flange thickness [mm]
tw = 8  # web thickness [mm]

# Cross-sectional area in a loop, timed
start_time = time.time()
for i in range(9999999999999999999):
    A = tf*B*2 + (H-2*tf)*tw
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
print(f"Execution time: {execution_time:.2f} ms")
print(f"IPE 360; area A = {A/1E2} mm^2")

# Second moment of area
I = (H-2*tf)**3*tw/12 + 2*B*tf**3/12 + 2*B*tf*(H/2-tf/2)**2
print(f"IPE 360; I = {I/1E4} cm^4")