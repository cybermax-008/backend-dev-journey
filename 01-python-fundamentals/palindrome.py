def palindrome(word):
    # make all words lower case and remove any non-alphanumeric characters
    lower_case = word.lower()
    # cancatenate all words together after removing all non-alphanumerical characters
    cancatenated_words = ''.join(char for char in lower_case if char.isalnum())
    return cancatenated_words == cancatenated_words[::-1]


# Test cases
test_words = ["racecar", "Hello", "A man a plan a canal Panama", "python"]

#Run tests

for word in test_words:
    if palindrome(word):
        print (f"{word} is a palindrome")
    else:
        print (f"{word} is not a palindrome")