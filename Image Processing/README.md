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

1    2    3    4

5    6    7    8

9   10   11   12

13  14   15   16

**3. Output**

The program displays:

The processed image.
Each pixel value increased by 1.

Output:

2    3    4    5

6    7    8    9

10   11   12   13

14   15   16   17

**4. Algorithm**

Start.
Create a 4 × 4 image containing pixel values from 1 to 16.
Define a function process(image, start, end).
Check the base case:
If end - start <= 2, the region is small enough to process directly.
Use range(start, end) to select the rows of the current region.
For every selected row, use range(len(image[0])) to visit every pixel.
Increase each pixel value by 1.
If the region is larger than 2 rows, find the middle using:
mid = (start + end) // 2
Divide the image into two smaller regions:
First region: start to mid
Second region: mid to end
Conquer by recursively processing the first region.
Recursively process the second region.
The processed regions remain in the original image, so no separate combine operation is required.
Display the final image row by row.
Stop.

**5. Time Complexity**

Let n be the total number of pixels.

Divide: O(log n) recursive levels.
Process pixels: Every pixel is processed once → O(n).
Display image: O(n).

Therefore, the overall time complexity is:

O(n)

For our 4 × 4 example, n = 16.

**6. Space Complexity**

O(log n)

The recursive function creates calls for the divided regions. Therefore, the recursion stack requires logarithmic space.
