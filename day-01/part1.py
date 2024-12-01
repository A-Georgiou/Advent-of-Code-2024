puzzle = """

COPY PUZZLE DATA HERE

"""

out = puzzle.split('\n')[1:-1]

list1, list2 = [], []
for val in out:
  l1, l2 = [int(x) for x in val.split()]
  list1.append(l1)
  list2.append(l2)
list1.sort()
list2.sort()

dist = 0
for l1, l2 in zip(list1, list2):
  dist += abs(l1-l2)

print(dist)
