# strArr = ["a,b,c,d","a,b,c,d,-B,d"]
strArr = ["c,a,r,d","c,a,-B,r,d"]
def EquivalentKeypresses1(strArr):
    '''
    strings index everything including character ",-"
    '''
    st1 = strArr[0]
    st2 = strArr[1]
    if "-B" in st1:
        B = st1.index("-B") #index of "-B" 
        st1 = st1[:B-3] + st1[B+2:]    
    if "-B" in st2:
        B = st2.index("-B")
        st2 = st2[:B-3] + st2[B+2:]
    print(st1 == st2)
        
print (EquivalentKeypresses1(input()))



def EquivalentKeypresses2(strArr):

  # code goes here
  s1 = strArr[0]
  s2 = strArr[1]
  if "-B" in s1:
   s1List = s1.split(",-B,")
   s1 = s1List[0].rstrip(s1List[0][-1])+s1List[1]
  if "-B" in s2:
   s2List = s2.split(",-B,")
   s2 = s2List[0].rstrip(s2List[0][-1])+s2List[1]
  if s1 == s2:
    return "true"
  else:
    return "false"
    

# keep this function call here 
print (EquivalentKeypresses2(input()))