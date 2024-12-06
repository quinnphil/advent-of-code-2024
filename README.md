# Advent of Code 2024


### Puzzles  

⭐⭐ [Day 1: Historian Hysteria](https://adventofcode.com/2024/day/1)     
- two lists of numbers     
- P1: return sum of distance between sorted pairs  
- P2: return sum of number from first list multiplied by number  of times it appear in second list

⭐⭐ [Day 2: Red-Nosed Reports](https://adventofcode.com/2024/day/2)  
- input is list of reports - each report has multiple levels (integers)
- P1: determine safe reports by checking contiuning increase or decrease in levels  
- P2: determine safe reports by allowing at most one of the levels to be incorrect  

⭐⭐ [Day 3: Mull It Over](https://adventofcode.com/2024/day/3)  
- input is a contiuous string representing corrupt memory
- P1: find mul(a,b) pairs and calculate sum product 
- P2: find do() and don't() operators and only calculate sum product if in a do() state

⭐⭐ [Day 4: Ceres Search](https://adventofcode.com/2024/day/4)  
- input is a list of strings representing a word search grid
- P1: XMAS in any direction
- P2: find MAS in the shape of an X

⭐⭐ [Day 5: Print Queue](https://adventofcode.com/2024/day/8)  
- input:
  -  list of rules about page orders  
  -  list of updates with pages in order  
- P1: Find all updates with the correct page order 
- P2: Fix the incorrectly ordered pages

⭐⭐ [Day 6: Guard Gallivant](https://adventofcode.com/2024/day/6)  
- input:
  -  lab layout  
  -  guard position
- P1: Find distinct positions before guard leaves map
- P2: Find positions where obstacle could be added to cause loop


⭐⭐ [Day 7: Bridge Repair](https://adventofcode.com/2024/day/7)  
Synopsis:  
- input:
  - list of integer equations that are missing operators
- P1: Use addition and multiplication to determine valid equations
- P2: Use addition, multiplicatin and combination to determine valid equations


### Links  
[Advent of Code 2024](https://adventofcode.com/2024)     
[Advent of Code 2024 - Private Leaderboard](https://adventofcode.com/2024/leaderboard/private)  
[Advent of Code 2024 - Personal Times](https://adventofcode.com/2024/leaderboard/self)  


### Tweet
⭐⭐ Day 7: Bridge Repair 
adventofcode.com/2024/day/7

P1: Create first class functions for addition and multiplier.  Apply all permentations of these to the integer values.  Sum totals of valid equations.
P2: Add combination first class function.  Same as P1.
#aoc2024 #python
Code: https://github.com/quinnphil/advent-of-code-2024/blob/main/day_07.py
