
# ============================================================================
# EXPERIMENT 1 — PROGRAM 01: Check whether a number is a Fibonacci number
# ============================================================================
def exp_01_program_01():
    from math import isqrt
    def is_square(x):
        return isqrt(x) ** 2 == x
    def is_fibonacci(n):
        return n >= 0 and (is_square(5*n*n + 4) or is_square(5*n*n - 4))
    n = 34
    print(n, 'is Fibonacci:', is_fibonacci(n))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check whether a number is a Fibonacci number.
    # Use the identity that n is Fibonacci exactly when 5*n*n + 4 or 5*n*n - 4 is a perfect
    # square; test squares with math.isqrt.
    # Defined functions: is_square, is_fibonacci. These package reusable steps and accept
    # arguments as shown in their signatures.
    # isqrt(): returns exact integer square root.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 02: Find the nth multiple of a number in the Fibonacci series
# ============================================================================
def exp_01_program_02():
    def nth_fibonacci_multiple(k, n):
        if k == 0 or n < 1:
            raise ValueError("k must be nonzero and n must be positive")
        a, b, found = 0, 1, 0
        while True:
                if a != 0 and a % k == 0:
                    found += 1
                    if found == n:
                        return a
                a, b = b, a + b
    print(nth_fibonacci_multiple(3, 4))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Find the nth multiple of a number in the Fibonacci series.
    # Generate Fibonacci values iteratively; skip zero, count terms divisible by k, and return
    # the nth such term. Require k != 0 and n >= 1.
    # Defined functions: nth_fibonacci_multiple. These package reusable steps and accept
    # arguments as shown in their signatures.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Define the helper/search/model functions and their return conditions.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Evaluate each decision condition and follow the matching branch.
    # 5. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 03: Print ASCII value of a character
# ============================================================================
def exp_01_program_03():
    ch = 'A'
    print('ASCII value:', ord(ch))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Print ASCII value of a character.
    # ord(): returns the Unicode code point (ASCII for ASCII characters).
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 04: Sum of squares of first n natural numbers
# ============================================================================
def exp_01_program_04():
    n = 5
    print(sum(i*i for i in range(1, n+1)))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Sum of squares of first n natural numbers.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 05: Sum of cubes of first n natural numbers
# ============================================================================
def exp_01_program_05():
    n = 5
    print(sum(i**3 for i in range(1, n+1)))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Sum of cubes of first n natural numbers.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 06: Rotate an array
# ============================================================================
def exp_01_program_06():
    a = [1, 2, 3, 4, 5]
    k = 2
    k %= len(a)
    print(a[k:] + a[:k])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Rotate an array.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 07: Reversal algorithm for array rotation
# ============================================================================
def exp_01_program_07():
    def reverse(a, left, right):
        while left < right:
            a[left], a[right] = a[right], a[left]
            left, right = left + 1, right - 1
    def rotate_left(a, k):
        if not a:
            return a
        k %= len(a)
        reverse(a, 0, k-1)
        reverse(a, k, len(a)-1)
        reverse(a, 0, len(a)-1)
        return a
    print(rotate_left([1, 2, 3, 4, 5], 2))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Reversal algorithm for array rotation.
    # Reverse the first k entries, reverse the remaining entries, then reverse the whole array to
    # obtain a left rotation in place.
    # Defined functions: reverse, rotate_left. These package reusable steps and accept arguments
    # as shown in their signatures.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Define the helper/search/model functions and their return conditions.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Evaluate each decision condition and follow the matching branch.
    # 5. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 08: Split an array and move the first part to the end
# ============================================================================
def exp_01_program_08():
    a = [10, 20, 30, 40, 50]
    position = 3
    print(a[position:] + a[:position])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Split an array and move the first part to the end.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 09: Remainder of array product divided by n
# ============================================================================
def exp_01_program_09():
    a = [2, 3, 4, 5]
    n = 7
    if n == 0:
        raise ValueError("Modulus n must be nonzero")
    remainder = 1
    for value in a:
        remainder = (remainder * value) % n
    print('Remainder:', remainder)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Remainder of array product divided by n.
    # Multiply entries modulo n after each step; modular reduction avoids constructing the entire
    # product. Require nonzero modulus.
    # for loops: visit each item or iteration in the specified iterable.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 3. Evaluate each decision condition and follow the matching branch.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 10: Check whether an array is monotonic
# ============================================================================
def exp_01_program_10():
    def monotonic(a):
        increasing = all(a[i] <= a[i+1] for i in range(len(a)-1))
        decreasing = all(a[i] >= a[i+1] for i in range(len(a)-1))
        return increasing or decreasing
    print(monotonic([5, 4, 4, 2]))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check whether an array is monotonic.
    # Defined functions: monotonic. These package reusable steps and accept arguments as shown in
    # their signatures.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Define the helper/search/model functions and their return conditions.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 11: Print all negative numbers in a range
# ============================================================================
def exp_01_program_11():
    start, end = -5, 3
    print([x for x in range(start, end+1) if x < 0])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Print all negative numbers in a range.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 12: Remove multiple elements from a list
# ============================================================================
def exp_01_program_12():
    a = [1, 2, 3, 4, 5, 6]
    remove = {2, 4, 6}
    print([x for x in a if x not in remove])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Remove multiple elements from a list.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 13: Remove empty lists from a list
