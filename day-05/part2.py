import os
import sys
from collections import defaultdict, deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def parse_updates(lines):
    updates = []
    for line in lines:
        update = list(map(int, line.split(',')))
        updates.append(update)
    return updates

def parse_rules(lines):
    rules = {}
    for line in lines:
        before, after = map(int, line.split('|'))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)
    return rules

def is_valid_order(pages, rules):
    positions = {num: i for i, num in enumerate(pages)}
    for page in pages:
        if page in rules:
            for must_come_after in rules[page]:
                if must_come_after in positions and positions[must_come_after] < positions[page]:
                    return False
    return True

def topological_sort(nums, rules):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    nums_set = set(nums)
    for before in rules:
        if before in nums_set:
            for after in rules[before]:
                if after in nums_set:
                    graph[before].add(after)
                    in_degree[after] += 1
    
    queue = deque()
    for num in nums_set:
        if in_degree[num] == 0:
            queue.append(num)
    
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

rules, updates = Parser(file_path='input.txt').parse_sections(str)
rules = parse_rules(rules.splitlines())
updates = parse_updates(updates.splitlines())

total = 0
for update in updates:
    if not is_valid_order(update, rules):
        sorted_update = topological_sort(update, rules)
        middle_idx = len(sorted_update) // 2
        total += sorted_update[middle_idx]

print("Total:", total)