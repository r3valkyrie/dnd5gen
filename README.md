# dnd5gen (WIP)
https://pypi.org/project/dnd5gen

A python 3.6+ library to generate D&D 5e characters on the fly.

Currently does not support all character options.

##### Basic Usage
```python
import dnd5gen

my_char = dnd5gen.Character()
print(vars(my_char))                # If you want a simple list of all the variables.
my_char.print_char_vals()           # If you want them printed out in a human-readable format.
```