# ============================================================================
def exp_01_program_13():
    a = [[], [1, 2], [], [3], []]
    print([item for item in a if item != []])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Remove empty lists from a list.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 14: Clone or copy a list
# ============================================================================
def exp_01_program_14():
    original = [10, 20, 30]
    cloned = original.copy()
    cloned.append(40)
    print('Original:', original)
    print('Copy:', cloned)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Clone or copy a list.
    # copy(): creates a shallow copy.
    # append(): adds an item to the end of a list.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 15: Count occurrences of an element in a list
# ============================================================================
def exp_01_program_15():
    a = [2, 3, 2, 5, 2, 7]
    print('Occurrences:', a.count(2))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Count occurrences of an element in a list.
    # count(): counts matching list items.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 16: Remove empty tuples from a list
# ============================================================================
def exp_01_program_16():
    a = [(), (1, 2), (), (3,)]
    print([item for item in a if item])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Remove empty tuples from a list.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 17: Print duplicate integers in a list
# ============================================================================
def exp_01_program_17():
    a = [1, 2, 3, 2, 4, 1, 5]
    seen, duplicates = set(), set()
    for x in a:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    print(sorted(duplicates))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Print duplicate integers in a list.
    # sorted(): returns elements in sorted order.
    # for loops: visit each item or iteration in the specified iterable.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 3. Evaluate each decision condition and follow the matching branch.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 18: Calculate cumulative sum of a list
# ============================================================================
def exp_01_program_18():
    a = [1, 2, 3, 4]
    total, result = 0, []
    for x in a:
        total += x
        result.append(total)
    print(result)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Calculate cumulative sum of a list.
    # append(): adds an item to the end of a list.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 19: Sum digits of each number in a list
# ============================================================================
def exp_01_program_19():
    a = [123, 45, 907]
    result = [sum(int(ch) for ch in str(abs(x))) for x in a]
    print(result)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Sum digits of each number in a list.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 20: Split a list into chunks of size N
# ============================================================================
def exp_01_program_20():
    a = list(range(1, 10))
    n = 4
    print([a[i:i+n] for i in range(0, len(a), n)])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Split a list into chunks of size N.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 21: Sort values of one list using another list
# ============================================================================
def exp_01_program_21():
    values = ['a', 'b', 'c']
    keys = [30, 10, 20]
    print([value for _, value in sorted(zip(keys, values))])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Sort values of one list using another list.
    # sorted(): returns elements in sorted order.
    # zip(): pairs elements across iterables; * unpacks rows for transpose.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 22: Transpose a matrix in a single line
# ============================================================================
def exp_01_program_22():
    matrix = [[1, 2, 3], [4, 5, 6]]
    print([list(row) for row in zip(*matrix)])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Transpose a matrix in a single line.
    # zip(): pairs elements across iterables; * unpacks rows for transpose.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 23: Create an n x n matrix
# ============================================================================
def exp_01_program_23():
    n = 3
    matrix = [[i*n+j+1 for j in range(n)] for i in range(n)]
    for row in matrix:
        print(row)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Create an n x n matrix.
    # for loops: visit each item or iteration in the specified iterable.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 24: Extract the kth column of a matrix
# ============================================================================
def exp_01_program_24():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1     # zero-based column index
    print([row[k] for row in matrix])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Extract the kth column of a matrix.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 25: Vertically concatenate two matrices
# ============================================================================
def exp_01_program_25():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print(a + b)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Vertically concatenate two matrices.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 26: Split and join a string
# ============================================================================
def exp_01_program_26():
    s = 'Artificial Intelligence Lab'
    words = s.split()
    print(words)
    print('-'.join(words))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Split and join a string.
    # split(): separates text into tokens.
    # join(): joins strings with a separator.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 27: Check whether a string is binary
# ============================================================================
def exp_01_program_27():
    s = '101001'
    print(bool(s) and set(s) <= {'0', '1'})

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check whether a string is binary.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 28: Find uncommon words from two strings
# ============================================================================
def exp_01_program_28():
    from collections import Counter
    s1 = 'python is easy'
    s2 = 'python is powerful'
    a, b = Counter(s1.split()), Counter(s2.split())
    print(sorted(word for word in a.keys() | b.keys()
                    if a[word] + b[word] == 1))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Find uncommon words from two strings.
    # Count words in each sentence; a word is uncommon only if its combined frequency across both
    # sentences is exactly one.
    # Counter(): counts occurrences of elements.
    # sorted(): returns elements in sorted order.
    # split(): separates text into tokens.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 29: Replace duplicate occurrences in a string
# ============================================================================
def exp_01_program_29():
    s = 'programming'
    seen, result = set(), []
    for ch in s:
        result.append(ch if ch not in seen else '*')
        seen.add(ch)
    print(''.join(result))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Replace duplicate occurrences in a string.
    # append(): adds an item to the end of a list.
    # join(): joins strings with a separator.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 30: Replace multiple words with K
# ============================================================================
def exp_01_program_30():
    import re
    s = 'cats and dogs are friendly'
    words = ['cats', 'dogs']
    pattern = r'\b(?:' + '|'.join(map(re.escape, words)) + r')\b'
    print(re.sub(pattern, 'K', s))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Replace multiple words with K.
    # sub(): replaces text matching a regular expression.
    # join(): joins strings with a separator.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 31: Generate permutations of a string using built-in functions
