1. Coding Exercise 1: Square of side 'N'
2. Coding Exercise 2: Hollow Square of side 'N'
3. Coding Exercise 3: Rectangle Pattern
4. Coding Exercise 4: Right Angled Triangle
5. Coding Exercise 5: Inverted Right Angled Triangle
6. Coding Exercise 6: Pyramid Pattern
7. Coding Exercise 7: Inverted Pyramid Pattern
8. Coding Exercise 8: Right Angled Triangle with Numbers
9. Coding Exercise 9: Floyds Triangle
10. Coding Exercise 10: Diamond Pattern
11. Coding Exercise 11: Right Angled Triangle II
12. Coding Exercise 12: Sandglass Pattern
13. Coding Exercise 13: Hollow Right Triangle
14. Coding Exercise 14: Hollow Inverted Right Triangle
15. Coding Exercise 15: Number Pyramid Pattern

## Exercise 1

## Square of side 'N'
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.



Input Parameters:

n (int): The size of the square (number of rows and columns).



Output:

A list of strings where each string is a row of n characters.



Example:
```
Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']
```



```python
n = 5
l = []
for i in range(n):
    l.append("*"*n)
print(l)
```

    ['*****', '*****', '*****', '*****', '*****']


## Exercise 2

### Hollow Square of side 'N'
#### Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).



#### Input Parameters:

n (int): The size of the square (number of rows and columns).



#### Output:

A list of strings where each string is a row of n characters, representing a hollow square.



#### Example:

```
Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
```


```python
n = 1
l = []
for i in range(n):
    k = "*"*n
    if i==0 or i==(n-1):
        l.append(k)
    else:
        spaces = (n - 2) * " "
        k = "*"+spaces+"*"
        l.append(k)  

print(l)
```

    ['*']


## Exercise 3

## Rectangle Pattern
#### Problem Description:

You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).



#### Input:

Two integers n and m, where 1 <= n, m <= 100.



#### Output:

A list of strings where each string represents a row of the rectangle pattern.



#### Example:
```
Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']
```


```python
n, m, l = 4, 5, []

for i in range(n):
    l.append("*"*m)
print(l) 
```

    ['*****', '*****', '*****', '*****']


## Exercise 4

## Right Angled Triangle
#### Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.



#### Input Parameters:

n (int): The height and base of the right-angled triangle.



#### Output:

A list of strings where each string is a row of '*' characters that increases in length from 1 to n.



#### Example:
```

Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****']

```


```python
n, l = 3, []
for i in range(n):
    l.append("*"*(i+1))
print(l)
```

    ['*', '**', '***']


## Exercise 5

## Inverted Right Angled Triangle
#### Problem Description:

You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.



#### Input Parameters:

n (int): The height and base of the inverted right-angled triangle.



#### Output:

A list of strings where each string is a row of '*' characters that decreases in length from n to 1.



#### Example:
```
Input: 3
Output: ['***', '**', '*']
 
Input: 5
Output: ['*****', '****', '***', '**', '*']
```



```python
n, l = 3, []

while n>=1:
    l.append("*"*n)
    n -= 1

print(l)
```

    ['***', '**', '*']


## Exercise 6

## Pyramid Pattern
#### Problem Description:

You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.



#### Input:

A single integer n, where 1 <= n <= 100.



#### Output:

A list of strings where each string contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.



#### Example:
```
Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
```



```python
n = 3 
pyramid = []

for i in range(1, n+1): 
    r = ""
    for j in range(n-i): 
        r += " "
    for k in range(1, 2*i): 
        r += "*"
    for l in range(n-i): 
        r += " "
    pyramid.append(r)
pyramid
```




    ['  *  ', ' *** ', '*****']



## Exercise 7

## Inverted Pyramid Pattern
**Problem Description**

You are given an integer n. Your task is to return an inverted pyramid pattern of '*', where each side has n rows, represented as a list of strings. The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, until the last row has 1 star, with each row centered using spaces.



**Input Parameters**:

n (int): The number of rows in the inverted pyramid.



**Output:**

A list of strings where each string represents a row of the inverted pyramid.



**Example:**
```
Input: 3
Output: ['*****', ' *** ', '  *  ']
 
Input: 5
Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
```


```python
n = 3
p = []

for i in range(n, 0, -1):
  r = ""
  for j in range(n-i):
    r += " "
  for k in range(1, 2*i):
    r += "*"
  for l in range(n-i):
    r += " "
  p.append(r)

p
```




    ['*****', ' *** ', '  *  ']



## Exercise 8

## Right Angled Triangle with Numbers
**Problem Description:**

You are given an integer n. Your task is to return a right-angled triangle pattern where each row contains repeated digits. The first row contains the number 1 repeated once, the second row contains the number 2 repeated twice, and so on until the nth row contains the number n repeated n times.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the triangle. The ith row contains the digit i repeated i times.



