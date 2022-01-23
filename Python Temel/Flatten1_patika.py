inp = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
out = []

def flatten(inp):
    
    for i in inp:
        if type(i) == list :
            flatten(i)
        else:
            out.append(i)
    return out

print(flatten(inp))
        

    