# ============================================================================
def exp_01_program_31():
    from itertools import permutations
    s = 'ABC'
    print([''.join(p) for p in permutations(s)])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Generate permutations of a string using built-in functions.
    # join(): joins strings with a separator.
    # permutations(): generates all ordered arrangements.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 32: Check for a URL in a string
# ============================================================================
def exp_01_program_32():
    import re
    s = 'Visit https://example.com for details.'
    urls = re.findall(r'https?://[^\s,]+', s)
    print(urls)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check for a URL in a string.
    # findall(): finds regex matches in text.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 33: Execute a string of Python code
# ============================================================================
def exp_01_program_33():
    code = 'result = 5 * 6'
    namespace = {}
    # Execute only trusted code strings.
    exec(code, {'__builtins__': {}}, namespace)
    print(namespace['result'])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Execute a string of Python code.
    # The example executes a fixed trusted assignment with builtins disabled. Disabling builtins
    # is not a general-purpose secure sandbox.
    # exec(): executes a trusted Python code string; never use on untrusted input.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 34: Rotate a string using slicing
# ============================================================================
def exp_01_program_34():
    s = 'python'
    k = 2
    print(s[k:] + s[:k])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Rotate a string using slicing.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 35: Check whether recursive deletion can empty a string
# ============================================================================
def exp_01_program_35():
    def can_reduce(s, pattern):
        if not pattern:
            return s == ''
        while pattern in s:
            s = s.replace(pattern, '', 1)
        return s == ''
    print(can_reduce('abcabc', 'abc'))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check whether recursive deletion can empty a string.
    # Repeatedly remove the first occurrence of the chosen substring until it no longer appears;
    # success means the remaining string is empty.
    # Defined functions: can_reduce. These package reusable steps and accept arguments as shown
    # in their signatures.
    # replace(): substitutes occurrences in a string.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Define the helper/search/model functions and their return conditions.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Evaluate each decision condition and follow the matching branch.
    # 5. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 36: Find all duplicate characters in a string
# ============================================================================
def exp_01_program_36():
    from collections import Counter
    s = 'programming'
    counts = Counter(s)
    print(sorted(ch for ch, count in counts.items() if count > 1))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Find all duplicate characters in a string.
    # Counter(): counts occurrences of elements.
    # sorted(): returns elements in sorted order.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 37: Replace all occurrences of a substring
# ============================================================================
def exp_01_program_37():
    s = 'red blue red green red'
    print(s.replace('red', 'yellow'))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Replace all occurrences of a substring.
    # replace(): substitutes occurrences in a string.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 38: Count frequencies in a list using a dictionary
# ============================================================================
def exp_01_program_38():
    a = ['a', 'b', 'a', 'c', 'b', 'a']
    counts = {}
    for item in a:
        counts[item] = counts.get(item, 0) + 1
    print(counts)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Count frequencies in a list using a dictionary.
    # get(): fetches a dictionary value with a fallback.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 39: Convert a list of tuples into a dictionary
# ============================================================================
def exp_01_program_39():
    pairs = [('name', 'Riya'), ('age', 20), ('course', 'AI')]
    print(dict(pairs))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Convert a list of tuples into a dictionary.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 40: Check whether a string can be formed by deletion and rearrangement
# ============================================================================
def exp_01_program_40():
    from collections import Counter
    source = 'artificial intelligence'
    target = 'intelligence'
    possible = not (Counter(target) - Counter(source))
    print('Can form target:', possible)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check whether a string can be formed by deletion and rearrangement.
    # Counter(): counts occurrences of elements.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 41: Check whether character frequencies can become equal
# ============================================================================
def exp_01_program_41():
    from collections import Counter
    def equal_after_one_removal(s):
        for i in range(len(s)):
            counts = Counter(s[:i] + s[i+1:])
            if len(set(counts.values())) <= 1:
                    return True
        return False
    print(equal_after_one_removal('aabbccc'))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Check whether character frequencies can become equal.
    # Try deleting each character once; after each deletion count the remaining letters and check
    # whether all positive frequencies are equal.
    # Defined functions: equal_after_one_removal. These package reusable steps and accept
    # arguments as shown in their signatures.
    # Counter(): counts occurrences of elements.
    # for loops: visit each item or iteration in the specified iterable.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 5. Evaluate each decision condition and follow the matching branch.
    # 6. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 42: Find alphabetically ordered words in a dictionary
# ============================================================================
def exp_01_program_42():
    words = ['abc', 'ace', 'hello', 'almost', 'zoo']
    ordered = [w for w in words if list(w) == sorted(w)]
    print(ordered)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Find alphabetically ordered words in a dictionary.
    # sorted(): returns elements in sorted order.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 43: Find possible words from given characters
# ============================================================================
def exp_01_program_43():
    from collections import Counter
    letters = Counter('atepr')
    dictionary = ['tap', 'pet', 'pear', 'rate', 'tree']
    print([w for w in dictionary if not (Counter(w) - letters)])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Find possible words from given characters.
    # Counter(): counts occurrences of elements.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 44: Find keys associated with a dictionary value
# ============================================================================
def exp_01_program_44():
    data = {'A': 10, 'B': 20, 'C': 10}
    value = 10
    print([key for key, val in data.items() if val == value])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Find keys associated with a dictionary value.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 45: Convert a date string to a timestamp
