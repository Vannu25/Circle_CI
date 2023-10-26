# Modules : The way of organizing the code and py files is called modules.

import utility
import random
import datetime
from array import array

ar = array('i', [1, 2, 3])
print(ar)
print(datetime.date.today())
print(random)
print(utility.mul(2, 3))

# different ways to import
# from time import time
# from Decorators import decorators
#  utility - direct import as it is in same package or directory