**Example:**
```
Input: 5
Output: ['1', '22', '333', '4444', '55555']
 
Input: 3
Output: ['1', '22', '333']
```



```python
n = 3
p = []

for i in range(1, n+1):
  r = ""
  for j in range(i):
    r += str(i)
  p.append(r)
p
```




    ['1', '22', '333']



## Exercise 9

## Floyds Triangle
**Problem Description**:

You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in Floyd's Triangle.



**Example:**
```
Input: 5
Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
 
Input: 3
Output: ['1', '2 3', '4 5 6']
```


```python
n = 3
p = []
count = 1
for i in range(1, n+1):
  r = ""
  for j in range(i):
    r += str(count) + " "
    count += 1
  p.append(r)
p
```




    ['1 ', '2 3 ', '4 5 6 ']



## Exercise 10

## Diamond Pattern
**Problem Description**:

You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the diamond pattern.



**Example:**
```
Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
```


```python
d = []
n = 3 

for i in range(1, n+1): 
    row = ""
    for j in range(n-i): 
        row += " "
    for k in range(1, 2*i): 
        row += "*" 
    for l in range(n-i): 
        row += " "
    d.append(row)

for i in range(n-1, 0, -1): 
    row = "" 
    for j in range(n-i): 
        row += " "
    for k in range(1, 2*i): 
        row += "*"
    for l in range(n-i): 
        row += " "
    d.append(row)
d
```




    ['  *  ', ' *** ', '*****', ' *** ', '  *  ']



## Exersice 11

## Right Angled Triangle II
**Problem Description**:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*', where each row contains stars aligned to the right. The first row has one star, the second row has two stars, and so on, until the nth row has n stars.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the right-angled triangle, right-aligned.



**Example:**
```
Input: 4
Output: ['   *', '  **', ' ***', '****']
 
Input: 3
Output: ['  *', ' **', '***']
```


```python
tri = [] 
n = 3 

for i in range(1, n+1): 
    r = ""
    for space in range(n-i): 
        r += " "
    for star in range(i): 
        r += "*"
    tri.append(r)

tri
```




    ['  *', ' **', '***']



## Exersice 12 

## Sandglass Pattern
**Problem Description**:

You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the sandglass pattern.



**Example:**
```
Input: 3
Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
 
Input: 4
Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
```


```python
sandg = []
n = 3 

for i in range(n, 0, -1): 
    r = ""
    # space 
    for j in range(n-i): 
        r += " " 
    # star 
    for k in range(1, 2*i): 
        r += "*" 
    # space 
    for l in range(n-i): 
        r += " "
    sandg.append(r)

for i in range(2, n+1): 
    r = "" 
    # space 
    for j in range(n-i): 
        r += " " 
    # star 
    for k in range(1, 2*i): 
        r += "*" 
    # space 
    for l in range(n-i): 
        r += " "
    sandg.append(r)

sandg
```




    ['*****', ' *** ', '  *  ', ' *** ', '*****']



## Exersice 13

## Hollow Right Triangle
**Problem Description**:

You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be right-aligned.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the hollow right-angled triangle.



**Example:**
```
Input: 4
Output: ['*', '**', '* *', '****']
 
Input: 5
Output: ['*', '**', '* *', '*  *', '*****']
```


```python
hollow = [] 
n = 5

for i in range(1, n+1): 
    r = ""
    if i<3 or i==n:
        for j in range(i): 
            r += "*"
    else:
        for j in range(i-2):
            r += " "  
        r = "*"+r+"*"
    hollow.append(r)
hollow
```




    ['*', '**', '* *', '*  *', '*****']



## Exercise 14

## Hollow Inverted Right Triangle
**Problem Description**:

You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the hollow inverted right-angled triangle.



**Example:**
```
Input: 4
Output: ['****', '* *', '**', '*']
 
Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
```


```python
h = [] 
n = 4 

for i in range(n, 0, -1): 
    r = ""
    if i<3 or i==n: 
        for j in range(i): 
            r += "*"
    else: 
        for j in range(i-2): 
            r += " "
        r = "*"+r+"*"
    h.append(r)
h
```




    ['****', '* *', '**', '*']



## Exercise 15 

## Number Pyramid Pattern
**Problem Description**:

You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces.



**Input:**

A single integer n, where 1 <= n <= 100.



**Output:**

A list of strings where each string represents a row in the pyramid pattern.



**Example:**
```
Input: 4
Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
Input: 3
Output: ['  1  ', ' 1 2 ', '1 2 3']
```


```python
nums = []
n = 3 

for i in range(1, n+1): 
    r = ""
    for j in range(n-i): 
        r += " "
    for k in range(1, i+1): 
        r += str(k)
    for l in range(n-i): 
        r += " "
    nums.append(r)
nums
```




    ['  1  ', ' 12 ', '123']


