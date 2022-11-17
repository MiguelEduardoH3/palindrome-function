def is_palindrome(input_phrase):
    right_phrase = ""
    reverse_phrase = ""
    for letter in input_phrase.strip():
        if letter != ' ':
            right_phrase = right_phrase + letter
            reverse_phrase =  letter + reverse_phrase
    if right_phrase.lower() == reverse_phrase.lower():
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
