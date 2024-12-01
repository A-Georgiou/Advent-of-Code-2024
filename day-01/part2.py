puzzle = """

COPY PUZZLE DATA HERE

"""

out = puzzle.split('\n')[1:-1]

list1, dict2 = [], {}
for val in out:
  l1, l2 = [int(x) for x in val.split()]
  list1.append(l1)
  dict2[l2] = dict2.get(l2, 0) + 1

dist = 0
for l1 in list1:
  dist += (l1 * dict2.get(l1, 1))

print(dist)
