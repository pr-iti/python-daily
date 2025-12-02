def generator():
    for i in range(5000):
        # heavy computations//
        yield i

# generates fly values not in memory locations
#-- used for saving memory 
gen = generator()

for j in gen :
    print(j)

