l1 = ["a", "b"]
l2 = ["z", "x"]

# don't do...
for i in range(len(l1)):
    print(f"1.){l1[i], l2[i]}")

# do...
for l1, l2 in zip(l1, l2):
    print(f"2.){l1, l2}")