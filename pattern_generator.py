import os
import numpy as np
import sys
import matplotlib.pyplot as plt
import argparse
import time

class PatternGenerator():
    def __init__ (self, num_experiments):
        self.num_experiments = num_experiments
        

    def simulate(self):


        # Create the associated figure 
        fig = plt.figure()
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off() 
        fig.add_axes(ax)
        ax.imshow(self.palette[self.board.astype(int)]) 
        img_fn = self.exp_dir + "/experiment_" + str(experiment) + "_step_" + str(z) + ".png"
        plt.savefig(img_fn, dpi=800, bbox_inches="tight", pad_inches=0)
        plt.close(fig)

    if __name__ == '__main__':
        print ("Hello World!")
        parser = argparse.ArgumentParser(description="Crochet Cellular Automata")
        
        # Determine the arguments we wish to have
        parser.add_argument("--")

        args = parser.parse_args()

        pattern = PatternGenerator(args.expereiments, args )
        pattern.simulate()
