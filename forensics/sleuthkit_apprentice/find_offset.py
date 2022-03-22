import sys
import math

# for automatically find the offset of the file in the image

sector_size = 512
block_size = 1024

if len(sys.argv) < 3:
    print(f"\nUsage: python {sys.argv[0]} file_offset disk_start_sector (OPTIONAL: sector_size block_size)\n")

else:
    if len(sys.argv) >= 4:
        sector_size = int(sys.argv[3])
    if len(sys.argv) >= 5:
        block_size = int(sys.argv[4])

    print(math.floor((int(sys.argv[1]) - int(sys.argv[2]) * sector_size)/block_size))