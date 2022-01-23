inp = [[1, 2], [3, 4], [5, 6, 7]]
out = []

def reverseAll(inp):
    if type(inp) == list:
        inp.reverse()
        for i in inp:
            reverseAll(i)
            
    return inp

print(reverseAll(inp))