# ============================================================================
def exp_01_program_45():
    from datetime import datetime, timezone
    date = datetime.strptime('2026-01-01', '%Y-%m-%d')
    date = date.replace(tzinfo=timezone.utc)
    print(int(date.timestamp()))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Convert a date string to a timestamp.
    # strptime(): parses a date/time string using a format.
    # replace(): substitutes occurrences in a string.
    # timestamp(): converts a datetime into Unix seconds.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 46: Convert a timestamp string to a datetime object
# ============================================================================
def exp_01_program_46():
    from datetime import datetime, timezone
    timestamp = '1767225600'
    dt = datetime.fromtimestamp(int(timestamp), tz=timezone.utc)
    print(dt.strftime('%Y-%m-%d %H:%M:%S UTC'))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Convert a timestamp string to a datetime object.
    # fromtimestamp(): converts a Unix timestamp into a datetime.
    # strftime(): formats a date/time value as text.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 47: Count how many times each weekday occurs in a year
# ============================================================================
def exp_01_program_47():
    from datetime import date, timedelta
    from collections import Counter
    year = 2026
    start, end = date(year, 1, 1), date(year+1, 1, 1)
    counts = Counter((start + timedelta(days=i)).strftime('%A')
                    for i in range((end-start).days))
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']:
        print(day, counts[day])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Count how many times each weekday occurs in a year.
    # Counter(): counts occurrences of elements.
    # strftime(): formats a date/time value as text.
    # timedelta(): represents a duration used for date arithmetic.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 48: Count lines in a text file
# ============================================================================
def exp_01_program_48():
    from pathlib import Path
    path = Path('sample.txt')
    path.write_text('one\ntwo\nthree\n', encoding='utf-8')
    with path.open(encoding='utf-8') as file:
        print('Lines:', sum(1 for _ in file))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Count lines in a text file.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 49: Remove lines starting with a prefix
# ============================================================================
def exp_01_program_49():
    from pathlib import Path
    path = Path('notes.txt')
    path.write_text('# skip\nkeep this\n# skip too\n', encoding='utf-8')
    lines = path.read_text(encoding='utf-8').splitlines(True)
    path.write_text(''.join(line for line in lines
                                if not line.startswith('#')), encoding='utf-8')
    print(path.read_text(encoding='utf-8').strip())

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Remove lines starting with a prefix.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # splitlines(): splits text into separate lines.
    # join(): joins strings with a separator.
    # read_text(): reads text from a file.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 50: Eliminate repeated lines from a file
# ============================================================================
def exp_01_program_50():
    from pathlib import Path
    path = Path('repeat.txt')
    path.write_text('red\nblue\nred\ngreen\n', encoding='utf-8')
    seen, unique = set(), []
    for line in path.read_text(encoding='utf-8').splitlines():
        if line not in seen:
            seen.add(line)
            unique.append(line)
    path.write_text('\n'.join(unique) + '\n', encoding='utf-8')
    print(unique)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Eliminate repeated lines from a file.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # splitlines(): splits text into separate lines.
    # read_text(): reads text from a file.
    # append(): adds an item to the end of a list.
    # join(): joins strings with a separator.
    # for loops: visit each item or iteration in the specified iterable.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Evaluate each decision condition and follow the matching branch.
    # 5. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 6. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 51: Append content of one text file to another
# ============================================================================
def exp_01_program_51():
    from pathlib import Path
    Path('first.txt').write_text('Hello\n', encoding='utf-8')
    Path('second.txt').write_text('World\n', encoding='utf-8')
    with open('first.txt', 'a', encoding='utf-8') as dest:
        dest.write(Path('second.txt').read_text(encoding='utf-8'))
    print(Path('first.txt').read_text(encoding='utf-8').strip())

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Append content of one text file to another.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # read_text(): reads text from a file.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 52: Copy odd-numbered lines to another file
# ============================================================================
def exp_01_program_52():
    from pathlib import Path
    Path('input.txt').write_text('A\nB\nC\nD\nE\n', encoding='utf-8')
    with open('input.txt', encoding='utf-8') as source, \
            open('odd.txt', 'w', encoding='utf-8') as dest:
        for number, line in enumerate(source, start=1):
            if number % 2 == 1:
                    dest.write(line)
    print(Path('odd.txt').read_text(encoding='utf-8').splitlines())

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Copy odd-numbered lines to another file.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # enumerate(): iterates with an index or line number.
    # splitlines(): splits text into separate lines.
    # read_text(): reads text from a file.
    # for loops: visit each item or iteration in the specified iterable.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Evaluate each decision condition and follow the matching branch.
    # 5. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 6. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 53: Merge two files into a third file
# ============================================================================
def exp_01_program_53():
    from pathlib import Path
    Path('a.txt').write_text('Alpha\n', encoding='utf-8')
    Path('b.txt').write_text('Beta\n', encoding='utf-8')
    with open('merged.txt', 'w', encoding='utf-8') as dest:
        for name in ('a.txt', 'b.txt'):
            dest.write(Path(name).read_text(encoding='utf-8'))
    print(Path('merged.txt').read_text(encoding='utf-8').strip())

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Merge two files into a third file.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # read_text(): reads text from a file.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 5. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 54: Reverse one line of a text file
# ============================================================================
def exp_01_program_54():
    from pathlib import Path
    path = Path('line.txt')
    path.write_text('Python is fun\n', encoding='utf-8')
    lines = path.read_text(encoding='utf-8').splitlines()
    lines[0] = lines[0][::-1]
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(lines[0])

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Reverse one line of a text file.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # splitlines(): splits text into separate lines.
    # read_text(): reads text from a file.
    # join(): joins strings with a separator.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 55: Reverse file content and store it in another file
