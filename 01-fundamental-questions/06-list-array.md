- Coding Exercise 63: Maximum Element in a List.
- Coding Exercise 64: Sum of Elements in a List
- Coding Exercise 65: Palindrome List
- Coding Exercise 66: Reverse a List
- Coding Exercise 67: Rotate List
- Coding Exercise 68: Plus One in the Number
- Coding Exercise 69: Missing Number
- Coding Exercise 70: Is Array Sorted?
- Coding Exercise 71: Move Zeroes
- Coding Exercise 72: Intersection of two Lists
- Coding Exercise 73: Max Consecutive Ones
- Coding Exercise 74: Maximum Subarray Sum

### **1. Maximum Element in a List.**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a list of integers, write a function to find the maximum element in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The maximum element in the list.



Example:

Input: lst = [3, 5, 2, 9, 6]
Output: 9
 
Input: lst = [-1, -2, -3, -4]
Output: -1
 
Input: lst = [7]
Output: 7


```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

arr = [1, 2, 3, 4, 5]
print(find_max(arr))
```

    5


### **2. Sum of Elements in a List**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a list of integers, write a function to find the sum of all the elements in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The sum of all the elements in the list.



Example:

Input: lst = [7]
Output: 7
 
Input: lst = [-1, -2, -3, -4]
Output: -10
 
Input: lst = [1, 2, 3, 4, 5]
Output: 15



```python
def sum_of(arr):
    summ = 0
    for i in range(len(arr)):
        summ += arr[i]
    return summ

arr = [1, 2, 3, 4, 5]
print(sum_of(arr)) 
```

    15


### **3. Palindrome List**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.



Input Parameters:

lst (List[int]): A list of integers.

Output:

bool: Return True if the list is a palindrome, otherwise False.



Example:

Input: lst = [7, 8, 9, 8, 7]
Output: True
 
Input: lst = [1, 2, 3, 4, 5]
Output: False
 
Input: lst = [1, 2, 3, 2, 1]
Output: True



```python
def check_palindrome(arr):
    reversed_arr = arr[::-1]
    for i in range(len(arr)):
        if arr[i] != reversed_arr[i]:
            return False 
    return True 

arr = [1, 2, 3, 2, 1]
print(check_palindrome(arr))
```

    True


### **4. Reverse a List**
Asked in Companies:

Google

Amazon

Microsoft

Apple



Description:
Given a list of integers, write a function to reverse the order of elements in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

List[int]: The list with elements in reversed order.



Example:

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
 
Input: lst = [10, 20, 30]
Output: [30, 20, 10]
 
Input: lst = [7, 8, 9]
Output: [9, 8, 7]



```python
def reverse_arr(arr):
    newarr = []
    for i in range(len(arr)-1, -1, -1):
        print(i)
        newarr.append(arr[i])
    return newarr 

arr = [1, 2, 3, 4, 5]
print(reverse_arr(arr))
```

    4
    3
    2
    1
    0
    [5, 4, 3, 2, 1]


### **5. Rotate List**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a list of integers and an integer D, write a function to rotate the list to the left by D positions.



Input Parameters:

ARR (List[int]): A list of integers.

D (int): The number of positions to rotate the list to the left.

Output:

List[int]: The list after rotating it to the left by D positions.



Example:

Input: ARR = [1, 2, 3, 4, 5], D = 2
Output: [3, 4, 5, 1, 2]
 
Input: ARR = [10, 20, 30, 40, 50], D = 3
Output: [40, 50, 10, 20, 30]
 
Input: ARR = [7, 8, 9, 10], D = 1
Output: [8, 9, 10, 7]



```python
def rotate_list_by_d(arr, d):
    newarr = arr[d:] + arr[:d]
    return newarr

arr = [1, 2, 3, 4, 5]
d = 2
print(rotate_list_by_d(arr, d))
```

    [3, 4, 5, 1, 2]


### **6. Plus One in the Number**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeroes.

Write a function to increment the large integer by one and return the resulting array of digits.



Input Parameters:

digits (List[int]): A list of integers where each integer represents a digit of a large number.

Output:

List[int]: The list representing the number after incrementing it by one.



Example:

Input: digits = [1, 2, 3]
Output: [1, 2, 4]
 
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
 
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]



```python
def plus_one(arr):
    print(arr)
    nums = "".join([str(i) for i in arr])
    print(nums)
    nums = str(int(nums) + 1)
    print(nums)
    nums = [int(i) for i in nums]
    print(nums)
    return 

arr = [1,2,3]
plus_one(arr)
```

    [1, 2, 3]
    123
    124
    [1, 2, 4]


### **7. Missing Number**
Asked in Companies:

Google

Microsoft

Amazon

Facebook



Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Input Parameters:

nums (List[int]): A list of integers where each integer is unique and in the range [0, n].

Output:

int: The missing number in the range [0, n].



Example:

Input: nums = [3, 0, 1]
Output: 2
 
Input: nums = [0, 1]
Output: 2
 
Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
Output: 5



