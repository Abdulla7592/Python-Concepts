#this is for single line comment
#this
#is
#for multiline comment
#python ignores string literals that are not assined to variable
#so we can use string literals for writing comments
'single line comment'
"""this is 
for multi line comment
"""
#python docstring is string literals with triple quates that are given right after
#function we use _doc_ for this 
#example
def fun(a,b):
    """multiply value of a and b"""
    return a*b
print(fun.__doc__)