# ============================================================================
def exp_01_program_55():
    from pathlib import Path
    Path('original.txt').write_text('abc\ndef\n', encoding='utf-8')
    content = Path('original.txt').read_text(encoding='utf-8')
    Path('reversed.txt').write_text(content[::-1], encoding='utf-8')
    print(repr(Path('reversed.txt').read_text(encoding='utf-8')))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Reverse file content and store it in another file.
    # write_text(): writes UTF-8 text to a file (overwriting existing content).
    # read_text(): reads text from a file.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Read/write the example text files in the working directory; the example overwrites some
    #    filenames.
    # 4. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 1 — PROGRAM 56: Convert time from 12-hour to 24-hour format
# ============================================================================
def exp_01_program_56():
    from datetime import datetime
    time_12 = '07:45:30 PM'
    time_24 = datetime.strptime(time_12, '%I:%M:%S %p').strftime('%H:%M:%S')
    print(time_24)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Convert time from 12-hour to 24-hour format.
    # strftime(): formats a date/time value as text.
    # strptime(): parses a date/time string using a format.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 2: Breadth First Search and Depth First Search
# ============================================================================
def exp_02():
    from collections import deque
    graph = {
        'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
        'D': [], 'E': ['F'], 'F': []
    }
    def bfs(start, goal):
        queue = deque([(start, [start])])
        visited = {start}
        while queue:
                node, path = queue.popleft()
                if node == goal:
                    return path
                for nxt in graph[node]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, path + [nxt]))
        return None
    def dfs(node, goal, visited=None, path=None):
        visited = set() if visited is None else visited
        path = [] if path is None else path
        visited.add(node)
        path = path + [node]
        if node == goal:
                return path
        for nxt in graph[node]:
            if nxt not in visited:
                answer = dfs(nxt, goal, visited, path)
                if answer:
                    return answer
        return None
    print('BFS:', bfs('A', 'F'))
    print('DFS:', dfs('A', 'F'))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Breadth First Search and Depth First Search.
    # BFS uses a FIFO queue and discovers shortest unweighted paths. DFS recursively follows one
    # branch, then backtracks; visited prevents cycles.
    # Defined functions: bfs, dfs. These package reusable steps and accept arguments as shown in
    # their signatures.
    # deque(): creates a double-ended queue for efficient FIFO operations.
    # popleft(): removes the oldest queued item.
    # append(): adds an item to the end of a list.
    # for loops: visit each item or iteration in the specified iterable.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 5. Evaluate each decision condition and follow the matching branch.
    # 6. Explore candidate states using the experiment’s queue, priority, recursion, or
    #    optimization policy until a result is found.
    # 7. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 3: Uniform Cost Search and Depth Limited Search
# ============================================================================
def exp_03():
    import heapq
    graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('D', 4), ('E', 1)],
        'C': [('F', 2)], 'D': [('F', 1)],
        'E': [('F', 2)], 'F': []
    }
    def ucs(start, goal):
        heap = [(0, start, [start])]
        best = {start: 0}
        while heap:
            cost, node, path = heapq.heappop(heap)
            if cost > best[node]:
                    continue
            if node == goal:
                    return cost, path
            for nxt, weight in graph[node]:
                    new_cost = cost + weight
                    if new_cost < best.get(nxt, float('inf')):
                        best[nxt] = new_cost
                        heapq.heappush(heap, (new_cost, nxt, path + [nxt]))
        return None
    def dls(node, goal, limit, path=None):
        path = [node] if path is None else path
        if node == goal:
            return path
        if limit == 0:
            return None
        for nxt, _ in graph[node]:
            if nxt not in path:
                answer = dls(nxt, goal, limit-1, path + [nxt])
                if answer:
                    return answer
        return None
    print('UCS:', ucs('A', 'F'))
    print('DLS (limit 2):', dls('A', 'F', 2))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Uniform Cost Search and Depth Limited Search.
    # UCS uses a min-heap ordered by total path cost, while DLS recursively explores only paths
    # within the specified depth limit.
    # Defined functions: ucs, dls. These package reusable steps and accept arguments as shown in
    # their signatures.
    # heappop(): removes the smallest-priority entry.
    # get(): fetches a dictionary value with a fallback.
    # heappush(): inserts a priority-ordered entry into the min-heap.
    # for loops: visit each item or iteration in the specified iterable.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 5. Evaluate each decision condition and follow the matching branch.
    # 6. Explore candidate states using the experiment’s queue, priority, recursion, or
    #    optimization policy until a result is found.
    # 7. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 4: A* Search and Genetic Algorithm
