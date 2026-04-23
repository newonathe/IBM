n = int(input())
for i in range(n):
    star_space = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(star_space + stars)

for i in range(n - 2, -1, -1):
    star_space = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(star_space + stars)

#find the sum of all even numbers in a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in nums:
    if n % 2 == 0:
        total += n

print(total)

#count numbers greater than five. takes a list
def countGreaterThanFive(num):
    count = 0
    for n in num:
        if n > 5:
            count += 1
    return count
 
num = nums
print(countGreaterThanFive(num))

# Check if a string is a palindrome (reads same forward and backward)
# "racecar" → palindrome, "hello" → not

def is_palindrome(s):    
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

def is_palindrome_easy(s):
    return s == s.reverse()

def two_sum_sorted(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1    
    return []
    
# Check if two strings are anagrams
# "listen" and "silent" → same characters, different order → anagram!

def check_if_anagram(wordOne, wordTwo):
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()
    
    if len(wordOne) != len(wordTwo):
        return False

    count = {}

    for char in wordOne:
        count[char] = count.get(char, 0) + 1
    
    for char in wordTwo:
        count[char] = count.get(char, 0) - 1
    
    for value in count.values():
        if value != 0:
            return False
    
    return True

def is_frequent(nums):
    if len(nums) <= 0:
        return None
    
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    most_common = max(freq, key=freq.get())

    return most_common

# Find the second largest number

def is_second_largest_num(nums):
    sorted_nums = sorted(set(nums))

    if len(sorted_nums) < 2:
        return None
    
    return sorted_nums[-2]

def is_second_largest_num_fast(nums):
    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n

    if second != float('-inf'):
        return second 
    
    return None

#find the median
def median(arr):
    sorted_arr = sorted(arr)
    n = len(arr)

    if n % 2 == 0:
        return (sorted_arr[n // 2] + sorted_arr[n // 2 - 1])/2
    else:
        return (sorted_arr[n//2])
    