```python
def check_missing_num(arr):
    count = 0
    missing = []
    for i in range(len(arr)):
        if count not in arr:
            missing.append(count)
        count += 1
    return missing

arr = [0, 1, 2, 3, 4, 6, 7, 8]
print(check_missing_num(arr))

```

    [5]


### **8. Is Array Sorted?**
Asked in Companies:

Google

Microsoft

Amazon

Facebook



Description:
Write a function that checks whether the given array is sorted in non-decreasing order. The array is considered sorted if every element is less than or equal to the next element.



Input Parameters:

arr (List[int]): A list of integers.

Output:

bool: True if the array is sorted in non-decreasing order, False otherwise.



Example:

Input: arr = [5, 4, 3, 2, 1]
Output: False
 
Input: arr = [1, 3, 2, 4, 5]
Output: False
 
Input: arr = [1, 2, 3, 4, 5]
Output: True



```python
def is_array_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True 

arr = [1,2,3,4]
arr2 = [1,3,2,5]

is_array_sorted(arr2)
```




    False



### **9. Move Zeroes**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given an integer array nums, write a function to move all 0s to the end of the array while maintaining the relative order of the non-zero elements.



Input Parameters:

nums (List[int]): A list of integers.

Output:

The list nums with all 0s moved to the end, preserving the order of non-zero elements.



Example:

Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
 
Input: nums = [0, 0, 1]
Output: [1, 0, 0]
 
Input: nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]



```python
def move_zero_to_left(arr): 
    non_zero = []
    zeros = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros.append(arr[i])
        else:
            non_zero.append(arr[i]) 
    return non_zero + zeros

arr = [1,0,2,0,3,0,4,5]
move_zero_to_left(arr)
```




    [1, 2, 3, 4, 5, 0, 0, 0]



### **10. Intersection of two Lists**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique, and you may return the result in any order.



Input Parameters:

nums1 (List[int]): An array of integers.

nums2 (List[int]): An array of integers.

Output:

List[int]: An array of unique integers that are present in both nums1 and nums2.



Example:

Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
Output: []
 
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
 
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]



```python
def get_intersection_from(arr1, arr2): 
    intersection = []
    for i in arr1:
        for j in arr2:
            if i == j and i not in intersection: 
                intersection.append(i) 
    return intersection

arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]
get_intersection_from(arr1, arr2)
```




    [3, 4, 5]



### **11. Max Consecutive Ones**
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a binary array nums, return the maximum number of consecutive 1s in the array.



Input Parameters:

nums (List[int]): A binary array where each element is either 0 or 1.

Output:

int: The maximum number of consecutive 1s in the array.



Example:

Input: nums = [0, 0, 0, 0]
Output: 0
 
Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
Output: 4
 
Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3



```python
def check_cons_ones(arr):
    ones = []
    for i in range(len(arr)):
        if arr[i] == 1:
            if not ones:
                ones.append([])
            ones[-1].append(arr[i])
        elif arr[i] == 0:
            ones.append([])
    print(f"List: {ones} | Max: {max(ones)}")
    return len(max(ones))

arr = [1,1,0,1,1,1,0,1,1,1,1,0,1]
check_cons_ones(arr)
```

    List: [[1, 1], [1, 1, 1], [1, 1, 1, 1], [1]] | Max: [1, 1, 1, 1]





    4



### **12. Maximum Subarray Sum**
Asked in Companies:

Accenture

SAP labs

Dunzo

Acko



Description:

Given an array arr of length n, consisting of integers, find the sum of the subarray (including an empty subarray) that has the maximum sum among all possible subarrays.



Input:

An integer array arr of length n where 1 ≤ n ≤ 10^5 and each element arr[i] is an integer.

Output:

An integer representing the sum of the subarray with the maximum sum. If all numbers are negative, the algorithm should handle that correctly by returning the largest single number or zero if the array is empty.

Example:

Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the maximum sum 6.



```python
def find_max_subarry_sum(arr):
    """ 
    Steps to solve: 
    1. Write program to create sub arrays
    2. Write program to calculate sum of sub arrays
    3. Find max sum idx from the sub arrays
    """
    sums = []
    subarrays = []
    # for i in range(len(arr)):
    #     subarrays.append([])
    #     for j in range(i+1):
    #         subarrays[-1].append(arr[j])
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarrays.append([])
            for k in range(i, j+1):
                subarrays[-1].append(arr[k])

    max_sum, max_idx = 0, 0
    for i in range(len(subarrays)):
        if sum(subarrays[i]) > max_sum:
            max_sum = sum(subarrays[i])
            max_idx = i
        sums.append(sum(subarrays[i]))
    print(f"Subarrays: {subarrays} \nSums: {sums} \nMax: {max_sum}")

arr = [1,2,3,4]
find_max_subarry_sum(arr)
```

    Subarrays: [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]] 
    Sums: [1, 3, 6, 10, 2, 5, 9, 3, 7, 4] 
    Max: 10

