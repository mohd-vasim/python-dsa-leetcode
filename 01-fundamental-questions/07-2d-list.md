- Coding Exercise 75: Pascal's Triangle
- Coding Exercise 76: Rotate Image
- Coding Exercise 77: Matrix obtained by Rotation or not?
- Coding Exercise 78: Spiral Matrix
- Coding Exercise 79: Search a 2D Matrix
- Coding Exercise 80: Reshape Matrix

### **1. Pascal's Triangle**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it. The first row is row 0, which is [1].



Input Parameters:

numRows (int): The number of rows of Pascal's triangle to generate.

Output:

List[List[int]]: A list of lists where each list represents a row in Pascal's triangle.



Example:

Input: numRows = 3
Output: [
  [1],
  [1, 1],
  [1, 2, 1]
]
 
Input: numRows = 1
Output: [
  [1]
]
 
Input: numRows = 5
Output: [
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1]
]


### **2. Rotate Image**
Asked in Companies:

Zoho

Amazon

Schlumberger

Facebook



Description:
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees clockwise. The rotation should be done in-place, meaning you have to modify the input matrix directly without using any additional matrix for storage.



Input Parameters:

matrix (List[List[int]]): A 2D list of integers representing the matrix of size n x n.

Output:

The function should modify the matrix in-place. No need to return anything.



Example:

Input: matrix = [[5, 1, 9, 11],
                 [2, 4, 8, 10],
                 [13, 3, 6, 7],
                 [15, 14, 12, 16]]
Output: [[15, 13, 2, 5],
         [14, 3, 4, 1],
         [12, 6, 8, 9],
         [16, 7, 10, 11]]
 
 
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
Output: [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]


### **3. Matrix obtained by Rotation or not?**
Asked in Companies:

Oracle

Apple

Wipro



Description:
You are given two n x n binary matrices mat and target. Your task is to determine whether it is possible to make mat equal to target by rotating mat in 90-degree increments (clockwise). You can rotate mat by 90, 180, or 270 degrees, or leave it unchanged.



Input Parameters:

mat (List[List[int]]): A n x n binary matrix.

target (List[List[int]]): A n x n binary matrix.

Output:

bool: Return True if mat can be made equal to target by rotating it, otherwise return False.



Example:

Input: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]], target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
Output: True
 
Input: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
Output: False


### **4. Spiral Matrix**
Asked in Companies:

Apple

Adobe

Paytm

Jio



Description:
You are given an m x n matrix. Write a function that returns all the elements of the matrix in spiral order, starting from the top-left corner, moving right across the top row, then down the last column, then left across the bottom row, and then up the first column, repeating this process until all the elements have been visited.



Input Parameters:

matrix (List[List[int]]): A 2D list representing the matrix of size m x n.

Output:

List[int]: A list of integers representing the elements of the matrix in spiral order.



Example:

Input: matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
 
Input: matrix = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]


### **5. Search a 2D Matrix**
Asked in Companies:

Salesforce

Flipkart

Amazon



Description:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.

The first integer of each row is greater than the last integer of the previous row.

Write a function that takes an integer target and returns True if target is in matrix, or False otherwise. You must solve this problem with a time complexity better than O(m * n).



Input Parameters:

matrix (List[List[int]]): A 2D list representing an m x n matrix.

target (int): The target integer to search for in the matrix.

Output:

bool: Return True if the target is found, otherwise return False.



Example:

Input: matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]], target = 13
Output: False
 
Input: matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]], target = 3
Output: True

### **6. Reshape Matrix**
Asked in Companies:

Dunzo

Flipkart



Description:
In MATLAB, there is a handy function called reshape that reshapes a matrix of dimensions m x n into a new one with a different size r x c keeping its original data in row-traversing order.

You are given an m x n matrix mat and two integers r and c representing the number of rows and columns of the wanted reshaped matrix. The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with the given parameters is possible and legal, output the new reshaped matrix. Otherwise, output the original matrix.



Input Parameters:

mat (List[List[int]]): A 2D list representing an m x n matrix.

r (int): The number of rows for the reshaped matrix.

c (int): The number of columns for the reshaped matrix.



Output:

List[List[int]]: The reshaped matrix or the original matrix if reshaping isn't possible.



Example:

Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
Output: [[1, 2, 3, 4]]
 
Input: mat = [[1, 2], [3, 4]], r = 2, c = 4
Output: [[1, 2], [3, 4]]

