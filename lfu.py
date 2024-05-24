f,r = map(int,input("enter no. frame and no. refrences").split())
ref = list(map(int, input("Enter the reference string (space-separated): ").split()))
frame = [-1] * f
pf = 0
victim = -1
# Optimal page replacement algorithm
print("\nPage replacement process:")
for i in range(r):
    flag = False
    print(f"\n\tReference no {ref[i]} ->\t", end="")
    # Check if page is already in frame
    if ref[i] in frame:
        flag = True
    if not flag:
        pf += 1
        if -1 in frame:
            victim = frame.index(-1)
        else:
            opt = [r] * f  # default to a large value (nor)
            for j in range(f):
                if frame[j] in ref[i+1:]:
                    opt[j] = ref[i+1:].index(frame[j]) + i + 1
            victim = opt.index(max(opt))
        frame[victim] = ref[i]

    print(" ".join(f"{x if x != -1 else '-'}" for x in frame))
print(f"\nNumber of page faults: {pf}")
