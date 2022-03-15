import re


'''
import re

pattern = "(.{5})(.)"

def wahsg(jxuvy):
    return re.sub(pattern, '\\2', jxuvy)

with open("my_copy_vba", "rt") as f:
    for line in f:
        print(wahsg(line.strip()), end="")
'''

dctwz = "(."
zthwa = "$"
pattern = "(.+)O(.+)"

def cgzew():
    return "O" + dctwz + "+)"

def dvci_2(jxuvy):
    return int(re.sub(pattern, '\\2', jxuvy))

def dvci_1(jxuvy):
    return int(re.sub(pattern, '\\1', jxuvy))

def ucau(wxgbv):
  return chr( dvci_2( wxgbv) - dvci_1( wxgbv) )

# print(ucau("766O825")) # testing

with open("my_copy", "rt") as f:
    for line in f:
        print(ucau(line.strip()), end="")