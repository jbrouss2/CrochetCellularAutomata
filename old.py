# import os
# import numpy as np
# import sys
# import matplotlib.pyplot as plt
# import argparse
# import time

# class PatternGenerator():
#     def __init__ (self, num_experiments):
#         self.num_experiments = num_experiments
        

#     def simulate(self):


#         # Create the associated figure 
#         fig = plt.figure()
#         ax = plt.Axes(fig, [0., 0., 1., 1.])
#         ax.set_axis_off() 
#         fig.add_axes(ax)
#         ax.imshow(self.palette[self.board.astype(int)]) 
#         img_fn = self.exp_dir + "/experiment_" + str(experiment) + "_step_" + str(z) + ".png"
#         plt.savefig(img_fn, dpi=800, bbox_inches="tight", pad_inches=0)
#         plt.close(fig)

#     if __name__ == '__main__':
#         print ("Hello World!")
#         parser = argparse.ArgumentParser(description="Crochet Cellular Automata")
        
#         # Determine the arguments we wish to have
#         parser.add_argument("--")

#         args = parser.parse_args()

#         pattern = PatternGenerator(args.expereiments, args )
#         pattern.simulate()

# import cellpylib as cpl

# # initialize a 60x60 2D cellular automaton
# cellular_automaton = cpl.init_simple2d(60, 60)

# # evolve the cellular automaton for 30 time steps,
# #  applying totalistic rule 126 to each cell with a Moore neighbourhood
# cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=30, neighbourhood='von Neumann',
#                                   apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=26))

# cpl.plot2d(cellular_automaton, show_grid=True)

import cellpylib as cpl
import matplotlib.pyplot as plt
import argparse
import numpy as np
import sys
print(sys.path)

# evolve the cellular automaton for 30 time steps,
#  applying totalistic rule 126 to each cell with a Moore neighbourhood
# cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=30, neighbourhood='von Neumann',
                                #   apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=22))


class PatternGenerator():
    def __init__(self, size_block, number_of_blocks, size_pattern, neighbourhood, rule_number):
        self.size_block = size_block
        self.number_of_blocks = number_of_blocks
        self.size_pattern = size_pattern
        self.neighbourhood = neighbourhood
        self.rule_number = rule_number

    # Compile the info to generate one sqaure
    def create_square(self):
        # Create a list to store them 
        patterns_list = []

        # initialize a 2D cellular automaton based off size block
        cellular_automaton = cpl.init_simple2d(self.size_block, self.size_block)

        # Determine the neighborhood
        neighborhood = ""
        if self.neighbourhood == 0:
            neighborhood = "Moore"
        elif self.neighbourhood == 1:
            neighborhood = "von Neumann"
        else:
            print("Error: Invalid neighbourhood")
            sys.exit(1)

        print(neighborhood)

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=30, neighbourhood=neighborhood,
                                            apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=4, rule=self.rule_number))
        
        cpl.plot2d(cellular_automaton, show_grid=True)
        
    def create_full_pattern():
        # Compile the squares into one full thing
        print("hello")

if __name__ == '__main__':
    print("hello")
    parser = argparse.ArgumentParser(description="Crochet Cellular Automata")

    # Overall arguments
    parser.add_argument("--size_block", "-sb", required=False, type=int, help="Size of one block", default=60)
    parser.add_argument("--number_of_blocks", "-b", required=False, type=int, help="Number of blocks", default=4)
    parser.add_argument("--size_pattern", "-sp", required=False, type=int, nargs=2, help="Overall size of pattern", default=(2, 2))

    # Arguments for the Cellular Automata Formula
    parser.add_argument("--neighbourhood", "-n", required=False, type=int, help="0 for Moore, 1 for von Neumann", default=1)
    parser.add_argument("--rule_number", "-r", required=True, type=int, help= "Rule number")

    args = parser.parse_args()
    print("Arguments:", args)


    patterns = PatternGenerator(args.size_block, args.number_of_blocks, args.size_pattern, args.neighbourhood, args.rule_number)
    patterns.create_square()  