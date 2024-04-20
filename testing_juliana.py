import cellpylib as cpl
import matplotlib.pyplot as plt
import argparse
import numpy as np
import sys
from PIL import Image
import os

def custom_plot2d(array, show_grid=True):
    plt.imshow(array, cmap='binary', origin='lower')
    if show_grid:
        plt.grid(color='black', linestyle='-', linewidth=0.5)
    plt.axis('off')

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
 
        # pattern_block = np.squeeze(pattern_block)
        # for slice_2d in pattern_block:
        #     print(slice_2d)
        #     print() 
        # cpl.plot2d(pattern_block, show_grid=True)
        # print(type(pattern_block)) #use matplotlib 
        return pattern_block

   
    def compile_full_pattern(self):
        patterns_list = []

        # Generate square patterns
        for _ in range(self.number_of_blocks):
            square_pattern = self.generate_square()
            patterns_list.append(square_pattern)

        return patterns_list

    def arrange_patterns(self, patterns_list):
        fig, axs = plt.subplots(self.size_pattern[0], self.size_pattern[1], figsize=(10, 10))
        for i, pattern in enumerate(patterns_list):
            row = i // self.size_pattern[1]
            col = i % self.size_pattern[1]
            axs[row, col].imshow(pattern[0], cmap='binary')
            axs[row, col].axis('off')
        return fig
  
    # def save_pattern_images(self):
    #     # Generate individual images for each pattern block and save them as separate files
    #     img_dir = "individual_images"
    #     os.makedirs(img_dir, exist_ok=True)

    #     patterns_list = self.compile_full_pattern()

    #     for i, pattern_block in enumerate(patterns_list):
    #         img_path = os.path.join(img_dir, f"pattern_block_{i}.png")
    #         fig = plt.figure(figsize=(5, 5))
    #         cpl.plot2d(pattern_block, show_grid=True)
    #         plt.axis('off')
    #         plt.savefig(img_path, dpi=300, bbox_inches="tight", pad_inches=0)
    #         plt.close(fig)

    #     # Once individual pattern images are saved, combine them into one big image
    #     num_rows, num_cols = self.size_pattern
    #     combined_width = num_cols * patterns_list[0].shape[1]
    #     combined_height = num_rows * patterns_list[0].shape[0]
    #     combined_image = Image.new('RGB', (combined_width, combined_height))

    #     for i in range(len(patterns_list)):
    #         img_path = os.path.join(img_dir, f"pattern_block_{i}.png")
    #         pattern_image = Image.open(img_path)
    #         row = i // num_cols
    #         col = i % num_cols
    #         combined_image.paste(pattern_image, (col * pattern_image.width, row * pattern_image.height))

    #     combined_image.save("combined_image.png")
    # def save_pattern_images(self):
    #     # Generate individual images for each pattern block and save them as separate files
    #     img_dir = "individual_images"
    #     os.makedirs(img_dir, exist_ok=True)

    #     patterns_list = self.compile_full_pattern()

    #     for i, pattern_block in enumerate(patterns_list):
    #         img_path = os.path.join(img_dir, f"pattern_block_{i}.png")
    #         fig = plt.figure(figsize=(5, 5))
    #         cpl.plot2d(pattern_block, show_grid=True)
    #         plt.axis('off')
    #         plt.savefig(img_path, dpi=300, bbox_inches="tight", pad_inches=0)
    #         plt.close(fig)

    #     # Combine individual pattern images into one big image
    #     combined_img = self.combine_images(img_dir, len(patterns_list))
    #     combined_img.save("combined_image.png")
  
    # def combine_images(self, img_dir, num_images):
    #     # Create a blank canvas for combining images
    #     canvas_width = 2 * 5  # 2 images per row, each image is 5 units wide
    #     canvas_height = 2 * 5  # 2 images per column, each image is 5 units high
    #     canvas = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))

    #     # Load individual pattern images and paste them onto the canvas
    #     for i in range(num_images):
    #         img_path = os.path.join(img_dir, f"pattern_block_{i}.png")
    #         img = Image.open(img_path)
    #         img = img.resize((5, 5), Image.ANTIALIAS)  # Resize images to fit on canvas
    #         x_offset = (i % 2) * 5  # Calculate x-offset based on image index and canvas layout
    #         y_offset = (i // 2) * 5  # Calculate y-offset based on image index and canvas layout
    #         canvas.paste(img, (x_offset, y_offset))

    #     return canvas

    # def save_pattern_images(self):
    #     patterns_list = self.compile_full_pattern()
    #     img_dir = "photos"
    #     os.makedirs(img_dir, exist_ok=True)

    #     for z, pattern in enumerate(patterns_list):  # Iterate over patterns
    #         img_path = os.path.join(img_dir, f"pattern_{z}.png")
    #         plt.figure(figsize=(5, 5))  # Adjust figsize as needed
    #         cpl.plot2d(pattern, show_grid=True)  # Plot the pattern
    #         plt.axis('off')  # Turn off axis labels
    #         plt.savefig(img_path, dpi=300, bbox_inches="tight", pad_inches=0)  # Save the figure as PNG
    #         plt.close()  # Close the figure to free up memory

    def save_pattern_images(self):
        patterns_list = self.compile_full_pattern()
        img_dir = "Images"
        os.makedirs(img_dir, exist_ok=True)

        for z, pattern in enumerate(patterns_list):  # Iterate over patterns
            for t in range(pattern.shape[0]):  # Iterate over slices
                # Create the associated figure
                fig = plt.figure(figsize=(5, 5))  # Adjust figsize as needed
                plt.imshow(pattern[t], cmap='binary', interpolation='none')  # Plot the pattern slice
                plt.axis('off')  # Turn off axis labels
                img_fn = os.path.join(img_dir, f"experiment_{z}_slice_{t}.png")
                plt.savefig(img_fn, dpi=300, bbox_inches="tight", pad_inches=0)
                plt.close(fig)
        

