- Coding Exercise 43: Reverse a string
- Coding Exercise 44: Count Vowels in a string
- Coding Exercise 45: Check for same strings
- Coding Exercise 46: Check Palindrome
- Coding Exercise 47: Count words in a string
- Coding Exercise 48: Remove Duplicates in a string
- Coding Exercise 49: Count consonants in a string
- Coding Exercise 50: Check for anagrams
- Coding Exercise 51: Check Subsequence
- Coding Exercise 52: Check for Substring
- Coding Exercise 53: Length of the Longest Word

### 1. Reverse a string
**Problem Description**:

You are given a string s. Your task is to return the reversed version of the string.



**Input:**

A single string s, where the length of s is between 1 and 1000.



**Output:**

A single string that is the reverse of the input string.



**Example:**
```
Input: "hello"
Output: "olleh"
 
Input: "Python"
Output: "nohtyP"
```


```python
def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

name = "vasim"
print(reverse_string(name))
```

    misav


### 2. Count Vowels in a string
**Problem Description:**

You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.



**Input:**

A single string s, where the length of s is between 1 and 1000.



**Output:**

An integer representing the total count of vowels in the input string.



**Example:**
```
Input: "Hello, World!"
Output: 3
 
Input: "Python Programming"
Output: 4
```


```python
def count_vowels_in(string):
    vowels = "aeiou"
    count = 0 
    for i in range(len(string)):
        if string[i] in vowels:
            count += 1 
    return count 

print(count_vowels_in("vasim"))
```

    2


### 3. Check for same strings
**Problem Description:**

You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.



**Input:**

Two strings s and t, where 1 <= len(s), len(t) <= 1000.



**Output:**

A boolean value (True or False) indicating whether the two strings are equal.



**Example:**
```
Input: s = "hello", t = "hello"
Output: True
 
Input: s = "hello", t = "world"
Output: False
```


```python
def compare_strings(str1, str2):
    for i in range(len(str1)-1):
        if str1[i] != str2[i]:
            return False 
    return True

# print(compare_strings("vasim", "vasim"))
print(compare_strings("vasim", "vasum"))
```

    False


### 4. Check Palindrome
**Problem Description:**

You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.



**Input:**

A single string s, where the length of s is between 1 and 1000.



**Output:**

A boolean value: True if the string is a palindrome, and False otherwise.



**Example:**
```
Input: "A man a plan a canal Panama"
Output: True
 
Input: "Hello, World!"
Output: False
```


```python
def check_palindrome(string):
    reversed_string = string[::-1]
    for i in range(len(string)):
        if string[i] != reversed_string[i]:
            return False
    return True

# print(check_palindrome("madam"))
print(check_palindrome("madan"))
```

    False


### 5. Count words in a string
**Problem Description:**

You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces.



**Input:**

A single string s, where the length of s is between 1 and 1000.



**Output:**

An integer representing the total count of words in the input string.



**Example:**
```
Input: "Hello, World!"
Output: 2
 
Input: "Python programming is fun."
Output: 4
```


```python
def count_words(string):
    words = string.split()
    return len(words)

print(count_words("vasim is excellent!"))
```

    3


### 6.Remove Duplicates in a string
**Problem Description:**

You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.



**Input:**

A single string s, where the length of s is between 1 and 1000.



**Output:**

A string that contains only the first occurrence of each character from the input string.



**Example:**
```
Input: "programming"
Output: "progamin"
 
Input: "Hello, World!"
Output: "Helo, Wrd!"
```


```python
def remove_duplicates(string):
    newstr = ""
    for i in range(len(string)):
        if string[i] not in newstr:
            newstr += string[i]
    return newstr

print(remove_duplicates("mohammed vasim"))
```

    mohaed vsi


### 7. Count consonants in a string
**Problem Description**:

You are given a string s. Your task is to count the number of consonants in the string and return the total count. A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).



**Input:**

A single string s, where the length of s is between 1 and 1000.



**Output:**

An integer representing the total count of consonants in the input string.



**Example:**
```
Input: "Hello, World!"
Output: 7
 
Input: "Python Programming"
Output: 13
```