# ============================================================================
def exp_04():
    import heapq
    import random
    edges = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)],
                'C': [('D', 1)], 'D': [('G', 3)], 'G': []}
    h = {'A': 5, 'B': 4, 'C': 4, 'D': 3, 'G': 0}
    def astar(start, goal):
        frontier = [(h[start], 0, start, [start])]
        best = {start: 0}
        while frontier:
                _, g, node, path = heapq.heappop(frontier)
                if g > best[node]:
                    continue
                if node == goal:
                    return g, path
                for nxt, cost in edges[node]:
                    new_g = g + cost
                    if new_g < best.get(nxt, float('inf')):
                        best[nxt] = new_g
                        heapq.heappush(frontier,
                                        (new_g + h[nxt], new_g, nxt, path + [nxt]))
        return None
    random.seed(7)
    population = [[random.randint(0, 1) for _ in range(8)]
                    for _ in range(12)]
    fitness = lambda bits: sum(bits)
    for generation in range(30):
        population.sort(key=fitness, reverse=True)
        parents = population[:4]
        children = parents.copy()
        while len(children) < 12:
            a, b = random.sample(parents, 2)
            cut = random.randint(1, 7)
            child = a[:cut] + b[cut:]
            child = [1-bit if random.random() < 0.08 else bit
                    for bit in child]
            children.append(child)
        population = children
    best = max(population, key=fitness)
    print('A*:', astar('A', 'G'))
    print('GA best fitness:', fitness(best), 'of 8')

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: A* Search and Genetic Algorithm.
    # A* ranks candidate paths by f=g+h. The genetic algorithm independently evolves eight-bit
    # strings through fitness selection, one-point crossover and random mutation.
    # Defined functions: astar. These package reusable steps and accept arguments as shown in
    # their signatures.
    # seed(): sets a reproducible random seed.
    # sort(): sorts a list in place.
    # copy(): creates a shallow copy.
    # heappop(): removes the smallest-priority entry.
    # randint(): draws a random integer in an inclusive range.
    # sample(): chooses distinct random elements.
    # append(): adds an item to the end of a list.
    # get(): fetches a dictionary value with a fallback.
    # heappush(): inserts a priority-ordered entry into the min-heap.
    # for loops: visit each item or iteration in the specified iterable.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 5. Evaluate each decision condition and follow the matching branch.
    # 6. Explore candidate states using the experiment’s queue, priority, recursion, or
    #    optimization policy until a result is found.
    # 7. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 5: Best First, Uniform Cost and Hill Climbing Search
# ============================================================================
def exp_05():
    import heapq
    import random
    edges = {'S': [('A', 2), ('B', 5)], 'A': [('G', 6)],
                'B': [('G', 1)], 'G': []}
    h = {'S': 3, 'A': 1, 'B': 2, 'G': 0}
    def search(greedy):
        queue = [(h['S'] if greedy else 0, 0, 'S', ['S'])]
        best = {'S': 0}
        while queue:
            _, cost, node, path = heapq.heappop(queue)
            if not greedy and cost > best[node]:
                    continue
            if node == 'G':
                    return cost, path
            for nxt, weight in edges[node]:
                    new_cost = cost + weight
                    if nxt not in best or (not greedy and new_cost < best[nxt]):
                        best[nxt] = new_cost
                        priority = h[nxt] if greedy else new_cost
                        heapq.heappush(queue, (priority, new_cost, nxt,
                                            path + [nxt]))
        return None
    # Maximize f(x) = -(x - 7)^2 + 49, for integer x in [0, 14].
    def score(x):
        return 49 - (x-7)**2
    def climb(start, mode):
        x = start
        for _ in range(50):
            neighbors = [y for y in (x-1, x+1) if 0 <= y <= 14]
            better = [y for y in neighbors if score(y) > score(x)]
            if not better:
                break
            if mode == 'steepest':
                x = max(better, key=score)
            elif mode == 'stochastic':
                weights = [score(y)-score(x) for y in better]
                x = random.choices(better, weights=weights)[0]
            else:   # first-choice: take first improving random neighbor
                random.shuffle(neighbors)
                x = next(y for y in neighbors if score(y) > score(x))
        return x, score(x)
    random.seed(5)
    print('Greedy:', search(True))
    print('UCS:', search(False))
    for mode in ('steepest', 'stochastic', 'first-choice'):
        print(mode, climb(2, mode))
    print('random-restart:', max((climb(random.randint(0, 14),
                                        'steepest') for _ in range(5)),
                                    key=lambda item: item[1]))

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Best First, Uniform Cost and Hill Climbing Search.
    # Greedy search ranks by heuristic only; UCS ranks by accumulated cost. Hill climbing
    # compares neighboring integer states, with multiple choice and restart policies.
    # Defined functions: search, score, climb. These package reusable steps and accept arguments
    # as shown in their signatures.
    # seed(): sets a reproducible random seed.
    # heappop(): removes the smallest-priority entry.
    # heappush(): inserts a priority-ordered entry into the min-heap.
    # shuffle(): randomly rearranges a list in place.
    # randint(): draws a random integer in an inclusive range.
    # choices(): selects random items with optional weights.
    # for loops: visit each item or iteration in the specified iterable.
    # while loops: repeat until the condition fails or a return/break exits.
    # if/elif/else: select the appropriate action based on a condition.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 5. Evaluate each decision condition and follow the matching branch.
    # 6. Explore candidate states using the experiment’s queue, priority, recursion, or
    #    optimization policy until a result is found.
    # 7. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 6: Simple Linear Regression and Logistic Regression
