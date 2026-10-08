
def reverse_string(text):

    chars = list(text) 

    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)



text = "hello"
print(reverse_string(text))

print(reverse_string(""))        # ""
print(reverse_string("a"))       # "a"
print(reverse_string("ab"))      # "ba"
print(reverse_string("level"))   # "level"