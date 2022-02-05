# Useful patterns we noticed

- Get array of split input of integers

```python
[int(x) for x in input().split()]
```

- For sorting a 2D array based on 0th column

```py
arr.sort(key=lambda x: x[0])
```

Note: this sorts the array directly and overwrites it. Does not return a value

- For taking input of space-separated data

```py
list(map(int,input().split())) # Replace int with str for strings
```

- For outputting to one decimal place:

```py 
print( round(ans, 1) )
```

- Find all permutations of characters in a string

```py 
import itertools
s = 'ABC'
nums = list(s)
perms = list(itertools.permutations(nums)) # Recursion Tree
```

- Remove duplicates from an array

```py
mylist = list(dict.fromkeys(mylist))
```

# Regular Expression Common Uses
```py
import re
```

- Find all occurrences of a substring in a string

```py
re.findall(substring, string) # Substring can also be a pattern
```
