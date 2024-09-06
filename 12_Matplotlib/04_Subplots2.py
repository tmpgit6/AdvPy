import matplotlib.pyplot as plt 

fig, ax = plt.subplots(2,2) # i need 2x rows and 2x columns in the window

x = [1,2,3,4,5,6,7]
y = [10,29,30,43,51,65,71]
z = [11,32,41, 1, 2, 17,24]


# Format: row, column

# Row : 0
###############
ax[0,0].plot(x, y, color = "green")
ax[0,1].plot(x, z, color = "red")


# Row: 1
################
ax[1,0].plot(x, y, color = "blue")
ax[1,1].plot(x, z, color = "black")


# Show Window
plt.show()