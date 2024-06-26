def generate_pattern(cellular_automaton, timesteps):
    # Count the zeros and ones to decide which should be holes in the lace (the one with fewer should be the lacey part)
    # Actually do the opposite of the above comment.
    # Actually changing it back for testing.
    num_zeros = 0
    num_ones = 0
    for row in cellular_automaton[timesteps-1]:
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

    graph = cellular_automaton[timesteps-1]
    
    # Pad all edges with stiches (i.e. we can't end or start a row with empty space, the last and first rows cannot have empty space either)
    pattern_graph = np.pad(graph, ((1, 1), (1, 1)), mode='constant', constant_values=stitch)
    # First tell the user to make a foundation chain the length of pattern_graph + 2
    found_ch = (len(pattern_graph[0]))*2 + 2
    foundation_ch = str(found_ch)
    foundation = "Foundation Row: ch " + foundation_ch
    # Map the 0's and 1's to actual crochet stitches (half double crochet and chain spaces)
    stitch_map = {stitch: "dc", space: "ch"}
    # Go row by row, element by element, counting the number of stitches until it changes to the different stitch, then counting those.
    rows = []
    for i, row in enumerate(reversed(pattern_graph)):
        row_text = f"Row {i + 1}: "
        current_stitch = None
        current_count = 0
        # Rows are worked back and forth, hence we need to read the graph back and forth to generate the pattern.
        if i % 2 == 0:
            for stitch_i in reversed(row):
                if stitch_i == current_stitch:
                    current_count += 2
                elif stitch_i != current_stitch and current_stitch == None:
                    current_stitch = stitch_i
                    current_count += 2
                elif stitch_i != current_stitch and current_stitch is not None:
                    row_text += f", {current_count} {stitch_map[current_stitch]}"
                    current_stitch = stitch_i
                    current_count = 2
        else:
            for stitch_i in row:
                if stitch_i == current_stitch:
                    current_count += 2
                elif stitch_i != current_stitch and current_stitch == None:
                    current_stitch = stitch_i
                    current_count += 2
                elif stitch_i != current_stitch and current_stitch is not None:
                    row_text += f", {current_count} {stitch_map[current_stitch]}"
                    current_stitch = stitch_i
                    current_count = 2
        row_text += f", {current_count} {stitch_map[current_stitch]}"
        row_text = row_text.replace(', ', '', 1)

        # Reformant line
        line = row_text# Reformant line
        row_number, instructions = line.split(': ')
        
                
        new_line = ""
        instructions = line.split(", ")  # Split the line into individual instructions
    
        # Initialize an empty list to store instructions sets
        instruction_sets = []

        # Group every two instructions together
        for i in range(0, len(instructions), 2):
            group = instructions[i:i+2]
            instruction_sets.append(", ".join(group))

        # See if the next instruction set matches the current instruction set
        i = 0
        while i < len(instruction_sets):
            j = i + 1
            # Count the number of matches/repeat instructions sets you see
            repeats = 1
            #print(instruction_sets[i])
            while (j < len(instruction_sets)):
                #print(instruction_sets[j])
                if instruction_sets[j] == instruction_sets[i]:
                    #print("repeat")
                    repeats += 1
                    j += 1
                else:
                    break
            if repeats == 1:
                new_line += f", {instruction_sets[i]}"
                i += 1
            elif repeats > 0:
                new_line += f", ({instruction_sets[i]})*{repeats}"
                i += repeats

        formatted_instructions = new_line
        formatted_instructions = formatted_instructions.rstrip("\n")
        row_text = f"{row_number}: {formatted_instructions}"
        row_text = row_text.replace(', ', '', 1)
        rows.append(formatted_instructions)

    # Write the text to a file
    title = "Cellular Automata Crochet Pattern"
    stitch_defs = "Stitch definitions: dc = double crochet, ch = chain"
    note = "Note: Please note that the ch 3 and turn counts as the first dc."
    # Write the text to a file
    with open("complete_pattern.txt", "w") as file:
        file.write(title)
        file.write("\n")
        file.write(stitch_defs)
        file.write("\n")
        file.write(note)
        for i, row in enumerate(formatted_pattern):
            file.write("\n")
            file.write(foundation)
            file.write("\n")
            if i == 0:
                row += "."
                file.write(row)
            if i != 0:
                row += ", ch 3 and turn."
                file.write(row)
            file.write("\n")

    
    
            
            
