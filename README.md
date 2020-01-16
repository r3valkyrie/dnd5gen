# dnd5gen (WIP)

A python 3.6+ library to generate D&D 5e characters on the fly.

Currently does not support all character options.

##### Basic Usage
```python
from dnd5gen import character

my_char = character.Character()
print(vars(my_char))
```