```python
def count_consonants_in(string):
    vowels = "aeiou"
    count = 0
    for i in range(len(string)):
        if string[i] not in vowels:
            count += 1
    return count

print(count_consonants_in("vasim"))
```

    3


### 8. Check for anagrams
**Problem Description**:

You are given two strings s and t. Your task is to determine if string t is an anagram of string s. An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, using all the original characters exactly once.



**Input:**

Two strings s and t where both lengths are between 1 and 1000.



**Output:**

Return True if t is an anagram of s, and False otherwise.



**Example:**
```
Input: s = "anagram", t = "nagaram"
Output: True
 
Input: s = "rat", t = "car"
Output: False
```


```python
def check_anagram(str1, str2):
    # If lengths are not equal they are not anagram
    if len(str1) != len(str2):
        return False 
    
    # Count frequency
    count1, count2 = {}, {}

    for i in range(len(str1)):
        if str1[i] in count1:
            count1[str1[i]] += 1
        else:
            count1[str1[i]] = 1

    for i in range(len(str2)):
        if str2[i] in count2:
            count2[str2[i]] += 1
        else:
            count2[str2[i]] = 1
    
    return count1 == count2

check_anagram("listen", "silent")
```




    True



### 9. Check Subsequence
**Problem Description**:

You are given two strings s and t. Your task is to determine if string t is a subsequence of string s. A subsequence of a string is a new string that is formed from the original string by deleting some (or no) characters without changing the order of the remaining characters.



**Input:**

Two strings s and t where the length of s is between 1 and 1000, and the length of t is between 1 and 1000.



**Output:**

Return True if t is a subsequence of s, and False otherwise.



**Example:**
```
Input: s = "abcde", t = "ace"
Output: True
 
Input: s = "abcde", t = "aec"
Output: False
```


```python
def is_subsequence(s, t):
    # Initialize pointers for both strings
    i, j = 0, 0
    
    # Traverse the string t
    while i < len(s) and j < len(t):
        # If characters match, move the pointer for s
        if s[i] == t[j]:
            i += 1
        # Always move the pointer for t
        j += 1
    
    # If we have traversed all characters of s, it is a subsequence of t
    return i == len(s)

# Example usage
s = "abc"
t = "aebdc"
print(is_subsequence(s, t))  # Output: True

s = "axc"
t = "ahbgdc"
print(is_subsequence(s, t))  # Output: False
```

    True
    False


Sure, let's go through the process step-by-step with a detailed explanation and an example.

### Problem Definition
You need to determine if string `s` is a subsequence of string `t`. A subsequence means that you can delete some or no characters from `t` to get `s`, without changing the order of the remaining characters.

### Example
Let's take `s = "abc"` and `t = "aebdc"`.

### Step-by-Step Explanation

1. **Initialize Pointers**:
   - We use two pointers, `i` for `s` and `j` for `t`.
   - Both pointers start at the beginning of their respective strings (`i = 0`, `j = 0`).

2. **Traverse `t`**:
   - We will iterate through `t` using the pointer `j`.

3. **Character Matching**:
   - At each step, we compare the character at `s[i]` with the character at `t[j]`.
   - If `s[i]` matches `t[j]`, it means we have found the current character of `s` in `t`, so we move the pointer `i` to the next character in `s`.
   - Regardless of whether there was a match or not, we always move the pointer `j` to the next character in `t`.

4. **End Condition**:
   - If we reach the end of `s` (`i == len(s)`), it means all characters of `s` have been found in `t` in the correct order, so `s` is a subsequence of `t`.
   - If we reach the end of `t` without matching all characters of `s`, then `s` is not a subsequence of `t`.

### Detailed Example Walkthrough

Let's walk through the example `s = "abc"` and `t = "aebdc"`:

1. **Initial State**:
   - `i = 0`, `j = 0`
   - `s[i] = 'a'`, `t[j] = 'a'`

2. **First Iteration**:
   - Compare `s[i]` with `t[j]`: `'a' == 'a'`
   - Characters match, so move `i` to the next character in `s`: `i = 1`
   - Always move `j` to the next character in `t`: `j = 1`

