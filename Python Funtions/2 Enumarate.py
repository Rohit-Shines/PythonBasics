# The enumerate() method adds a counter to an iterable and returns it (the enumerate object).

languages = ['Python', 'Java', 'JavaScript']
print(list(enumerate(languages)))
# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
print(list(enumerate(languages,10)))
# [(10, 'Python'), (11, 'Java'), (12, 'JavaScript')]


### for enumarate
grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
  print(item) # (0, 'bread') (1, 'milk') (2, 'butter')


for count, item in enumerate(grocery):
  print(count, item) # 0 bread  1 milk  2 butter

