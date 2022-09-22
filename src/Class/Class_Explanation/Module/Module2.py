import Module1
import Module1 as mod
from Module1 import *
from Module1 import x, add, sub

import Package1.package_module

print(mod.x)
print(mod.add(2, 3))
print(f"from Module2 name: {__name__}")