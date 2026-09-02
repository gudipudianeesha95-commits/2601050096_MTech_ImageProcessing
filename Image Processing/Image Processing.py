def process(image, start, end):

    # Base Case
    if end - start <= 2:
        for i in range(start, end):
            for j in range(len(image[0])):
                image[i][j] += 1
        return

    # Divide
    mid = (start + end) // 2

    # Process two smaller regions
    process(image, start, mid)
    process(image, mid, end)


# Simple Image
image = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Process image
process(image, 0, 4)

# Display result
for row in image:
    print(row)