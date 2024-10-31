#!/usr/bin/env python3

import random
a=int(input("a:"))
b=random.randint(-10, 10)

if b!=0:
   result = a/b
   print(f"a/b={result}")
else:
   print("error! b=0")