if __name__ == '__main__':
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

    pattern = PatternGenerator(args.size_block, args.number_of_blocks, args.size_pattern, args.neighbourhood, args.rule_number)
    pattern.save_pattern_images()
 
 
    # def compile_full_pattern(self):
    #     patterns_list = []

    #     # Generate square patterns
    #     for _ in range(self.number_of_blocks):
    #         square_pattern = self.generate_square()
    #         patterns_list.append(square_pattern)

    #     # Compile squares into a full pattern (e.g., arrange them in a grid)
    #     full_pattern = self.arrange_patterns(patterns_list)
    #     print(type(full_pattern))
    #     return full_pattern
           
    # def arrange_patterns(self, patterns_list):
    #     # Create the associated figure
    #     num_rows, num_cols = self.size_pattern
    #     fig, axs = plt.subplots(num_rows, num_cols, figsize=(num_cols * 5, num_rows * 5))

    #     # Plot each square pattern onto the corresponding subplot
    #     for i, pattern in enumerate(patterns_list):
    #         row = i // num_cols
    #         col = i % num_cols
    #         axs[row, col].imshow(pattern[0], cmap='binary')  # Assuming pattern is a 2D array
    #         axs[row, col].axis('off')  # Turn off axis labels

    #     plt.tight_layout()  # Adjust layout to prevent overlapping
        
    #     return fig

   # def save_pattern_images(self):
    #     full_pattern = self.compile_full_pattern()
    #     img_dir = "photos"
    #     os.makedirs(img_dir, exist_ok=True)

    #     for z in range(full_pattern.shape[0]):
    #         # Create the associated figure
    #         fig = self.arrange_patterns(full_pattern[z])
    #         img_fn = os.path.join(img_dir, f"step_{z}.png")
    #         fig.savefig(img_fn, dpi=800, bbox_inches="tight", pad_inches=0)
    #         plt.close(fig)
    # def save_pattern_images(self):
    #     patterns_list = self.compile_full_pattern()
    #     img_dir = "photos"
    #     os.makedirs(img_dir, exist_ok=True)
    #     layout = self.size_pattern

    #     for z, pattern in enumerate(patterns_list):  # Iterate over patterns
    #         # Create the associated figure
    #         fig = self.arrange_patterns([pattern])  # Create figure for visualization with specified layout
    #         img_fn = os.path.join(img_dir, f"experiment_{z}.png")
    #         fig.savefig(img_fn, dpi=800, bbox_inches="tight", pad_inches=0)
    #         plt.close(fig) 
    
    
    # def save_pattern_images(self):
    #     patterns_list = self.compile_full_pattern()
    #     img_dir = "photos"
    #     os.makedirs(img_dir, exist_ok=True)

    #     # for z, pattern in enumerate(patterns_list):  # Iterate over patterns
    #     #     # Create the associated figure using cpl.plot2d
    #     #     fig = plt.figure(figsize=(5, 5))  # Adjust figsize as needed
    #     #     print (pattern[0].shape)
    #     #     cpl.plot2d(pattern[0], show_grid=True)  # Assuming pattern is a 2D array
    #     #     plt.axis('off')  # Turn off axis labels
    #     #     img_fn = os.path.join(img_dir, f"experiment_{z}.png")
    #     #     plt.savefig(img_fn, dpi=300, bbox_inches="tight", pad_inches=0)
    #     #     plt.close(fig)
    #     # for z, pattern in enumerate(patterns_list):  # Iterate over patterns
    #     #     fig = plt.figure(figsize=(5, 5))  # Adjust figsize as needed
    #     #     custom_plot2d(pattern[0], show_grid=True)  # Use the custom plotting function
    #     #     img_fn = os.path.join(img_dir, f"experiment_{z}.png")
    #     #     plt.savefig(img_fn, dpi=300, bbox_inches="tight", pad_inches=0)
    #     #     plt.close(fig)
    #     for z, pattern in enumerate(patterns_list):  # Iterate over patterns
    #         fig, axs = plt.subplots(1, len(patterns_list), figsize=(5 * len(patterns_list), 5))  # Create subplots for each pattern
    #         for i, pattern_array in enumerate(pattern): 
    #             print(pattern_array.shape) # Iterate over each pattern's array
    #             cpl.plot2d(pattern_array, show_grid=True, ax=axs[i])  # Plot the pattern array on the corresponding subplot
    #             axs[i].axis('off')  # Turn off axis labels
    #         img_fn = os.path.join(img_dir, f"experiment_{z}.png")
    #         plt.savefig(img_fn, dpi=300, bbox_inches="tight", pad_inches=0)
    #         plt.close(fig)