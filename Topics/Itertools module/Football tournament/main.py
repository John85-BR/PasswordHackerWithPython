# the variable 'teams' is already defined
import itertools
for i, j in itertools.combinations(teams,2):
    print(f"('{i}', '{j}')")