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

⭐⭐ [Day 8: Resonant Collinearity](https://adventofcode.com/2024/day/8)  
Synopsis:  
- input:
  - list of antanna positons
- P1: Determine antinodes
- P2: Find more antinodes

⭐⭐ [Day 9: Disk Fragmenter](https://adventofcode.com/2024/day/9)  
Synopsis:  
- input:
  - disk to defrag
- P1: Defrag using all available space
- P2: Defrag using continuous space only

⭐⭐ [Day 10: Hoof It](https://adventofcode.com/2024/day/10)  
Synopsis:  
- input:
  - x,y,h topology map
- P1: Find count trails that lead to trailhead
- P2: Determine trail rating for trailhead

⭐⭐ [Day 11: Plutonian Pebbles](https://adventofcode.com/2024/day/11)  
Synopsis:  
- input:
  - list of stones
- P1: Find number of stones after blinking 25 times
- P2: Find number of stones after blinking 75 times

### Links  
[Advent of Code 2024](https://adventofcode.com/2024)     
[Advent of Code 2024 - Private Leaderboard](https://adventofcode.com/2024/leaderboard/private)  
[Advent of Code 2024 - Personal Times](https://adventofcode.com/2024/leaderboard/self)  

[Github - Leftfish](https://github.com/Leftfish/Advent-of-Code-2023)

### Tweet
⭐⭐ Day 11: Plutonian Pebbles
https://adventofcode.com/2024/day/11

- P1: Count stoned after 25 blinks
- P2: Use function call caching to count stones after 75 blinks


P1: For each antenna pair - determine antinode position
P2: For each antenna pair - keep adding antinodes while within grid
#aoc2024 #python
Code: [needs tidyinging up]
