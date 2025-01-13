import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Create figure with transparent background
fig = plt.figure(figsize=(12, 12))
fig.patch.set_alpha(0)

# Create axes with transparent background
ax = plt.axes()
ax.set_axis_off()  # Hide axes
ax.patch.set_alpha(0)

# Set the text
text = ax.text(0.0, 0.5, 'LW', 
               horizontalalignment='center',
               verticalalignment='center',
               fontweight='bold',
               fontname='Arial',  # You can change this to your preferred font
               fontsize=1000)

# Adjust the layout to be tight around the text
plt.tight_layout()

# Save as SVG with transparent background
plt.savefig('LW_arial.svg', 
            format='svg',
            transparent=True,
            bbox_inches='tight',
            pad_inches=0.1)

plt.close()