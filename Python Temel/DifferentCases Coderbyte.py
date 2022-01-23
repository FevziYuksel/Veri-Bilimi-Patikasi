import re

def DifferentCases(strParam):

  # code goes here
  strParam = re.sub("[^a-zA-Z]"," ",strParam)

  strList = strParam.split(" ")
  returnStr = ""
  for word in strList:
    word = word.lower()
    word = word[0].upper() + word[1:]
    returnStr += word


  return returnStr
 

# keep this function call here 
print (DifferentCases(input()))