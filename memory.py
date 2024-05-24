# Input memory sizes and partition size
pmsize = int(input("Enter the Size of Physical memory: "))
lmsize = int(input("Enter the size of Logical memory: "))
psize = int(input("Enter the partition size: "))

# Calculate number of frames and pages
frame_count = pmsize // psize
page_count = lmsize // psize

# Print memory divisions
print(f"\nThe physical memory is divided into {frame_count} frames")
print(f"The Logical memory is divided into {page_count} pages\n")

# Initialize page table and frame table
page_table = [{'frame_number': -1, 'presence_bit': -1} for _ in range(page_count)]
frame_table = [-1] * frame_count

# Assign pages to frames
for i in range(page_count):
    frame_number = int(input(f"Enter the Frame number where page {i} must be placed: "))
    frame_table[frame_number] = i
    page_table[i]['frame_number'] = frame_number
    page_table[i]['presence_bit'] = 1

# Display page table
print("\nPAGE TABLE")
print("Page Address\tFrame No.\tPresence Bit")
for i in range(page_count):
    print(f"{i}\t\t{page_table[i]['frame_number']}\t\t{page_table[i]['presence_bit']}")

# Display frame table
print("\nFRAME TABLE")
print("Frame Address\tPage No")
for i in range(frame_count):
    print(f"{i}\t\t{frame_table[i]}")

# Logical to physical address translation
base_address = int(input("\nEnter the Base Address: "))
logical_address = int(input("Enter the Logical Address: "))
page_number = logical_address // psize
offset = logical_address % psize

if page_table[page_number]['presence_bit'] == 1:
    physical_address = base_address + (page_table[page_number]['frame_number'] * psize) + offset
    print(f"\nThe Physical Address where the instruction is present: {physical_address}")
else:
    print("Invalid logical address: page not in memory")
