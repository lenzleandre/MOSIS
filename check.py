from case3_checker import Case3Checker
from case4_checker import Case4Checker

from charstream import CharacterStream


with open('trace.txt', 'r') as myfile:
    data=myfile.read()
a = CharacterStream(data)
case4test = Case4Checker(a)
if case4test.scan():
    print("Case 4 validated correctly")
else:
    print("Error found in case 4")
