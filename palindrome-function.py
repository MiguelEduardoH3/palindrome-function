if __name__ == '__main__':
    def is_palindrome(sentence):
        palindrome_order = ""
        palindrome_reverse = ""
        for letter in sentence.strip():
            if letter != ' ':
                palindrome_order = palindrome_order + letter
                palindrome_reverse = letter + palindrome_reverse
        if palindrome_order == palindrome_reverse:
            return True
        return False


sent = input('Write your sentence, to verify if it is a palindrome or not: ')
print(is_palindrome(sent))