# ============================================================================
def exp_06():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.metrics import r2_score, accuracy_score
    hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
    marks = np.array([12, 20, 29, 39, 49, 60])
    df = pd.DataFrame({'Hours': hours.ravel(), 'Marks': marks})
    linear = LinearRegression().fit(hours, marks)
    pred = linear.predict(hours)
    print('Linear R2:', round(r2_score(marks, pred), 3))
    print('Predicted marks at 7 hours:', round(linear.predict([[7]])[0], 2))
    sns.regplot(data=df, x='Hours', y='Marks')
    plt.title('Simple Linear Regression')
    plt.tight_layout()
    plt.savefig('exp6_linear.png')
    plt.close()
    x = np.array([[1], [2], [3], [4], [5], [6]])
    y = np.array([0, 0, 0, 1, 1, 1])
    logistic = LogisticRegression().fit(x, y)
    labels = logistic.predict(x)
    print('Logistic accuracy:', accuracy_score(y, labels))
    print('Class for x=5:', logistic.predict([[5]])[0])
    sns.scatterplot(x=x.ravel(), y=y)
    plt.title('Logistic Regression Classes')
    plt.savefig('exp6_logistic.png')
    plt.close()

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Simple Linear Regression and Logistic Regression.
    # Linear regression predicts numeric marks from study hours; logistic regression classifies
    # binary labels. Fit each model, evaluate, and save plots.
    # reshape(): changes array dimensions.
    # fit(): learns model parameters from training data.
    # predict(): generates predictions using a fitted model.
    # regplot(): draws observations and a fitted regression line.
    # savefig(): saves a chart to an image file.
    # close(): closes the current plot to prevent overlap.
    # scatterplot(): plots individual data points.
    # accuracy_score(): calculates the fraction of correct predictions.
    # ravel(): flattens an array.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Transform the data and calculate predictions, scores, losses, or term weights as
    #    appropriate.
    # 4. Save the visual comparison or training plot as a PNG file.
    # 5. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 7: Multilayer Perceptron and Backpropagation
