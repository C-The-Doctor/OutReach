# Python3 code to demonstrate
# the random generation of string id's

import random
import string

# defining function for random
# string id with parameter
def Generate_Link(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

# function call for random string
# generation with size 8 and string
print (Generate_Link(10, "AEIOSUMA23"))
