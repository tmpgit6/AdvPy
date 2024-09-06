import matplotlib.pyplot as plt 



x = [1,2,3,4,5,6,7]
y_normal = [10,29,30,43,51,65,71]
y_custom = [15,23,32,49,58,61,79]
labels = ["A", "B", "C", "D", "E", "F", "G"]


fig, ax = plt.subplots()


# Scatter
ax.scatter(x, y_normal)
ax.scatter(x, y_custom)


# Add annotations to Scatter 1 --> with a label
for i, label in enumerate(labels):  # enumerate(y) or enumerate(labels)
    ax.annotate(label, (x[i], y_normal[i]) )

# Add annotations to Scatter 2 --> with the value of y_axis
for i, label in enumerate(y_custom):  # enumerate(y) or enumerate(labels)
    ax.annotate(label, (x[i], y_custom[i]) )


# Show Window
plt.show()