3. **Second Iteration**:
   - `i = 1`, `j = 1`
   - `s[i] = 'b'`, `t[j] = 'e'`
   - Compare `s[i]` with `t[j]`: `'b' != 'e'`
   - Characters do not match, so only move `j` to the next character in `t`: `j = 2`

4. **Third Iteration**:
   - `i = 1`, `j = 2`
   - `s[i] = 'b'`, `t[j] = 'b'`
   - Compare `s[i]` with `t[j]`: `'b' == 'b'`
   - Characters match, so move `i` to the next character in `s`: `i = 2`
   - Always move `j` to the next character in `t`: `j = 3`

5. **Fourth Iteration**:
   - `i = 2`, `j = 3`
   - `s[i] = 'c'`, `t[j] = 'd'`
   - Compare `s[i]` with `t[j]`: `'c' != 'd'`
   - Characters do not match, so only move `j` to the next character in `t`: `j = 4`

6. **Fifth Iteration**:
   - `i = 2`, `j = 4`
   - `s[i] = 'c'`, `t[j] = 'c'`
   - Compare `s[i]` with `t[j]`: `'c' == 'c'`
   - Characters match, so move `i` to the next character in `s`: `i = 3`
   - Always move `j` to the next character in `t`: `j = 5`

7. **End Condition**:
   - `i = 3`, which is equal to `len(s)`
   - All characters of `s` have been found in `t` in the correct order.

Therefore, `s = "abc"` is a subsequence of `t = "aebdc"`.

### Function Implementation

Here is the function again for reference:




```python
def is_subsequence(s, t):
    # Initialize pointers for both strings
    i, j = 0, 0
    
    # Traverse the string t
    while i < len(s) and j < len(t):
        # If characters match, move the pointer for s
        if s[i] == t[j]:
            i += 1
        # Always move the pointer for t
        j += 1
    
    # If we have traversed all characters of s, it is a subsequence of t
    return i == len(s)

# Example usage
s = "abc"
t = "aebdc"
print(is_subsequence(s, t))  # Output: True

s = "axc"
t = "ahbgdc"
print(is_subsequence(s, t))  # Output: False
```



This function uses the two-pointer technique to efficiently check if `s` is a subsequence of `t`.

### 10. Check for Substring
**Problem Description**:

You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for string operations and do not use recursion.



**Input:**

Two strings s and t, where 1 <= len(s), len(t) <= 1000.



**Output:**

A boolean value (True or False) indicating whether t is a substring of s.



**Example:**
```
Input: s = "hello world", t = "world"
Output: True
 
Input: s = "hello world", t = "worlds"
Output: False
```


```python
def check_substr(string, substr):
    words = string.split()
    for i in range(len(words)):
        if words[i] == substr:
            return True 
        
s = "vasim is excellent"
t = "excellent"
print(check_substr(s, t))
```

    True


### 11. Length of the Longest Word
**Problem Description**:

You are given a string s. Your task is to find the length of the longest word in the string. A word is defined as a sequence of characters separated by spaces. Do not use any built-in functions for string manipulation.



**Input:**

A string s, where the length of s is between 1 and 1000 characters.



**Output:**

An integer representing the length of the longest word in the string.



**Example:**
```
Input: s = "The quick brown fox jumps over the lazy dog"
Output: 5
 
Input: s = "Hello World"
Output: 5
```


```python
def custom_split(s, delimiter=' '):
    result = []
    current_word = []
    
    for char in s:
        if char == delimiter:
            if current_word:
                result.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    # Add the last word if there is any
    if current_word:
        result.append(''.join(current_word))
    
    return result

# Example usage
s = "This is a test string"
print(custom_split(s))  # Output: ['This', 'is', 'a', 'test', 'string']

s = "apple,banana,cherry"
print(custom_split(s, ','))  # Output: ['apple', 'banana', 'cherry']
```

    ['This', 'is', 'a', 'test', 'string']
    ['apple', 'banana', 'cherry']



```python
# def find_longest(string):
#     words = string.split()
#     longest_word = ""
#     for i in range(len(words)):



#     return words 

# print(find_longest("vasim is excellent"))

```

    v
    va
    vas
    vasi
    vasim
    
    i
    is
    
    e
    ex
    exc
    exce
    excel
    excell
    excelle
    excellen
    excellent
    []



