def is_palindrome(text):

    left = 0
    right = len(text) -1

    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


text = "madam"
print(is_palindrome(text))
text = "level"
print(is_palindrome(text))
text = "radar"
print(is_palindrome(text))


#  failed test cases
text = "python"
print(is_palindrome(text))
text = "javascript"
print(is_palindrome(text))


#  edge cases
text = ""
print(is_palindrome(text))
text = "a"
print(is_palindrome(text))
text = "ab"
print(is_palindrome(text))
text = "aaa"
print(is_palindrome(text))