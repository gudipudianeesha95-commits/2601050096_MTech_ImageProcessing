**Image Processing Using Divide-and-Conquer**

**An image contains millions of pixels. You want to perform an operation independently on different regions of the image. Question: How can divide-and-conquer be used to solve this problem?**

**1. Objective**

To develop a simple Python-based image processing program using the Divide-and-Conquer technique, where an image is divided into smaller regions and an operation is performed independently on each region.

In this example, the image contains 16 pixels, and we increase the value of every pixel by 1.

**2. Input**

The program accepts:

A 2D image represented as a list.
Starting row index start.
Ending row index end.
Pixel values of the image.

Example image:

1      2      3      4

5      6      7      8

9   10   11   12

13  14   15   16

**3. Output**

The program displays:

The processed image.
Each pixel value increased by 1.

Output:

2      3      4      5

6      7      8      9

10   11   12   13

14   15   16   17

**4. Algorithm**

1. Start.

2. Create a 4 × 4 image containing pixel values from 1 to 16.

3. Define a function process(image, start, end).

4. Check the base case:

5. If end - start <= 2, the region is small enough to process directly.

6. Use range(start, end) to select the rows of the current region.

7. For every selected row, use range(len(image[0])) to visit every pixel.

8. Increase each pixel value by 1.

9. If the region is larger than 2 rows, find the middle using:

10. mid = (start + end) // 2

11. Divide the image into two smaller regions:

12. First region: start to mid

13. Second region: mid to end

14. Conquer by recursively processing the first region.

15. Recursively process the second region.

16. The processed regions remain in the original image, so no separate combine operation is required.

17. Display the final image row by row.

18. Stop.

**5. Python Implementation**

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

**6. Output**

[2, 3, 4, 5]

[6, 7, 8, 9]

[10, 11, 12, 13]

[14, 15, 16, 17]

**7. Time Complexity**

Let n be the total number of pixels.

Divide: O(log n) recursive levels.
Process pixels: Every pixel is processed once → O(n).
Display image: O(n).

Therefore, the overall time complexity is:

O(n)

For our 4 × 4 example, n = 16.

**8. Space Complexity**

O(log n)

The recursive function creates calls for the divided regions. Therefore, the recursion stack requires logarithmic space.
