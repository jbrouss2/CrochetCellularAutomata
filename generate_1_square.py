import cellpylib as cpl
import matplotlib.pyplot as plt
import argparse
import numpy as np
import sys
from PIL import Image
import os

class PatternGenerator():
    def __init__(self, size_block, number_of_blocks, size_pattern, neighbourhood, rule_number, timesteps, k_value):
        self.size_block = size_block
        self.number_of_blocks = number_of_blocks
        self.size_pattern = size_pattern
        self.neighbourhood = neighbourhood
        self.rule_number = rule_number
        self.timesteps = timesteps
        self.k_value = k_value

    # Compile the info to generate one sqaure
    def generate_square(self):
        # initialize a 2D cellular automaton based off size block
        pattern_block_size = cpl.init_simple2d(self.size_block[0], self.size_block[1])

        # Determine the neighborhood
        neighborhood = ""
        if self.neighbourhood == 0:
            neighborhood = "Moore"
        elif self.neighbourhood == 1:
            neighborhood = "von Neumann"
        else:
            print("Error: Invalid neighbourhood")
            sys.exit(1)

        # print(neighborhood)

        pattern_block = cpl.evolve2d(pattern_block_size, timesteps=self.timesteps, neighbourhood=neighborhood,
                                            apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=self.k_value, rule=self.rule_number))
 
        cpl.plot2d(pattern_block, show_grid=True)
        return pattern_block

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Crochet Cellular Automata")

    # Overall arguments
    parser.add_argument("--size_block", "-sb", required=False, type=int, nargs=2, help="Size of one block", default=(60,60))

    # Not in use anymore - no functionality
    parser.add_argument("--number_of_blocks", "-b", required=False, type=int, help="Number of blocks", default=1)
    parser.add_argument("--size_pattern", "-sp", required=False, type=int, nargs=2, help="Overall size of pattern", default=(2, 2))

    # Arguments for the Cellular Automata Formula
    parser.add_argument("--neighbourhood", "-n", required=False, type=int, help="0 for Moore, 1 for von Neumann", default=1)
    parser.add_argument("--rule_number", "-r", required=True, type=int, help= "Rule number")
    parser.add_argument("--timesteps", "-t", required=False, type=int, help="Timesteps", default=30)
    parser.add_argument("--k_value", "-k", required=False, type=int, help="K value", default=2)

    args = parser.parse_args()
    print("Arguments:", args)

    pattern = PatternGenerator(args.size_block, args.number_of_blocks, args.size_pattern, args.neighbourhood, args.rule_number, args.timesteps, args.k_value)
    pattern.generate_square()