import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
 

# Create 2x2 Plot with grid spec
gs = gridspec.GridSpec(2,2)

# First Subplot 
ax = plt.subplot(gs[0,0])  # row 0, col 0
plt.plot([0, 1 ,2], color = "blue")

# Second Plot 
ax = plt.subplot(gs[0,1])  # row 0, col 1
plt.plot([0, 1 ,2], color = "red")


# Third Plot
ax = plt.subplot(gs[1,:])  # row 1,  all columns ( span over all columns)
plt.plot([0, 1 ,2], color = "green")


# Show Plot
plt.show()