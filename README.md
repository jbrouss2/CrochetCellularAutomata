# CrochetCellularAutomata
COSC 420 Final Project

## Question: 
How can cellular automata be used to generate aesthetically pleasing lacey or mosaic crochet patterns?

## Necessary Things to Pip Install
```
pip install cellpylib
pip install numpy
pip install matplotlib
```

## How to Use
1. Download the repository
2. Make sure you have the neccessary libraries install
3. Run script by using python .\generate_1_square.py -r  [rule_number]
4. See the Cellular Automata generated

### Script Options
```
options:
  -h, --help            show this help message and exit
  --size_block SIZE_BLOCK SIZE_BLOCK, -sb SIZE_BLOCK SIZE_BLOCK
                        Size of one block
  --number_of_blocks NUMBER_OF_BLOCKS, -b NUMBER_OF_BLOCKS
                        Number of blocks
  --size_pattern SIZE_PATTERN SIZE_PATTERN, -sp SIZE_PATTERN SIZE_PATTERN
                        Overall size of pattern
  --neighbourhood NEIGHBOURHOOD, -n NEIGHBOURHOOD
                        0 for Moore, 1 for von Neumann
  --rule_number RULE_NUMBER, -r RULE_NUMBER
                        Rule number
  --timesteps TIMESTEPS, -t TIMESTEPS
                        Timesteps
  --k_value K_VALUE, -k K_VALUE
                        K value
  --lace_or_mosaic LACE_OR_MOSAIC, -lm LACE_OR_MOSAIC
                        0 for neither, 1 for lace, 2 for mosaic
```
#### Note: Use lace_pattern_generator.py to get written instructions
We will move this into the main script soon!