# ============================================================================
def exp_07():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_moons
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score
    X, y = make_moons(n_samples=400, noise=0.18, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    model = MLPClassifier(hidden_layer_sizes=(16, 8), activation='relu',
                            solver='adam', max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print('Test accuracy:', round(accuracy_score(y_test, pred), 3))
    print('Epochs:', model.n_iter_)
    history = pd.DataFrame({'Epoch': np.arange(1, len(model.loss_curve_)+1),
                            'Loss': model.loss_curve_})
    sns.lineplot(data=history, x='Epoch', y='Loss')
    plt.title('MLP Backpropagation Training Loss')
    plt.tight_layout()
    plt.savefig('exp7_loss.png')
    plt.close()

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Multilayer Perceptron and Backpropagation.
    # Generate two-moons data, split into train/test sets, standardize with training statistics,
    # fit an MLP via backpropagation, then chart the loss history.
    # make_moons(): generates a nonlinear two-class sample dataset.
    # train_test_split(): separates data into training and test subsets.
    # StandardScaler(): standardizes features using training-set mean and variance.
    # fit_transform(): learns vocabulary and transforms documents into vectors.
    # transform(): applies previously learned preprocessing.
    # MLPClassifier(): trains a multilayer perceptron classifier with backpropagation.
    # fit(): learns model parameters from training data.
    # predict(): generates predictions using a fitted model.
    # lineplot(): plots values along a line.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Transform the data and calculate predictions, scores, losses, or term weights as
    #    appropriate.
    # 4. Save the visual comparison or training plot as a PNG file.
    # 5. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 8: Batch, Stochastic and Mini-Batch Gradient Descent
# ============================================================================
def exp_08():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error
    rng = np.random.default_rng(42)
    X = rng.uniform(-1, 1, 120)
    y = 3*X + 2 + rng.normal(0, 0.12, len(X))
    def train(batch_size, epochs=80, lr=0.08):
        w, b = 0.0, 0.0
        history = []
        for epoch in range(epochs):
                indices = rng.permutation(len(X))
                for start in range(0, len(X), batch_size):
                    ids = indices[start:start+batch_size]
                    error = w*X[ids] + b - y[ids]
                    w -= lr * 2*np.mean(error*X[ids])
                    b -= lr * 2*np.mean(error)
                history.append(mean_squared_error(y, w*X+b))
        return w, b, history
    results = []
    for name, size in [('Batch', len(X)), ('Stochastic', 1),
                            ('Mini-batch', 16)]:
        w, b, losses = train(size)
        print(name, 'w=', round(w, 2), 'b=', round(b, 2),
                'MSE=', round(losses[-1], 4))
        results.extend({'Epoch': i+1, 'MSE': loss, 'Method': name}
                        for i, loss in enumerate(losses))
    sns.lineplot(data=pd.DataFrame(results), x='Epoch', y='MSE', hue='Method')
    plt.yscale('log')
    plt.title('Gradient Descent Comparison')
    plt.tight_layout()
    plt.savefig('exp8_gradient_descent.png')
    plt.close()

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Batch, Stochastic and Mini-Batch Gradient Descent.
    # Create noisy linear data; for each optimizer vary the batch size, compute MSE gradients for
    # weight and bias, update them, and plot loss by epoch.
    # Defined functions: train. These package reusable steps and accept arguments as shown in
    # their signatures.
    # default_rng(): creates a NumPy random-number generator.
    # uniform(): samples from a uniform distribution.
    # lineplot(): plots values along a line.
    # savefig(): saves a chart to an image file.
    # close(): closes the current plot to prevent overlap.
    # normal(): samples Gaussian noise.
    # permutation(): returns a random permutation.
    # append(): adds an item to the end of a list.
    # mean_squared_error(): calculates average squared prediction error.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Define the helper/search/model functions and their return conditions.
    # 4. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 5. Transform the data and calculate predictions, scores, losses, or term weights as
    #    appropriate.
    # 6. Save the visual comparison or training plot as a PNG file.
    # 7. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 9: Convolutional, Recurrent and LSTM Neural Networks
# ============================================================================
def exp_09():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.metrics import accuracy_score
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D
    from tensorflow.keras.layers import Flatten, Dense, SimpleRNN, LSTM
    from tensorflow.keras.utils import set_random_seed
    set_random_seed(42)
    rng = np.random.default_rng(42)
    # Binary image task: brighter left half versus brighter right half.
    images = rng.normal(0, 0.1, (240, 8, 8, 1)).astype('float32')
    image_y = np.arange(240) % 2
    for i, label in enumerate(image_y):
        images[i, :, :4 if label == 0 else 4:, 0] += 1.0
    cnn = Sequential([Input((8, 8, 1)), Conv2D(8, 3, activation='relu'),
                        MaxPooling2D(), Flatten(), Dense(1, activation='sigmoid')])
    cnn.compile(optimizer='adam', loss='binary_crossentropy',
                metrics=['accuracy'])
    cnn.fit(images[:200], image_y[:200], epochs=6, verbose=0)
    cnn_pred = (cnn.predict(images[200:], verbose=0).ravel() >= 0.5).astype(int)
    # Sequence task: classify whether the average signal is positive.
    sequences = rng.normal(size=(300, 10, 1)).astype('float32')
    sequence_y = (sequences.mean(axis=(1, 2)) > 0).astype(int)
    scores = {'CNN': accuracy_score(image_y[200:], cnn_pred)}
    for name, layer in [('RNN', SimpleRNN(12)), ('LSTM', LSTM(12))]:
        model = Sequential([Input((10, 1)), layer,
                                Dense(1, activation='sigmoid')])
        model.compile(optimizer='adam', loss='binary_crossentropy',
                        metrics=['accuracy'])
        model.fit(sequences[:240], sequence_y[:240], epochs=12,
                    batch_size=16, verbose=0)
        pred = (model.predict(sequences[240:], verbose=0).ravel() >= 0.5)
        scores[name] = accuracy_score(sequence_y[240:], pred)
    for name, accuracy in scores.items():
        print(name, 'accuracy:', round(accuracy, 3))
    sns.barplot(data=pd.DataFrame({'Model': list(scores),
                                    'Accuracy': list(scores.values())}),
                    x='Model', y='Accuracy')
    plt.ylim(0, 1)
    plt.title('CNN vs RNN vs LSTM')
    plt.savefig('exp9_models.png')
    plt.close()

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Convolutional, Recurrent and LSTM Neural Networks.
    # Create labeled synthetic images for CNN classification and synthetic sequences for RNN/LSTM
    # classification; train, predict, compare accuracy, and plot results.
    # default_rng(): creates a NumPy random-number generator.
    # enumerate(): iterates with an index or line number.
    # Sequential(): constructs a neural network as an ordered sequence of layers.
    # compile(): configures a neural network optimizer and loss.
    # fit(): learns model parameters from training data.
    # barplot(): draws categorical bars.
    # savefig(): saves a chart to an image file.
    # close(): closes the current plot to prevent overlap.
    # accuracy_score(): calculates the fraction of correct predictions.
    # for loops: visit each item or iteration in the specified iterable.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Transform the data and calculate predictions, scores, losses, or term weights as
    #    appropriate.
    # 5. Save the visual comparison or training plot as a PNG file.
    # 6. Print or return the final result for the supplied input, then stop.


# ============================================================================
# EXPERIMENT 10: Keyword Extraction with TF-IDF and scikit-learn
# ============================================================================
def exp_10():
    import numpy as np
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    texts = [
        'Machine learning models learn from data and patterns.',
        'Natural language processing analyzes text and language.',
        'Deep learning models use neural networks for vision.'
    ]
    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform(texts)
    terms = vectorizer.get_feature_names_out()
    for doc_id, row in enumerate(matrix):
        scores = row.toarray().ravel()
        top = np.argsort(scores)[::-1][:4]
        keywords = [(terms[i], round(float(scores[i]), 3))
                    for i in top if scores[i] > 0]
        print('Document', doc_id + 1, ':', keywords)
    summary = pd.DataFrame(matrix.toarray(), columns=terms)
    print('TF-IDF matrix shape:', summary.shape)

    # EXPLANATION / IMPORTANT CODE PARTS
    # Purpose: Keyword Extraction with TF-IDF and scikit-learn.
    # Build TF-IDF features from three documents, rank each document’s terms by their scores, and
    # print the four highest-scoring nonzero keywords.
    # TfidfVectorizer(): converts documents into weighted term vectors.
    # fit_transform(): learns vocabulary and transforms documents into vectors.
    # get_feature_names_out(): returns the vocabulary terms in column order.
    # enumerate(): iterates with an index or line number.
    # ravel(): flattens an array.
    # toarray(): converts a sparse matrix into a dense array.
    # argsort(): returns indices ordered by their values.
    # for loops: visit each item or iteration in the specified iterable.
    # List comprehensions: build a new list by mapping/filtering iterable values.
    # STEP-BY-STEP ALGORITHM (works with other valid input values)
    # 1. Identify the example input values and initialize the variables/data structures.
    # 2. Import the standard-library or third-party tools required by this program.
    # 3. Process the values in a loop, updating intermediate results or model parameters as
    #    needed.
    # 4. Transform the data and calculate predictions, scores, losses, or term weights as
    #    appropriate.
    # 5. Print or return the final result for the supplied input, then stop.


