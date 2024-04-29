import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 10))
colors = ['#e63946', '#f4a261', '#2a9d8f', '#264653', '#e9c46a']
num_shapes = 50
x_positions = np.random.uniform(0, 10, num_shapes)
y_positions = np.random.uniform(0, 10, num_shapes)
sizes = np.random.uniform(0.2, 1, num_shapes)

for x, y, s in zip(x_positions, y_positions, sizes):
    color = np.random.choice(colors)
    ax.add_patch(plt.Circle((x, y), radius=s, color=color, alpha=0.7))
num_rectangles = 10
for _ in range(num_rectangles):
    x = np.random.uniform(0, 9)
    y = np.random.uniform(0, 9)
    width = np.random.uniform(1, 3)
    height = np.random.uniform(1, 3)
    angle = np.random.uniform(0, 360)
    color = np.random.choice(colors)
    ax.add_patch(
        plt.Rectangle(
            (x, y),
            width,
            height,
            angle=angle,
            color=color,
            alpha=0.5,
            fill=True,
        )
    )

num_lines = 20
for _ in range(num_lines):
    x_start = np.random.uniform(0, 10)
    y_start = np.random.uniform(0, 10)
    x_end = np.random.uniform(0, 10)
    y_end = np.random.uniform(0, 10)
    color = np.random.choice(colors)
    ax.plot([x_start, x_end], [y_start, y_end], color=color, lw=2, alpha=0.7)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

plt.title("Abstract - CodeMaster7000")
plt.show()
