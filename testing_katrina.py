import cellpylib as cpl
import numpy as np

# initialize a 60x60 2D cellular automaton
cellular_automaton = cpl.init_simple2d(18, 18)

# evolve the cellular automaton for 30 time steps,
#  applying totalistic rule 126 to each cell with a Moore neighbourhood
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=30, neighbourhood='von Neumann',
                                  apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=22))

cpl.plot2d(cellular_automaton, show_grid = True)
print(cellular_automaton[29])

#von nueman 22
#print(type(cellular_automaton))
#print(cellular_automaton.shape)


##### pattern generator #######

# Count the zeros and ones to decide which should be holes in the lace (the one with fewer should be the lacey part)
num_zeros = 0
num_ones = 0
for row in cellular_automaton[29]:
    for element in row:
        if element == 0:
            num_zeros += 1
        elif element == 1:
            num_ones += 1

# Using zeros as stitches and ones as holes
if (num_zeros >= num_ones):
    print("more zeros")
    stitch = 0
    space = 1
# Using ones as stitches and zeros as holes
else: 
    print("more ones")
    stitch = 1
    space  = 0

def generate_lace_pattern(graph, stitch, space):
    # Pad all edges with stiches (i.e. we can't end or start a row with empty space, the last and first rows cannot have empty space either)
    pattern_graph = np.pad(graph, ((1, 1), (1, 1)), mode='constant', constant_values=stitch)
    # First tell the user to make a foundation chain the length of pattern_graph + 2
    foundation_ch = str(len(pattern_graph[0]) + 2)
    foundation = "Foundation Row: ch " + foundation_ch
    # Map the 0's and 1's to actual crochet stitches (half double crochet and chain spaces)
    stitch_map = {stitch: "hdc", space: "ch"}
    # Go row by row, element by element, counting the number of stitches until it changes to the different stitch, then counting those.
    rows = []
    for i, row in enumerate(reversed(pattern_graph)):
        row_text = f"Row {i + 1}: "
        current_stitch = None
        current_count = 0
        if i % 2 == 0:
            for stitch_i in reversed(row):
                if stitch_i == current_stitch:
                    current_count += 1
                elif stitch_i != current_stitch and current_stitch == None:
                    current_stitch = stitch_i
                    current_count += 1
                elif stitch_i != current_stitch and current_stitch is not None:
                    row_text += f", {current_count} {stitch_map[current_stitch]}"
                    current_stitch = stitch_i
                    current_count = 1
        else:
            for stitch_i in row:
                if stitch_i == current_stitch:
                    current_count += 1
                elif stitch_i != current_stitch and current_stitch == None:
                    current_stitch = stitch_i
                    current_count += 1
                elif stitch_i != current_stitch and current_stitch is not None:
                    row_text += f", {current_count} {stitch_map[current_stitch]}"
                    current_stitch = stitch_i
                    current_count = 1
        row_text += f", {current_count} {stitch_map[current_stitch]}"
        row_text = row_text.replace(', ', '', 1)
        rows.append(row_text)

    # Write the text to a file
    with open("pattern.txt", "w") as file:
         file.write(foundation)
         file.write("\n")
         file.write("\n".join(rows))

    # Each row of the array is a row of the pattern
    return pattern_graph

graph = generate_lace_pattern(cellular_automaton[29], stitch, space)
print(graph)

