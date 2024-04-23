import cellpylib as cpl
import matplotlib.pyplot as plt
import argparse
import numpy as np
import sys
from PIL import Image
import os

# def custom_plot2d(array, show_grid=True):
#     plt.imshow(array, cmap='binary', origin='lower')
#     if show_grid:
#         plt.grid(color='black', linestyle='-', linewidth=0.5)
#     plt.axis('off')

# def add_grid_lines(pattern):
#     # Add grid lines to the pattern
#     grid_color = (128, 128, 128)   # Define the color of the grid lines
#     line_width = 1  # Define the width of the grid lines

#     # Add vertical grid lines
#     for x in range(pattern.shape[1] + 1):
#         pattern[:, x:x + line_width] = np.array(grid_color).reshape(1, 1, -1)

#     # Add horizontal grid lines
#     for y in range(pattern.shape[0] + 1):
#         pattern[y:y + line_width, :] = np.array(grid_color).reshape(1, 1, -1)

#     return pattern

class PatternGenerator():
    def __init__(self, size_block, number_of_blocks, size_pattern, neighbourhood, rule_number):
        self.size_block = size_block
        self.number_of_blocks = number_of_blocks
        self.size_pattern = size_pattern
        self.neighbourhood = neighbourhood
        self.rule_number = rule_number

    # Compile the info to generate one sqaure
    def generate_square(self):
        # initialize a 2D cellular automaton based off size block
        pattern_block_size = cpl.init_simple2d(self.size_block, self.size_block)

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

        pattern_block = cpl.evolve2d(pattern_block_size, timesteps=30, neighbourhood=neighborhood,
                                            apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=self.rule_number))
 
        cpl.plot2d(pattern_block, show_grid=True)
        return pattern_block

   
    # def compile_full_pattern(self):
    #     patterns_list = []

    #     # Generate square patterns
    #     for _ in range(self.number_of_blocks):
    #         square_pattern = self.generate_square()
    #         patterns_list.append(square_pattern)

    #     return patterns_list

    # def arrange_patterns(self, patterns_list):
    #     fig, axs = plt.subplots(self.size_pattern[0], self.size_pattern[1], figsize=(10, 10))
    #     for i, pattern in enumerate(patterns_list):
    #         row = i // self.size_pattern[1]
    #         col = i % self.size_pattern[1]
    #         axs[row, col].imshow(pattern[0], cmap='binary')
    #         axs[row, col].axis('off')
    #     return fig

    # def save_pattern_images(self):
    #     patterns_list = self.compile_full_pattern()
    #     img_dir = "Images"
    #     os.makedirs(img_dir, exist_ok=True)

    #     for z, pattern in enumerate(patterns_list):
    #         # Create the associated figure using Matplotlib
    #         fig = plt.figure(figsize=(5, 5))  # Adjust figsize as needed

    #         # Plot the pattern with grid lines
    #         pattern_with_grid = add_grid_lines(pattern)
    #         plt.imshow(pattern_with_grid, cmap='binary', interpolation='none')

    #         plt.axis('off')  # Turn off axis labels

    #         # Save the image
    #         img_fn = os.path.join(img_dir, f"experiment_{z}.png")
    #         plt.savefig(img_fn, dpi=300, bbox_inches="tight", pad_inches=0)
    #         plt.close(fig)

    # def combine_images(self):
    #     img_dir = "Images"
    #     image_files = [f"experiment_{i}.png" for i in range(self.number_of_blocks)]
    #     print(image_files)

    #     # Open the individual images and store them in a list
    #     images = [Image.open(os.path.join(img_dir, img_file)) for img_file in image_files]
    #     print(images)

    #     # Create a new blank image with white background
    #     combined_image = Image.new("RGB", (3 * self.size_block, 3 * self.size_block), "white")
    #     print(combined_image)

    #     # Paste each individual image into the combined image
    #     for i, img_file in enumerate(image_files):
    #         img_path = os.path.join(img_dir, img_file)
    #         img = Image.open(img_path)
    #         row = i // 2  # Determine the row index
    #         col = i % 2   # Determine the column index
    #         x_offset = col * self.size_block
    #         y_offset = row * self.size_block
    #         combined_image.paste(img, (x_offset, y_offset))

    #         # Optionally, save the intermediate combined image for debugging
    #         combined_image.save(os.path.join(img_dir, f"combined_image_debug_{i}.png"))

    #     for i, img in enumerate(images):
    #         img.show()

    #     # Save the combined image
    #     combined_image.save(os.path.join(img_dir, "combined_image.png"))
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Crochet Cellular Automata")

    # Overall arguments
    parser.add_argument("--size_block", "-sb", required=False, type=int, help="Size of one block", default=60)
    parser.add_argument("--number_of_blocks", "-b", required=False, type=int, help="Number of blocks", default=1)
    parser.add_argument("--size_pattern", "-sp", required=False, type=int, nargs=2, help="Overall size of pattern", default=(2, 2))

    # Arguments for the Cellular Automata Formula
    parser.add_argument("--neighbourhood", "-n", required=False, type=int, help="0 for Moore, 1 for von Neumann", default=1)
    parser.add_argument("--rule_number", "-r", required=True, type=int, help= "Rule number")

    args = parser.parse_args()
    print("Arguments:", args)

    pattern = PatternGenerator(args.size_block, args.number_of_blocks, args.size_pattern, args.neighbourhood, args.rule_number)
    pattern.generate_square()
    # pattern.save_pattern_images()
    # pattern.combine_images()
 
