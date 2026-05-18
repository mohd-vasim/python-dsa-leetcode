# Recursion Fundamentals

---

## 1. Factorial of a Number using Recursion

### Problem Description
You are given a non-negative integer `n`. Your task is to find the **factorial** of `n`, defined as the product of all positive integers less than or equal to `n`.

> **Note:** The factorial of `0` is defined to be `1`.

### Input
- A non-negative integer `n`, where `0 <= n <= 20`

### Output
- An integer representing the factorial of `n`

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `n = 5` | `120` | `5! = 5 × 4 × 3 × 2 × 1 = 120` |
| `n = 0` | `1` | `0! = 1` (by definition) |

---

## 2. Sum of N Numbers using Recursion

### Problem Description
You are given a non-negative integer `n`. Your task is to find the **sum of the first `n` natural numbers** using recursion.

> **Formula:** `S = 1 + 2 + 3 + ... + n`

### Input
- A non-negative integer `n`, where `0 <= n <= 1000`

### Output
- An integer representing the sum of the first `n` natural numbers

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `n = 5` | `15` | `1 + 2 + 3 + 4 + 5 = 15` |
| `n = 0` | `0` | Sum of zero natural numbers |

---

## 3. Number of Digits using Recursion

### Problem Description
You are given a positive integer `n`. Your task is to find the **number of digits** in the integer using recursion.

### Input
- A positive integer `n`, where `1 <= n <= 10^9`

### Output
- An integer representing the number of digits in `n`

### Examples

| Input | Output |
|-------|--------|
| `n = 12345` | `5` |
| `n = 7` | `1` |

---

## 4. Fibonacci Series using Recursion

### Problem Description
You are given a non-negative integer `n`. Your task is to find the **nth Fibonacci number** using recursion.

### Fibonacci Sequence Definition
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  for n >= 2
```

### Input
- A non-negative integer `n`, where `0 <= n <= 30`

### Output
- An integer representing the nth Fibonacci number

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `n = 5` | `5` | Sequence: `0, 1, 1, 2, 3, 5` |
| `n = 0` | `0` | `F(0) = 0` |

---

## 5. Print 1 to N using Recursion

### Problem Description
You are given a positive integer `n`. Your task is to **return a list of integers from `1` to `n`** using recursion.

### Input
- A positive integer `n`, where `1 <= n <= 1000`

### Output
- A list of integers from `1` to `n`

### Examples

| Input | Output |
|-------|--------|
| `n = 5` | `[1, 2, 3, 4, 5]` |
| `n = 3` | `[1, 2, 3]` |

---

## 6. Print N to 1 using Recursion

### Problem Description
You are given a positive integer `n`. Your task is to **return a list of integers from `n` to `1`** using recursion.

### Input
- A positive integer `n`, where `1 <= n <= 1000`

### Output
- A list of integers from `n` to `1`

### Examples

| Input | Output |
|-------|--------|
| `n = 5` | `[5, 4, 3, 2, 1]` |
| `n = 3` | `[3, 2, 1]` |

