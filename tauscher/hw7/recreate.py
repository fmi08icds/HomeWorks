import matplotlib as plt

## recreate example from lecture, Excercise 1.





import matplotlib.pyplot as plt
import numpy as np

# make data
x = np.linspace(0, 8, 100)
y = np.cos(x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)


## add bold labels
ax.set_xlabel(r'Time ($t$)', fontweight='bold')
ax.set_ylabel(r'Voltage ($mV$)', fontweight='bold')
## add title
ax.set_title('About as simple as it gets, folks')

## add grid
ax.grid(True)

## add tickmarks in 0.25 steps
ax.set_xticks(np.arange(0, 2, 0.25), minor=True)
ax.set_yticks(np.arange(0, 2, 0.25), minor=True)


## add labelnames to x and y axis

plt.show()
