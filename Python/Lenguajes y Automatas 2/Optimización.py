import random
import time
data = 0
timp = time.time()
print(random.randint(0,5))
print(random.randint(0,5))
print(random.randint(0,5))
print(random.randint(0,5))
print("\n")
res = time.time() - timp
print(f"{res:.5f}")