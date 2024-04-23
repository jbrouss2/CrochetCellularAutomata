import cellpylib as cpl
import numpy as np
import matplotlib.pyplot as plt

# initialize a 60x60 2D cellular automaton
cellular_automaton = cpl.init_simple2d(9, 9)

timesteps= 30
# evolve the cellular automaton for 30 time steps,
#  applying totalistic rule 126 to each cell with a Moore neighbourhood
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=timesteps, neighbourhood='von Neumann',
                                  apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=22))

#print(cellular_automaton[timesteps-1])

def plot_grid(grid):
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.grid(True, which='both', color='gray', linewidth=1.0)
    plt.xticks(np.arange(-0.5, grid.shape[1], 1), [])
    plt.yticks(np.arange(-0.5, grid.shape[0], 1), [])
    plt.show()


arr = np.array(cellular_automaton[timesteps-1])
plot_grid(arr)

# I am manually manipulating the array here to fit mosaic rules.
# Later try to write code to do this.

arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  #0
                [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  #1
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  #0
                [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],  #1
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],  #0
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],  #1
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) #1


# Print and plot the new mosaic crochet grid.
print(arr)
plot_grid(arr)
