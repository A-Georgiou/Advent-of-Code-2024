import os
import sys
from collections import defaultdict
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

rules, updates = Parser(file_path='input.txt').parse_sections(str)
rules = parse_rules(rules.splitlines())
updates = parse_updates(updates.splitlines())

total = 0
for update in updates:
    if is_valid_order(update, rules):
        middle_idx = len(update) // 2
        total += update[middle_idx]

print("Total:", total)