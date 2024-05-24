# Read input from the user
n = int(input("Enter number of files: "))
file_names = []
start_blocks = []
sizes = []
all_blocks = []
for i in range(n):
    fname = input("Enter file name: ")
    start = int(input("Enter starting block: "))
    size = int(input("Enter number of blocks: "))
    blocks = list(map(int, input("Enter block numbers (space-separated): ").split()))
    file_names.append(fname)
    start_blocks.append(start)
    sizes.append(size)
    all_blocks.append([start] + blocks)
print("\nFile\tStart\tSize\tBlocks")
for i in range(len(file_names)):
    print(f"{file_names[i]}\t{start_blocks[i]}\t{sizes[i]}\t", end="")
    print(" ---> ".join(map(str, all_blocks[i][:-1])), end=" ---> ")
    print(all_blocks[i][-1])
