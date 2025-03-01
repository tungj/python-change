rows = 5
cols = 3
# Note: you can't use this since it'll create duplicate references to the same array
# arr = [[0] * cols] * rows
arr = [[0 for x in range(cols)] for y in range(rows)]
count = 0
for x, row in enumerate(arr):
    for y, cell in enumerate(row):
        count = count + 1
        print(x, y, count)
        arr[x][y] = count

print(arr)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

def search(searchVal):
    for x, row in enumerate(arr):
        for y, cell in enumerate(row):
            if (cell == searchVal):
                print(searchVal, 'found:', x, y)
                return (x, y)
    print(searchVal, 'not found')

search(99)
# 99 not found
search(2)
# 2 found: 0 1
search(6)
# 6 found: 1 2
search(15)
# 15 found: 4 2
