# pip install matplotlib
from matplotlib import pyplot as plt 
import os 
from pathlib import Path 

APP_FOLDER = Path(__file__).parent
FIGURE_FOLDER = APP_FOLDER / "figures"
os.chdir(APP_FOLDER)

""" # Multi Line Comment
line style:  '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted' 
"""


x = [1,2,3,4,5,6,7]
y = [10,29,30,43,51,65,71]
z = [11,32,41, 1, 2, 17,24]

# 1. Create a figure (Window)
fig = plt.figure()

# 2. Add a subplot to the figure ( Draw Area)
ax = fig.add_subplot(111)

# 3. Draw a graph/plot in the draw area
ax.plot(x, y, color = "green", linewidth = 5, linestyle = "--", label="Market range")
ax.plot(x, z, color = "blue", linewidth = 2, linestyle = ":" , label ="Customer Request")

# Scatter
ax.scatter([2,3,4], [23,24,36], marker= "^", color = "red", s = 50)  # s : size

# 4. Plot Configuration
plt.legend()
plt.grid(True)
plt.xlabel("Check Point")
plt.ylabel("Price")
plt.title("My First Diagram")

# 5.Save the plot as image
plt.savefig(FIGURE_FOLDER / "myfigure2.png")

# 6.Show Plot Window
plt.show()