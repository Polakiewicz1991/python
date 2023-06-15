# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
x = list(input("Podaj warotść: "))

def palindrome(x):
    i = 0
    print(x)
    y = list(reversed(x))
    print(y)
    while i < len(x):
        if x[i] == y[i]:
            i += 1
        else:
            return False
    return True

print(palindrome(x))