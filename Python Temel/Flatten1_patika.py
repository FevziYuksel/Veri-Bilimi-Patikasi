inp1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
inp = [(15,7),{"a":(3,2)}, [7,(3,4)]]
out = []

def flatten(inp):
    
    for i in inp:
        if type(i) == tuple or type(i) == list or type(i) == set or type(i) == dict :
            flatten(i)
        else:
            out.append(i)
    return out

print(flatten(inp))
        

    
