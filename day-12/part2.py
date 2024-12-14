import os
import sys
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def calculate_shape(garden_plot, start_i, start_j):
    current_char = garden_plot[start_i][start_j]
    region_cells = set()
    queue = deque([(start_i, start_j)])
    area = 0
    
    while queue:
        i, j = queue.popleft()
        if (i, j) in region_cells:
            continue
            
        if (i < 0 or i >= len(garden_plot) or 
            j < 0 or j >= len(garden_plot[0]) or 
            garden_plot[i][j] != current_char):
            continue
            
        region_cells.add((i, j))
        area += 1
        
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            queue.append((i + di, j + dj))
    
    corners = 0
    for i, j in region_cells:
        orthogonal_pairs = [
            ((0, 1), (1, 0)),   
            ((0, 1), (-1, 0)),  
            ((0, -1), (1, 0)),  
            ((0, -1), (-1, 0))  
        ]
        
        for dir1, dir2 in orthogonal_pairs:
            n1 = (i + dir1[0], j + dir1[1])
            n2 = (i + dir2[0], j + dir2[1])
            corner = (i + dir1[0] + dir2[0], j + dir1[1] + dir2[1])
            
            if (n1 not in region_cells and n2 not in region_cells):
                corners += 1
            elif (n1 in region_cells and n2 in region_cells and 
                  corner not in region_cells):
                corners += 1
    
    for i, j in region_cells:
        garden_plot[i][j] = '.'
        
    return (area * corners), garden_plot

if __name__ == "__main__":
    garden_plot = Parser(file_path='input.txt').parse_lines(list, flatten=True)
    total_count = 0
    for i in range(len(garden_plot)):
        for j in range(len(garden_plot[0])):
            if garden_plot[i][j] != '.':
                region_value, garden_plot = calculate_shape(garden_plot, i, j)
                total_count += region_value
                
    print("Result:", total_count)